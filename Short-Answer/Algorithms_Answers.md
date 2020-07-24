#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): The function is dependent upon input value n.


b)O(nlogn): outer loop(the for loop) is n, inner loop(the while loop) is log(n)


c)O(n): The function depends upon input value n(bunnies)

## Exercise II

The stratqegy I would choose depends on my priority.

If I wanna achive my goal by breaking minimum amount of eggs, I would do a linear search, I would start from the first floor, and keep moving up one floor until the egg breaks. In this way I would have to break only one egg to find the floor f. The runtime complexity would be O(n)

If I wanna achive my goal by dropping minimum amount of eggs, I would do a binery search. I would start at the middle floor, if the egg breaks I would go to the middle floor between current floor and bottom floor and so on. If the egg didn't break, I would go to the middle floor between current floor and top floor and so on. The runtime complexity would be O(logn)

If I consider both dropping and/or breaking as loss, I would use the binery search method, even if it breaks more eggs, it would require way less dropping.
