import math
import random


def find_floor(n, bp, floor=0, counter=1):
    print(f"n={n}")
    print(f"floor={floor}")
    print(f"floor-n/(2^counter)= {floor - (n/2**counter)}")

    if round(floor, 5) == round(floor - (n/2**counter), 5):
        print(
            f"Egg breaks on floor: {round(floor)} = breakpoint: {bp}")
        return

    if floor < bp:
        floor = round(floor + n/(2**counter), 5)
        counter += 1
        print(counter)

        find_floor(n, bp, floor, counter)

    else:
        floor = round(floor - n/(2**counter), 5)
        counter += 1
        find_floor(n, bp, floor, counter)


n = 10000000000000
break_point = random.randrange(500, n)
print(break_point)
find_floor(n, 648)


# if floor < bp
# if floor > bp
