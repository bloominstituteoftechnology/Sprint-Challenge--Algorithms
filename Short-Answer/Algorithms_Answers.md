#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)

b)
O(log n)

c)
O(n)

## Exercise II


assume stories >= 1

lowest_break = stories + 1
highest_unbroken = 0

while lowest_break - highest_unbroken > 1:
    test_floor = round(lowest_break + highest_unbroken)
    if did_break(test_floor):
        lowest_break = test_floor
    else:
        highest_unbroken = test_floor

return lowest_break


Runtime: O(log n)


