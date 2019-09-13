def find_f(floor):
    low = 0
    high = len(floor)  - 1
    while low < high:
        mid = (low + high) / 2
        if floor[mid] == 1:
            if floor[mid-1]== 0:
                return mid
            else:
                high = mid - 1
        elif floor[mid] == 0:
            if floor[mid+1] == 1:
                return mid + 1
            else:
                low = mid +1


print (find_f([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))