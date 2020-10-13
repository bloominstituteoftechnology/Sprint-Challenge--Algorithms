#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This looks like a 0_(n) runtime. The ammount of itterations cales with n


b) The number of iterations climbs by a reverse factor of n. The iteration is a graph logarithmic.
0_(log n)


c) This will return one iteration of "bunny ears"(n) passed to it. If "bunny ears" us n, then this is 0_(n)

## Exercise II
Eggs:

    class Humpty_Dumpty(intact=true, crack_threshold):
        def __init(self):
            self.intact = intact
            self.crack_threshold = crack_threshold

        def crack(self):
            self.intact = False

        def falls(self, floor):
            if floor >= crack_threshold:
                self.crack()

Now we have Humpty_Dumpty class that reprents an egg. 
If humpty dumpty falls from the floot of its crack threshold or higher he will crack

Now to devise a test cycle to test humpty dumpty at our building 
we will go to the center floor of the bulding and see if humpty dumpty cracks. If he does were either at or above the crack
threshold. We should test agaun halfway between our current floor and the ground fllor to see if we can get below and narrow
it  (search lower); if not then we'll search half way between ourselves and the roof to see if humpty dumpty will break. 
this allows us to cut off half the unsearched floors with each iteration (0_(log n) runtime)

This is psuedo--y but it should get to the point:

def find_threshold(building, carton, min = None, max = None):
    if min is None and max is None:
        min = 0
        max = len(building) - 1

    if min > max:
        return -1

    if min == max:
        carton[0].falls()
        if carton[0] is intact:
            carton.remove(0)
            return "Humpty dumpty wont break from the floor"
        else:
            carton.remove(0)
            return search_floor

    else:
        search_floor = (min + max) // 2
        carton[0].falls()

        if carton[0] is intact:
            carton.remove(0)
            return find_threshold(building, carton,search_floor max)
        elif carton[0] is not intact:
            carton.remove(0)
            return find_threshold(building, carton, min, search_floor)



