#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n ^ 3)


b) O(n * (n - 1)/2)


c) O(n)

## Exercise II

arr = array of all floors indication break of not e.g. [False, False, False, True]
n = number of floors
c = number of drops + number of eggs broken
min = min floor
f = first floor where egg breaks

# call egg_drop with (arr, 0, 0)

## egg_drop (arr, c, min)
base case if n = 2
# drop an egg from the ground floor
    if it breaks (arr[0] == True)
        return [c + 2, min]
    else (arr[1] == False)
        return [c + 1, min + 1]

# find half point - 
half = (n / 2) -> int
# if middle floor DOESN'T break and middle floor + 1 DOES
# count equals previous count + 3 and floor equals min + 1
if arr[half] == False and arr[half + 1] == True
    return [c + 3, min + 1]

# if middle floor and middle floor + 1 DON'T break 
# redo egg_drop with top half, add 2 to count 
if arr[half] == False and arr[half + 1] == False
    return egg_drop(arr[half:], c + 2, min + half)

# if middle floor and middle floor + 1 DO break e.g. 
# redo egg_drop with bottom half, add 4 to count
if arr[half] == True and arr[half + 1] == True
    return egg_drop(arr[:half], c + 4, min)
