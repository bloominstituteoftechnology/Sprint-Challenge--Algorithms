#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

b) O(n log n)

c) O(n)

## Exercise II

Use a binary search algorithm, log n
Keep a counter to see how many times you've moved up or down.

Move n/(2^counter) floors (math.floor value) up or down of your current position, indicated by the egg breaking. Breaks, move down. Doesn't break move up.<br>

Suppose the egg would break at floor 65 on a hundred-story building

n = 100<br>
floor = 0<br>
counter = 1

go up n/(2^counter) = 50
counter = 1<br>
position = n/(2^1) = floor 50 < 65<br>
no break

go up 25: <br>
counter = 2 <br>
position = position + n/(2^2) = floor 75 > 65<br>
break

go down 12: <br>counter = 3 <br>
position = position - n/(2^3) = floor 63 < 65 <br>
no break

go up 6: <br>
counter = 4 <br>
position = postion + n/(2^4) = floor 69 > 65<br>
break

go down 3: <br>
counter = 5 <br>
position = position - n/(2^5) = floor 66 > 65
break

go down 1: <br>
counter = 6 <br>
position = position - n/(2^6) = floor 65 = 65<br>
break

go down 0
counter = 7 <br>
position = position - n/(2^7) = **floor 65**
