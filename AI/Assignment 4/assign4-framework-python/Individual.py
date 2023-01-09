import random


# Author Fan Zhang
class Individual:
    def __init__(self, map):
        self.map = map  # the map
        self.fitness = 0  # fitness is cached and only updated on request whenever necessary
        # TODO some representation of the genom of the individual
        # TODO implement random generation of an individual
        self.color = [0, 1, 2, 3]
        self.statescolor = []
        for i in range(len(map.states)):
            r = random.randint(0, 3)
            self.statescolor.append(self.color[r])
        self.updateFitness()

    # Updates the fitness value based on the genom and the map.
    def updateFitness(self):
        # TODO implement fitness function
        sum_fitness = 0
        for i in range(len(self.map.states)):
            for j in range(len(self.map.borders)):  # 对每一个states， 查看所有的边界点
                if self.map.borders[j].index1 == i: # j=0 (0,1) #如果当前的这个州，有相邻节点的话
                    if self.statescolor[i] != self.statescolor[self.map.borders[j].index2]:
                        # statescolor[i]是自己的颜色， self.map.borders[j]是正在比较的边界。
                        # index1是当前节点的state index。 index2就是相邻的一个州了。 如果这个州的颜色， 跟当前州的颜色不同，那么就是不冲突的配色，可以保留。 这里就适应度+1
                        # print("self.map.borders[j] = "+ str(self.map.borders[j]))
                        print(self.map.borders[j].__dict__)

                        sum_fitness += 1
        self.fitness = sum_fitness

    # Reproduces a child randomly from two individuals (see textbook).
    # x The first parent.
    # y The second parent.
    # return The child created from the two individuals.
    def reproduce(self, x, y):
        child1 = Individual(x.map)
        # TODO reproduce child from individuals x and y
        r = random.uniform(0, len(x.statescolor))
        for i in range(len(x.statescolor)):
            if i < r:
                child1.statescolor[i] = x.statescolor[i]
            else:
                child1.statescolor[i] = y.statescolor[i]
        child1.updateFitness()

        child2 = Individual(x.map)
        for i in range(len(x.statescolor)):
            if i > r:
                child2.statescolor[i] = x.statescolor[i]
            else:
                child2.statescolor[i] = y.statescolor[i]
        child2.updateFitness()
        if child1.fitness > child2.fitness:
            return child1
        else:
            return child2

    # Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual
        r = random.randint(0, len(self.statescolor) - 1)
        c = random.randint(0, 3)
        self.statescolor[r] = c
        self.updateFitness()

    # Checks whether the individual represents a valid goal state.
    # return Whether the individual represents a valid goal state.
    def isGoal(self):
        print("fitness: ", self.fitness," goal fitness: ", len(self.map.borders))
        return self.fitness == len(self.map.borders)

    def printresult(self):
        print("Your result:")
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...
        print("Result:")
        print("fitness: ", self.fitness)
        print("0,1,2,3 are the four different colors of states")
        for i in range(len(self.statescolor)):
            print(self.map.states[i], ": ", self.statescolor[i])
