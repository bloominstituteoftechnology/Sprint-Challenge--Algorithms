Add your answers to the Algorithms exercises here.

## Exercise I
a) The Big O notation for this problem would be O(n) because although it cube whatever n will be it still pass through and run one check per loop.

But I'm also considering this problem would be O(n^3) because everytime it iterate through n is being calculating through until it reaches cube value but I also consider it to be constant because `a` is set at a constant value.

b) This would be classified as On^4 because it is nested loop 4 time, so the deepest nested loop condition will increment first then 3rd loop, 2nd loop and finally parent for loop will count 1. So it will exponentially increase by 4.

c) This function call n-1 every recursion, we subtract 1 from n before it calls itself, but still would be considered O(n) because n isn't set as exponential value or log.

## Exercise II

###### Notes
_so_

if(you write your condition in here){
    //if it is true, it'll run in here
}

greaterThanFive = false;

greaterThanFive = 0;

console.log(greaterThanFive)