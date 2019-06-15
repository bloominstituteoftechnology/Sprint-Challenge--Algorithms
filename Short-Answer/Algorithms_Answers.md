Add your answers to the Algorithms exercises here.


A ) the code would never end. the value of n would accelerate away from
"a" linearly i believe. the while loop could be considered n^3 and the inner loop 
its n^2+a which if subtracted reaches O(n) now I also have to consider "a" so maybe the time complexity is O(n + a)?  


B) I think the time complexity of this function is O(n^4) 
a normal double for loop is o(n^2) using this I cam to my conclusion 

for i in range n,   length of n  
        increase i 
        for j in range i + 1, to n    
        <!-- range is still determined by n but could be getting smaller because they increase the value of i by one -->
            add one to j
            for k in range k+ 1, to n      
            <!-- range n is still being approached but this time k times k in being incrase by one for some reason -->
                for l in range k + 1 to k + 10     
                <!-- l is limited by K instead of n, k has a hard limit of k+10 instead of n times              -->
                    increase l by one             
                    <!-- loop runs until until k runs out then incrases sum by one. -->
                    increase sum by 1

 


C) bunnies looks to be a number of bunnies. if no bunnies exist return 0
if not then return double the amount of bunnes inputed 
2 + O(n-1) time complexity?

example 5 bunnies
2 + (input 4) - returns 2 + (input 3) - returns 2 + (input 2) - returns 2 + (input 1) - returns 2 + (input 0 ) - returns 0

2 + 2 + 2 + 2 + 2 = 10 on an input of 5 


Exersise 2

n story building.
eggs have finite height limit to breaking 
F represents the floor it would first break on after the save zone

f-1 floors are safe by this assumption


eggs = 1 = safe
eggs = 0 = not safe

eggs = 1 
testeggs(n = number of floors):
        while eggs > 0: 
            while n > 0:
                throwEggFromFloor(n):  somehow tests if an egg returns 1 or 0
                    if egg < 1:
                        n -= 1   /subtract a floor from n
                    else
                        floorF = n + 1
                        return `Below floor ${floorF} is safe to drops eggs`  


time complexity for the first egg while loop is only o(1) it only has one iteration

time complexity for the second while loop is O(n-1) I think.