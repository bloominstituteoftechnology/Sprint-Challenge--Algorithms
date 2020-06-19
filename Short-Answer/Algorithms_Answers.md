#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The time complexity of this exercise is O(1), means constant time. We know that when we have this time complexity the size of the value n does not depend from the size of the input. In our exercise means no matter how big is the size of the n , only one operation has to be performed for every n number each time.


b) The time complexity for this exercise can be O(log n) logarithmic. For this time complexity we know that as the size of the input increase, then runtime used it will grow a little bit faster step. In our exercise this can be interpolate, like the number of the operations are increasing depending on the sie of n in the for loop. Which means when the n is bigger the range of the loop is bigger and more operations can be performed.


c) The time complexity in our last exercise can be described as O(n) linear time. Means by theory that the running time increases with the size of the input. So in our case the n is bigger so the operation will last longer, if on the other hand the n is small it will run less time.

## Exercise II
First of all, we assume the floors are in order, so in a building with n=20 floors we start from the entrance. To find out which floor is safe we can split up the and find the mid point floor and throw the egg from there. If it brakes then our mid point becomes the end of the building and we eliminate the rest up floors. We performed the same operation, finding the mid point of our new start and end floor. If it breaks again , then our old mid point is the new end, eliminating the upper floors. We start again finding with a new mid point and performing the same operation. In the end we are reaching the safe floor where our egg cant break. This method is called binary search. And our time complexity can be characterized as O(log n).

