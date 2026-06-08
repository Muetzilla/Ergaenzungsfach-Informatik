from numpy.random import random
import numpy as np

class Animal:
    max_deadly_mutations = 3
    reproduction_probability = 0.2
    min_reproduction_age = 8
    max_reproduction_age = 28

    num_descendents = 1
    multiple_descendents_probability = 0.2

    mutation_probability = 0.02
    radiation_mutation_probability = 0.005

    num_genes = 32

    def __init__(self, genome):
        self.genome = np.uint32(genome)
        self.age = 0

    def __str__(self):
        return f"Animal(age={self.age}, genome={self.genome:032b})"

    @classmethod
    def random_genome(cls, defect_probability):
        genome = np.uint32(0)

        for gene_index in range(cls.num_genes):
            if random() <= defect_probability:
                genome |= np.uint32(1 << gene_index)

        return genome

    @staticmethod
    def count_bits(value):
        return bin(int(value)).count("1")

    def active_gene_mask(self):
        if self.age >= self.__class__.num_genes:
            return np.uint32(0xFFFFFFFF)

        return np.uint32((1 << self.age) - 1)

    def is_alive(self):
        if self.age >= self.__class__.num_genes:
            return False

        active_genes = self.genome & self.active_gene_mask()
        deadly_mutations = self.count_bits(active_genes)

        return deadly_mutations < self.__class__.max_deadly_mutations

    def number_of_descendents(self):
        descendants = self.__class__.num_descendents

        while random() <= (
            self.__class__.multiple_descendents_probability ** descendants
        ):
            descendants += 1

        return descendants

    def can_reproduce(self):
        return (
            self.__class__.min_reproduction_age
            <= self.age
            <= self.__class__.max_reproduction_age
        )

    def descendents(self):
        children = []

        if self.can_reproduce():
            if random() <= self.__class__.reproduction_probability:
                for _ in range(self.number_of_descendents()):
                    children.append(self.clone())

        return children

    def clone(self):
        child_genome = np.uint32(self.genome)

        for gene_index in range(self.__class__.num_genes):
            if random() <= self.__class__.mutation_probability:
                child_genome ^= np.uint32(1 << gene_index)

        return Animal(child_genome)

    def age_one_year(self):
        self.age += 1

    def mutate(self):
        for gene_index in range(self.__class__.num_genes):
            if random() <= self.__class__.radiation_mutation_probability:
                self.genome ^= np.uint32(1 << gene_index)