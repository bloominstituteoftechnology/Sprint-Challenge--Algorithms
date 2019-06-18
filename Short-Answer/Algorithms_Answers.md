Add your answers to the Algorithms exercises here.

a) O(n^3)
    line 1 and 3 have times of O(1), since these are minor times, the heavier complexity takes precidence.
    Line 2 is a loop that runs from 0 to (n * n * n).  If n = 2, this would be 8 - if n = 3, this would be 27 times.
    The full running time would be O((n^3)+2), but the +2 makes such a small impact it can be dropped off.


b)  O(3n)
    Each loop reduces the value of 'n', but in the end they are still 'n'. The other O(6) can be dropped off.


c)  O(∞)
    This recursive function will never reach 0 (the break point) because it actually adds 1 to the value of n.


Excercise II:

n-story building and plenty of eggs
egg gets broken if dropped off floor f or higher, does not break if floor < f

pseudo-ish code:

def throw_eggs(stories, low=0, tests=0):
    high = stories                                    
    breakpoint = x                                    

    if stories/2 == breakpoint:                       
        # breaking point is halfway up
        return tests + 1                              
    elif stories/2 > breakpoint:                      
        throw_eggs(stories, stories/2, tests + 1)
    else:
        throw_eggs(stories/2, low, tests +1 )

Recursively checking half the floors at a time would make it O(log(n)), since n is reduced in half for each call
