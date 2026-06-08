from numpy.random import random
from pennamodell.animal import Animal
import matplotlib.pyplot as plt


def generate_random_genom(num_gens, defect_probability):
    return [bernoulli_variable(defect_probability) for _ in range(num_gens)]


def bernoulli_variable(probability):
    if random() <= probability:
        return True
    return False


def get_average_population_age(population):
    N = len(population)
    if N == 0:
        return 0
    return sum(a.age for a in population) / N


#Simulation

#Parameter
num_initial_population = 20
num_genes = 32
initial_defect_probability = 0.04
max_years = 400

#Class attribute
Animal.max_deadly_mutations = 3
Animal.reproduction_probability = 0.12
Animal.min_reproduction_age = 8
Animal.num_descendents = 1
Animal.mutation_probability = 0.05
Animal.radiation_mutation_probability = 0.0015
Animal.max_reproduction_age = 28

population = [Animal(generate_random_genom(num_genes, initial_defect_probability)) for i in range(num_initial_population)]

num_animals = [len(population)]
years = [0]
average_population_age = [get_average_population_age(population)]

#Simulatin Loop
for t in range(1, max_years + 1):
    new_population = []
    for animal in population:
        animal.age_one_year()
        if animal.is_alive():
            new_population.append(animal)
            new_population += animal.descendents()
            animal.mutate()
    population = new_population

    #Messungen
    years.append(t)
    num_animals.append(len(population))
    average_population_age.append(get_average_population_age(population))


print(num_animals)
print(years)
print(average_population_age)

print(f"Final Values (after {years[-1]} years):")
print("Final population:", num_animals[-1])
print("Final average age:", average_population_age[-1])

a = years
b = num_animals
c = average_population_age

# Zwei Subplots untereinander, gemeinsame x-Achse
fig, axs = plt.subplots(2, 1, figsize=(6, 4), sharex=True)

axs[0].plot(a, b, "o-r")
axs[0].set_ylabel("Populationsgrösse")
axs[0].set_title("Populationsgrösse der Penna-Population")
axs[0].grid(True)

axs[1].plot(a, c, ".-b")
axs[1].set_xlabel("Zeit t in Jahren")
axs[1].set_ylabel("Durchschnittsalter")
axs[1].grid(True)

plt.tight_layout()
plt.show()