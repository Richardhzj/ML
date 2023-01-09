import random


def trial():
    coins = 10
    number_of_players = 0
    count = 0
    while coins >= 1:
        coins -= 1
        number_of_players += 1
        slots = [random.choice(
            ["BAR", "BELL", "LEMON", "CHERRY"])
                 for i in range(3)]
        if slots[0] == slots[1]:
            if slots[1] == slots[2]:
                count = 3
                #print("count =3")
            else:
                count = 2
        else:
            count = 1
    if slots[0] == "CHERRY":
        coins += count
    elif count == 3:
        if slots[0] == "BAR":
            coins += 20
        elif slots[0] == "BELL":
            coins += 15
        else:
            coins += 5
    print(coins)
    return coins


def demo(trials):
    results = [trial() for i in range(trials)]

    print(results)
    mean = sum(results) / float(trials)

    median = sorted(results)[int(trials / 2)]
    print("Number of trials: ", trials)

    print("Mean: ", mean)

    print("Median: ", median)

if __name__ == "__main__":
    demo(100)

