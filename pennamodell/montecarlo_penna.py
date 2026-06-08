from numpy.random import random
from pennamodell.animal import Animal

import matplotlib.pyplot as plt
import pandas as pd

from datetime import datetime
from uuid import uuid4

import json
import os


# ============================================================
# Helper Functions
# ============================================================

def bernoulli_variable(probability):
    return random() <= probability


def generate_random_genom(num_gens, defect_probability):
    return [
        bernoulli_variable(defect_probability)
        for _ in range(num_gens)
    ]


def get_average_population_age(population):
    if len(population) == 0:
        return 0

    return sum(a.age for a in population) / len(population)


# ============================================================
# Single Simulation
# ============================================================

def run_single_simulation(
    iteration,
    num_initial_population,
    num_genes,
    initial_defect_probability,
    max_years,
):
    population = [
        Animal(
            generate_random_genom(
                num_genes,
                initial_defect_probability
            )
        )
        for _ in range(num_initial_population)
    ]

    results = []

    for t in range(max_years + 1):

        results.append(
            {
                "iteration": iteration,
                "year": t,
                "population_size": len(population),
                "average_age": get_average_population_age(population),
            }
        )

        new_population = []

        for animal in population:

            animal.age_one_year()

            if animal.is_alive():
                new_population.append(animal)

                new_population += animal.descendents()

                animal.mutate()

        population = new_population

    return results


# ============================================================
# Monte Carlo Simulation
# ============================================================

def run_monte_carlo_simulation(
    n_iterations,
    num_initial_population,
    num_genes,
    initial_defect_probability,
    max_years,
):
    all_results = []

    for i in range(n_iterations):

        print(
            f"Running simulation "
            f"{i + 1}/{n_iterations}"
        )

        simulation_results = run_single_simulation(
            iteration=i,
            num_initial_population=num_initial_population,
            num_genes=num_genes,
            initial_defect_probability=initial_defect_probability,
            max_years=max_years,
        )

        all_results.extend(simulation_results)

    return pd.DataFrame(all_results)


# ============================================================
# Parameters
# ============================================================

num_initial_population = 30
num_genes = 32
initial_defect_probability = 0.04
max_years = 400

# Monte Carlo iterations
n_iterations = 10

# ============================================================
# Animal Parameters
# ============================================================

Animal.max_deadly_mutations = 3
Animal.reproduction_probability = 0.15
Animal.min_reproduction_age = 8
Animal.num_descendents = 1
Animal.mutation_probability = 0.07
Animal.radiation_mutation_probability = 0.0015
Animal.max_reproduction_age = 28

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

run_dir = os.path.join(
    "simulation_results",
    run_name
)

os.makedirs(run_dir, exist_ok=True)

print()
print("=" * 60)
print(f"RUN DIRECTORY:")
print(run_dir)
print("=" * 60)
print()

# ============================================================
# Save Configuration
# ============================================================

config = {
    "num_initial_population": num_initial_population,
    "num_genes": num_genes,
    "initial_defect_probability": initial_defect_probability,
    "max_years": max_years,
    "n_iterations": n_iterations,

    "Animal.max_deadly_mutations":
        Animal.max_deadly_mutations,

    "Animal.reproduction_probability":
        Animal.reproduction_probability,

    "Animal.min_reproduction_age":
        Animal.min_reproduction_age,

    "Animal.num_descendents":
        Animal.num_descendents,

    "Animal.mutation_probability":
        Animal.mutation_probability,

    "Animal.radiation_mutation_probability":
        Animal.radiation_mutation_probability,

    "Animal.max_reproduction_age":
        Animal.max_reproduction_age,
}

with open(
    os.path.join(run_dir, "config.json"),
    "w",
) as f:
    json.dump(config, f, indent=4)

# ============================================================
# Run Monte Carlo
# ============================================================

df = run_monte_carlo_simulation(
    n_iterations=n_iterations,
    num_initial_population=num_initial_population,
    num_genes=num_genes,
    initial_defect_probability=initial_defect_probability,
    max_years=max_years,
)

# ============================================================
# Save Raw Data
# ============================================================

raw_file = os.path.join(
    run_dir,
    "raw_results.csv"
)

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

summary_file = os.path.join(
    run_dir,
    "summary.csv"
)

summary_df.to_csv(
    summary_file,
    index=False
)

# ============================================================
# Final Statistics
# ============================================================

final_year = df["year"].max()

final_values = df[df["year"] == final_year]

final_stats = {
    "final_year": int(final_year),

    "mean_final_population":
        float(
            final_values["population_size"].mean()
        ),

    "std_final_population":
        float(
            final_values["population_size"].std()
        ),

    "mean_final_age":
        float(
            final_values["average_age"].mean()
        ),

    "std_final_age":
        float(
            final_values["average_age"].std()
        ),

    "extinction_rate":
        float(
            (
                final_values["population_size"] == 0
            ).mean()
        ),
}

with open(
    os.path.join(
        run_dir,
        "final_statistics.json"
    ),
    "w",
) as f:
    json.dump(final_stats, f, indent=4)

# ============================================================
# Plot
# ============================================================

years = summary_df["year"]

fig, axs = plt.subplots(
    2,
    1,
    figsize=(10, 8),
    sharex=True
)

# ------------------------------------------------------------
# Population
# ------------------------------------------------------------

axs[0].plot(
    years,
    summary_df["mean_population"],
    linewidth=2,
    label="Mean population"
)

axs[0].fill_between(
    years,
    summary_df["mean_population"]
    - summary_df["std_population"],
    summary_df["mean_population"]
    + summary_df["std_population"],
    alpha=0.25,
    label="±1 Std"
)

axs[0].set_ylabel(
    "Population Size"
)

axs[0].set_title(
    f"Penna Monte Carlo Simulation "
    f"(n={n_iterations})"
)

axs[0].grid(True)
axs[0].legend()

# ------------------------------------------------------------
# Age
# ------------------------------------------------------------

axs[1].plot(
    years,
    summary_df["mean_age"],
    linewidth=2,
    label="Mean age"
)

axs[1].fill_between(
    years,
    summary_df["mean_age"]
    - summary_df["std_age"],
    summary_df["mean_age"]
    + summary_df["std_age"],
    alpha=0.25,
    label="±1 Std"
)

axs[1].set_xlabel(
    "Time (years)"
)

axs[1].set_ylabel(
    "Average Age"
)

axs[1].grid(True)
axs[1].legend()

plt.tight_layout()

plot_file = os.path.join(
    run_dir,
    "plot.png"
)

plt.savefig(
    plot_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# Report
# ============================================================

print()
print("=" * 60)
print("RUN COMPLETE")
print("=" * 60)

print(
    f"Mean final population: "
    f"{final_stats['mean_final_population']:.2f}"
)

print(
    f"Population std: "
    f"{final_stats['std_final_population']:.2f}"
)

print(
    f"Mean final age: "
    f"{final_stats['mean_final_age']:.2f}"
)

print(
    f"Extinction rate: "
    f"{100 * final_stats['extinction_rate']:.2f}%"
)

print()
print("Saved files:")
print(raw_file)
print(summary_file)
print(plot_file)
print(
    os.path.join(
        run_dir,
        "config.json"
    )
)
print(
    os.path.join(
        run_dir,
        "final_statistics.json"
    )
)