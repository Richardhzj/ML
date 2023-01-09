import random

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population


# Author Fan Zhang
def initMap(map):
    map.states.append("North Carolina")  # 0
    map.states.append("South Carolina")  # 1
    map.states.append("Virginia")  # 2
    map.states.append("Tennessee")  # 3
    map.states.append("Kentucky")  # 4
    map.states.append("West Virginia")  # 5
    map.states.append("Georgia")  # 6
    map.states.append("Alabama")  # 7
    map.states.append("Mississippi")  # 8
    map.states.append("Florida")  # 9

    map.borders.append(Border(0, 1))
    map.borders.append(Border(0, 2))
    map.borders.append(Border(0, 3))
    map.borders.append(Border(0, 6))
    map.borders.append(Border(1, 6))
    map.borders.append(Border(2, 3))
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 6))
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.borders.append(Border(4, 5))
    map.borders.append(Border(6, 7))
    map.borders.append(Border(6, 9))
    map.borders.append(Border(7, 8))
    map.borders.append(Border(7, 9))


if __name__ == '__main__':
    map = Map()
    initMap(map)
    populationSize = 100  # TODO find reasonable value
    population = Population(map, populationSize)  # 应该是生成100份不一样的着色图

    maxIterations = 500  # TODO find reasonable value
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map)  # to hold the individual representing the goal, if any
    mark = 0
    while currentIteration < maxIterations and goalFound == False:
        newPopulation = Population(map, 0)
        best_parent = Individual(map)
        worst_child = Individual(map)
        for i in range(populationSize):
            x, y = population.randomSelection()
            if x.fitness > y.fitness:
                if best_parent.fitness < x.fitness:
                    best_parent = x
            else:
                if best_parent.fitness < y.fitness:
                    best_parent = y
            child = Individual.reproduce(x, x, y)
            pmutate = random.random()
            if pmutate < 0.3:  # TODO use small probability instead
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
                mark = 1
                break
            newPopulation.vector.append(child)
        currentIteration += 1
        if mark == 1:
            break

        worst_mark = 0
        for i in range(len(newPopulation.vector)):
            if newPopulation.vector[i].fitness < worst_child.fitness:
                worst_child = newPopulation.vector[i]
                worst_mark = i
        newPopulation.vector[worst_mark] = best_parent
        population = newPopulation

    if goalFound:
        print("Found a solution after ", currentIteration, " iterations")
        bestIndividual.printresult()
    else:
        print("Did not find a solution after ", currentIteration, " iterations")
