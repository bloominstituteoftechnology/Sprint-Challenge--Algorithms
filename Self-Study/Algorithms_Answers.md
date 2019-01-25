Exercise I

a: This psuedocode has a runtime of O(n). Since "a" grows by n^2 every time the loop runs, it only takes n times to be equal to n^3.

b: The first loop runs n times, while the second and third loops run less than n times due to running on a range with an incremented start. The fourth loop will always run greater than n times because of the range it's given. The runtime is at least O(n^2).

c: The runtime is O(n), nothing increases n so it will only run n times.

Exercise II

If n is a sorted list of floors and k is an unknown floor that we must find then I'd do something like this:

def noBrokenEggs(n, k, low, high):
    middle = int((low+high)/2)
    
    if egg thrown from middle is broken:
        noBrokenEggs(n[middle:], k, middle, len(n))
    elif middle == k:
        return n[middle]
    else:
        noBrokenEggs(n[:middle], k, 0, middle)

The case time complexity is O(log n). We immediately cut down the list, so it isn't possible to search n times.