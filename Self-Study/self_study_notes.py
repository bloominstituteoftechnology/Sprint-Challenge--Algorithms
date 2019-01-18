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
b_list = []
sum_int = 0
i = 0
while i < n:  # O(n)
	b_list.append(i)
	j = i + 1  # O(1)
	while j < n:  # O(n - 1)
		b_list.append(j)
		k = j + 1  # O(1)
		while k < n:  # O(n - 2)
			b_list.append(k)
			l = k + 1  # O(1)
			while l < 10 + k:  # O(n)
				b_list.append(l)
				sum_int += 1  # O(1)
				l += 1  # O(1)
			k += 1  #(O1)
		j += 1  # O(1)
	i += 1  # O(1)
# O(n) * O(n) * O(n) * O(n) = O(n^4)
print("B", len(b_list))


# prac O(n^4)
prac_list = []
for i in range(n):
	prac_list.append(i)
	for j in range(n):
		prac_list.append(j)
		for k in range(n):
			prac_list.append(k)
			for l in range(n):
				prac_list.append(l)
print("PRAC", len(prac_list))

# c
c_list = []
def bunny_ears(bunnies):
	if bunnies == 0:
		return 0
	c_list.append(bunnies)
	return 2 + bunny_ears(bunnies - 1)  # O(n)

bunny_ears(n)
print("C", len(c_list))