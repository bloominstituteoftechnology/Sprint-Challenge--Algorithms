import time

def test(n):
    a = 0
    t0 = time.time()
    while (a < n):
        print(a)
        a = a + 1
    t1 = time.time()
    total = t1-t0
    print(total)

test(10000)

def test2(n):
    t0 = time.time()
    sum = 0
    for i in range(n):
        i += 1
        for j in range(i + 1, n):
            j += 1
            for k in range(j + 1, n):
                k += 1
                for l in range(k + 1, 10 + k):
                    l += 1
                    sum += 1
    t1 = time.time()
    total = t1-t0
    print(total)

# test2(1000)

def test3(n):

    def bunnyEars(bunnies):
        
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1)

    t0 = time.time()
    print(bunnyEars(n))
    t1 = time.time()
    total = t1-t0
    print(total)
    
test3(990)