Add your answers to the Algorithms exercises here.

# Exercicse I

a) 	O(n)

b) O(n^3)

c) O(n)

* notes in `self_study_notes.py`

# Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped eggs is minimized.

building_stories = n

def find_floor(n):
	first = 1
	last = n
	found = False
	while first <= last and not found:  # repeat until found and/or first is larger/equal to last
		midpoint = (first + last) // 2
		if egg break at midpoint and egg !break at (midpoint - 1):  # found f
			found = True
			return midpoint
		else:
			if egg break at midpoint:
				last = midpoint - 1  # check lower floors
			else:
				first = midpoint + 1  # check higher floors
	return None

Since this is using a binary search approach, the time complexity would be O(log n).
(The number of floors will be divided in half each time the correct floor is not found)