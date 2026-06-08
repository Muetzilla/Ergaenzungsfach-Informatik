import os
import json
from datetime import datetime
from uuid import uuid4

import pandas as pd
import matplotlib.pyplot as plt

from pennamodell.optimized_animal import Animal


# ============================================================
# Helper Functions
# ============================================================

def get_average_population_age(population):
    if len(population) == 0:
        return 0.0

    return sum(animal.age for animal in population) / len(population)


# ============================================================
# Single Simulation
# ============================================================

def run_single_simulation(
    iteration,
    num_initial_population,
    initial_defect_probability,
    max_years,
):
    population = [
        Animal(
            Animal.random_genome(initial_defect_probability)
        )
        for _ in range(num_initial_population)
    ]

    results = []

    for year in range(max_years + 1):

        results.append(
            {
                "iteration": iteration,
                "year": year,
                "population_size": len(population),
                "average_age": get_average_population_age(population),
            }
        )

        if year == max_years or len(population) == 0:
            continue

        new_population = []

        for animal in population:
            animal.age_one_year()

            if animal.is_alive():
                new_population.append(animal)
                new_population.extend(animal.descendents())
                animal.mutate()

        population = new_population

    return results


# ============================================================
# Monte Carlo Simulation
# ============================================================

def run_monte_carlo_simulation(
    n_iterations,
    num_initial_population,
    initial_defect_probability,
    max_years,
):
    all_results = []

    for iteration in range(n_iterations):
        print(f"Running simulation {iteration + 1}/{n_iterations}")

        all_results.extend(
            run_single_simulation(
                iteration=iteration,
                num_initial_population=num_initial_population,
                initial_defect_probability=initial_defect_probability,
                max_years=max_years,
            )
        )

    return pd.DataFrame(all_results)


# ============================================================
# Parameters
# ============================================================

num_initial_population = 30
initial_defect_probability = 0.04
max_years = 10000
n_iterations = 10

Animal.num_genes = 32
Animal.max_deadly_mutations = 3
Animal.reproduction_probability = 0.175
Animal.min_reproduction_age = 8
Animal.max_reproduction_age = 28
Animal.num_descendents = 1
Animal.multiple_descendents_probability = 0.2
Animal.mutation_probability = 0.07
Animal.radiation_mutation_probability = 0.0015


# ============================================================
# Create Unique Run Folder
# ============================================================

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
run_id = uuid4().hex[:8]

run_name = (
    f"{timestamp}"
    f"_N{num_initial_population}"
    f"_R{Animal.reproduction_probability}"
    f"_M{Animal.mutation_probability}"
    f"_{run_id}"
)

run_dir = os.path.join("simulation_results", run_name)
os.makedirs(run_dir, exist_ok=True)

print()
print("=" * 60)
print("RUN DIRECTORY:")
print(run_dir)
print("=" * 60)
print()


# ============================================================
# Save Configuration
# ============================================================

config = {
    "genome_representation": "uint32_bitmask_with_Animal_class",
    "num_initial_population": num_initial_population,
    "initial_defect_probability": initial_defect_probability,
    "max_years": max_years,
    "n_iterations": n_iterations,

    "Animal.num_genes": Animal.num_genes,
    "Animal.max_deadly_mutations": Animal.max_deadly_mutations,
    "Animal.reproduction_probability": Animal.reproduction_probability,
    "Animal.min_reproduction_age": Animal.min_reproduction_age,
    "Animal.max_reproduction_age": Animal.max_reproduction_age,
    "Animal.num_descendents": Animal.num_descendents,
    "Animal.multiple_descendents_probability": Animal.multiple_descendents_probability,
    "Animal.mutation_probability": Animal.mutation_probability,
    "Animal.radiation_mutation_probability": Animal.radiation_mutation_probability,
}

with open(os.path.join(run_dir, "config.json"), "w") as f:
    json.dump(config, f, indent=4)


# ============================================================
# Run Monte Carlo
# ============================================================

df = run_monte_carlo_simulation(
    n_iterations=n_iterations,
    num_initial_population=num_initial_population,
    initial_defect_probability=initial_defect_probability,
    max_years=max_years,
)


# ============================================================
# Save Raw Data
# ============================================================

raw_file = os.path.join(run_dir, "raw_results.csv")
df.to_csv(raw_file, index=False)


# ============================================================
# Summary Statistics
# ============================================================

summary_df = (
    df.groupby("year")
    .agg(
        mean_population=("population_size", "mean"),
        std_population=("population_size", "std"),
        min_population=("population_size", "min"),
        max_population=("population_size", "max"),

        mean_age=("average_age", "mean"),
        std_age=("average_age", "std"),
        min_age=("average_age", "min"),
        max_age=("average_age", "max"),
    )
    .reset_index()
)

summary_file = os.path.join(run_dir, "summary.csv")
summary_df.to_csv(summary_file, index=False)


# ============================================================
# Final Statistics
# ============================================================

final_year = df["year"].max()
final_values = df[df["year"] == final_year]

final_stats = {
    "final_year": int(final_year),
    "mean_final_population": float(final_values["population_size"].mean()),
    "std_final_population": float(final_values["population_size"].std()),
    "mean_final_age": float(final_values["average_age"].mean()),
    "std_final_age": float(final_values["average_age"].std()),
    "extinction_rate": float((final_values["population_size"] == 0).mean()),
}

final_stats_file = os.path.join(run_dir, "final_statistics.json")

with open(final_stats_file, "w") as f:
    json.dump(final_stats, f, indent=4)


# ============================================================
# Plot
# ============================================================

years = summary_df["year"]

fig, axs = plt.subplots(
    2,
    1,
    figsize=(10, 8),
    sharex=True,
)

axs[0].plot(
    years,
    summary_df["mean_population"],
    linewidth=2,
    label="Mean population",
)

axs[0].fill_between(
    years,
    summary_df["mean_population"] - summary_df["std_population"],
    summary_df["mean_population"] + summary_df["std_population"],
    alpha=0.25,
    label="±1 std",
)

axs[0].set_ylabel("Population Size")
axs[0].set_title(f"Penna Monte Carlo Simulation, n={n_iterations}")
axs[0].grid(True)
axs[0].legend()

axs[1].plot(
    years,
    summary_df["mean_age"],
    linewidth=2,
    label="Mean age",
)

axs[1].fill_between(
    years,
    summary_df["mean_age"] - summary_df["std_age"],
    summary_df["mean_age"] + summary_df["std_age"],
    alpha=0.25,
    label="±1 std",
)

axs[1].set_xlabel("Time in years")
axs[1].set_ylabel("Average Age")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()

plot_file = os.path.join(run_dir, "plot.png")

plt.savefig(
    plot_file,
    dpi=300,
    bbox_inches="tight",
)

plt.show()


# ============================================================
# Report
# ============================================================

print()
print("=" * 60)
print("RUN COMPLETE")
print("=" * 60)

print(f"Mean final population: {final_stats['mean_final_population']:.2f}")
print(f"Population std: {final_stats['std_final_population']:.2f}")
print(f"Mean final age: {final_stats['mean_final_age']:.2f}")
print(f"Extinction rate: {100 * final_stats['extinction_rate']:.2f}%")

print()
print("Saved files:")
print(raw_file)
print(summary_file)
print(plot_file)
print(os.path.join(run_dir, "config.json"))
print(final_stats_file)