from copy import deepcopy

# index 0: missionaries, index 1: cannibals
actions = [[1, 1], [0, 2], [2, 0], [0, 1], [1, 0]]


class State:

    def __init__(self, left, boat, right):
        self.left = left
        self.boat = boat
        self.right = right
        self.prev = None

    def __eq__(self, other):
        return (self.left[0] == other.left[0] and self.left[1] == other.left[1] and self.right[0] == other.right[0] and
                self.right[1] == other.right[1] and self.boat == other.boat)

    def __hash__(self):
        return hash((self.left[0], self.left[1], self.boat, self.right[0], self.right[1]))

    def isValidState(self):
        # The number of cannibals can't be larger than the number of missionaries on both side of the river
        if 0 < self.left[0] < self.left[1] or 0 < self.right[0] < self.right[1]:
            return False

        if self.left[0] < 0 or self.left[1] < 0 or self.right[0] < 0 or self.right[1] < 0:
            return False

        return True

    # goal state
    def allToTheRight(self):
        # send all the people to the right side of the river and make sure the total number of people for people is 6
        return self.left[0] == 0 and self.left[1] == 0 and self.right[0] == 3 and self.right[0] == 3


def nextStates(current):
    nodes = []

    for action in actions:

        nextState = deepcopy(current)
        nextState.prev = current

        # check the current position of the boat
        nextState.boat = 1 - current.boat

        # Moving from left to right
        if current.boat == 0:

            # Right population increases
            nextState.right[0] += action[0]
            nextState.right[1] += action[1]

            # Left population decreases
            nextState.left[0] -= action[0]
            nextState.left[1] -= action[1]

        # Moving from right to left
        elif current.boat == 1:

            # Right population decreases
            nextState.right[0] -= action[0]
            nextState.right[1] -= action[1]

            # Left population increases
            nextState.left[0] += action[0]
            nextState.left[1] += action[1]

        if nextState.isValidState():
            nodes.append(nextState)

    return nodes


def bfs(root):
    if root.allToTheRight():
        return root

    visited = set()
    queue = [root]
    while queue:
        state = queue.pop()
        if state.allToTheRight():
            return state

        visited.add(state)

        for s in nextStates(state):
            if s in visited:
                continue

            if s not in queue:
                queue.append(s)


def main():
    initial_state = State([3, 3], 0, [0, 0])

    state = bfs(initial_state)

    # build path
    path = []
    while state:
        path.append(state)
        state = state.prev

    # reverse path
    path = path[::-1]

    for state in path:
        if state.boat:
            print("""{:3} |         b| {:3}\n{:3} |          | {:3}""".format("c" * state.left[1], "c" * state.right[1],
                                                                              "m" * state.left[0],
                                                                              "m" * state.right[0]))
        else:
            print("""{:3} |b         | {:3}\n{:3} |          | {:3}""".format("c" * state.left[1], "c" * state.right[1],
                                                                              "m" * state.left[0],
                                                                              "m" * state.right[0]))
        print("--------------------")


if __name__ == "__main__":
    main()
