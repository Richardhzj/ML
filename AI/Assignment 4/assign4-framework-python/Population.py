# Class representing a population of individuals
# Author Fan Zhang
import random

from Individual import Individual


class Population:
    # Actual standard ctor.
    # param map The map.
    # param initialSize The initial size of the population.
    def __init__(self, map, initialSize):
        self.vector = []
        for i in range(initialSize):
            self.vector.append(Individual(map))

    # Randomly selects an individual out of the population
    # proportionally to its fitness.
    # return The selected individual.
    def randomSelection(self):
        # TODO implement random selection
        # an individual should be selected with a probability
        # proportional to its fitness
        sum_fitness = 0
        for i in range(len(self.vector)):
            sum_fitness += self.vector[i].fitness
        fitness_list = []
        for i in range(len(self.vector)):
            fitness_list.append(float(self.vector[i].fitness) / float(sum_fitness))
        r = random.choices(self.vector, weights=fitness_list, k=2)

        while r[0] == r[1]:
            r = random.choices(self.vector, weights=fitness_list, k=2)
        return r[0], r[1]
