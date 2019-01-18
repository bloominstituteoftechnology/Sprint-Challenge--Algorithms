Add your answers to the Algorithms exercises here.

# Exercise 1

a) O(n) -- The runtime is O(n) because are n stays the same while our variable a will go up at a linear pace. For example, if n is ten, then a will go up 100 each time until it hits 1000. That data is 100,200,300... which would give a linear curve.

<!-- b)O(n^4) -- The runtime is O(n^4) because we have 4 loops that go to n. Even though the last one has a constant, it is adding k to it which is going to n. Therefore we get the O(n^4). -->

b) The actual answer is O(n^3). I should have written some numbers out to see if the last for loop was any different when it increased the k, which it does not, it will always be 9. So there is 4 loops but 3 are O(n) and one is O(1), so we have a O(n^3)

c)O(n) -- This recursive funtion is O(n) because it is like a for loop. And for loops are usually O(n).

# Exercise II

We would want to do this like a Binary search. We would go to the middle of the building and throw the egg. If it breaks, go halfway down from the middle and do it again. If it doesn't break, we go up halfway and throw an egg again. We keep going up or down depending on the new middle of the leftover floors until we get to the floor f where it will not break if the egg is dropped less than that floor and where it will break if higher than that floor. This would be a O(log n) because we are halfing it everytime we go to throw another egg.
