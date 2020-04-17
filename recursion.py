import math


def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
# print(deliver_presents_recursively(houses))

a = []
b = [1]
c = [2]
# print(a + b + c)


def find_section(n):
    counter = 1
    halves = 8

    for halve in range(0, halves):
        print(f"{halve} half: {n/2**halve}")


find_section(100)

print(math.ceil(25.0000001))
