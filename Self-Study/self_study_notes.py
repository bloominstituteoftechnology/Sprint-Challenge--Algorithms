# a
a_list = []
n = 20
a = 0
while a < n * n * n:  # O(n^3) (if incremented by 1)
	a = a + n * n  # O(1) (a incremented by n^2)
	a_list.append(a)
# O(n^3) / O(n^2) * O(1) = O(n * 1) = O(n)
print("A", len(a_list))

# b
sum_int = 0
i = 0
while i < n:  # O(n)
	j = i + 1  # O(1)
	while j < n:  # O(n - 1)
		k = j + 1  # O(1)
		while k < n:  # O(n - 2)
			l = k + 1  # O(1)
			while l < 10 + k:  # O(9)
				sum_int += 1  # O(1)
				l += 1  # O(1)
			k += 1  #(O1)
		j += 1  # O(1)
	i += 1  # O(1)
# O(n) * O(n) * O(n) * O(9) = O(9n^3) = O(n^3)
print("B", sum_int)


# c
c_list = []
def bunny_ears(bunnies):
	if bunnies == 0:
		return 0
	c_list.append(bunnies)
	return 2 + bunny_ears(bunnies - 1)  # O(n)

bunny_ears(n)
print("C", len(c_list))