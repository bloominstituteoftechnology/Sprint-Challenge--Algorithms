Add your answers to the Algorithms exercises here.

I) 

a)  n^3 = a + n^2 
    n^3 = n^2 
    n^3 / n^2 = n = O(n)

b)  n * n * n * const = n^3 = O(n^3)

c)  n = O(n)

II) 

Take the number of stories _n_ and divid those floors by two and move to that floor. Drop the egg from that floor and if it breaks then you have determined that the floor you're looking for is below the current floor you're on, if it does not break then the floor you're looking for is above you. Continue this process of dividing the floors known to contain the floor you're looking for by 2, move to that floor, drop the egg and if the egg breaks the floor you're looking for is below or if it does not break then the floor maybe above.
 
