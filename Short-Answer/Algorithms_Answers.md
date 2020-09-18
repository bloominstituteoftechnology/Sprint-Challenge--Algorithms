#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Appears to be linear where the input is called only once


b) O(nlog(n)) where each iteration increases runtime


c) This appears to be a linear runtime where input doesnt effect runtime. It's only called once, so no looping through.

## Exercise II


The best approach is probably to do a binary search and start in the middle somewhere. So lets say theres 11 floors.
You can start at floor 6, if it doesnt break you can go to a higher floor, if it does break you go to a lower floor.
You would go to a floor that is in the middle again, like if it doesnt break on 6, you'd go to floor 8 or 9 next. If it
does break on 9 then you just have to determine between if it breaks on 7 and 8, if it doesnt break on 8, then you've found
the highest floor it wont break at. Seems like O(log n)