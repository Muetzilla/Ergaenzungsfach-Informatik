from numpy.random import random

class Animal:
    max_deadly_mutations = 3
    reproduction_probability = 0.2
    min_reproduction_age = 8
    num_descendents = 1
    mutation_probability = 0.02
    multiple_descendents_probability = 0.2
    radiation_mutation_probability = 0.005
    max_reproduction_age = 10

    def __init__(self, genom):
        self.genom = genom
        self.age = 0

    def __str__(self):
        return f"Animal(age={self.age}, genom={self.genom})"

    def is_alive(self):
        if self.age >= len(self.genom):
            return False
        deadly_mutations = sum(self.genom[:self.age])

        if deadly_mutations >= self.__class__.max_deadly_mutations:
            return False
        return True

    def number_of_descendents(self):
        descendants = self.__class__.num_descendents
        while random() <= self.__class__.multiple_descendents_probability ** descendants:
            descendants += 1
        return descendants

    def descendents(self):
        desc = []
        if self.__class__.max_reproduction_age < self.age or self.age > self.__class__.min_reproduction_age:
            if random() <= self.__class__.reproduction_probability:
               for i in range(self.number_of_descendents()):
                     desc.append(self.clone())
        return desc

    def clone(self):
        genome = self.genom.copy()
        for i in range(len(genome)):
            if random() <= self.__class__.mutation_probability:
               genome[i] = not genome[i]
        return Animal(genome)


    def age_one_year(self):
        self.age += 1


    def mutate(self):
        for i in range(len(self.genom)):
            if random() <= self.__class__.radiation_mutation_probability:
                self.genom[i] = not self.genom[i]
