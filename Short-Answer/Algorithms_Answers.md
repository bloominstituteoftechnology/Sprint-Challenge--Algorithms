Add your answers to the Algorithms exercises here.

a)
	  
1) 0(1)
2) 0(n)
3) 0(1)

1 + n * 1 = 1 + n

0(n)

As the number n grows the number of times the while loop runs occurs on a 1:1 ratio.

For instance: if n = 0 the while loop never runs, if n is 1 the while loop runs once, n = 2 the loop runs twice ect ect

b)
		
1) 0(1)
2) 0(n)
3) 0(1)
4) 0(n)
5) 0(1)
6) 0(n)
7) 0(1)
8) 0(10)
9) 0(1)
10) 0(1)

1 + n(1 + n (1 + n (1 + 10(1 + 1)))) =
1 + n(1 + n (1 + n (1 + 10(2)))) =
1 + n(1 + n (1 + n (1 + 20))) =
1 + n(1 + n (1 + n (21))) =
1 + n(1 + n (1 + 21n))=
1 + n(1 + n (22n))=
1 + n(1 + 22n^2) =
1 + n(23n^2) =
1 + 23n^3 =
n^3

0(n^3)

I guess I did this wrong idk, but I know it's somewhere in the horrible section because it has so many nested loops.  When you test this with various vaules it looks like O(n^2), but I have no idea how to get to that answer using the steps we went over with chris.  I'm pretty sure it's me because I suck at math in general.

c)
	  
1) 
2) 0(1)
3) 0(1)
4) 0(n-1)

(1 * 1) + n-1

0(n)



Exercise II:

Clearly my runtime complexity whatever skills are non-existent outside of the classroom (fun times).  However, understanding and explaining a problem is simple enough.  To minmize the number of eggs broken we would need to create an algorithm that breaks the building into smaller pieces until the "breaking point" is found.

For instance if we had 10 floors we could drop the egg from floor 5 to see if it breaks. If the egg does break, we know the stopping point for the highest floor is between 1 and 4. Therefore, we can retest the drop at floor 2 noting is the egg breaks. If it does we know the first floor is the only level an egg can be safely dropped from.  If not we now know the "safe zone" is somewhere between 3 and 4. If we use a math method like floor or ceiling we can round up or down to avoid partial building division. Much like before we could test the floor height to determine if the egg breaks or not.

I believe the time complexity would be something like O(n log(n)) since most of the sorts seem to fall into that category