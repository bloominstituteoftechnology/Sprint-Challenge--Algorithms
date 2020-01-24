# n = 20000
#
# def finder(n):
#     counter = 0
#     for i in range(n):
#         j = 1
#         while j < n:
#             j *= 2
#             print(j)
#             counter += 1
#             print(f'counter = {counter}')
#
#

def finder2(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
        # print(a)


# def bunnyEars(n):
#     if n == 0:
#         return 0
#     print(n)
#     return 2 + bunnyEars(n - 1)
#
#
#
import time
start_time = time.time()
print(finder2(100))
end_time = time.time()
print(f'runtime: {end_time - start_time}')

# import time
start_time = time.time()
print(finder2(1000))
end_time = time.time()
print(f'runtime: {end_time - start_time}')

# import time
start_time = time.time()
print(finder2(10000))
end_time = time.time()
print(f'runtime: {end_time - start_time}')

# import time
start_time = time.time()
print(finder2(100000))
end_time = time.time()
print(f'runtime: {end_time - start_time}')

start_time = time.time()
print(finder2(1000000))
end_time = time.time()
print(f'runtime: {end_time - start_time}')

start_time = time.time()
print(finder2(10000000))
end_time = time.time()
print(f'runtime: {end_time - start_time}')