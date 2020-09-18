#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is a fairly simple O_(n) runtime. The number of iterations scales directly with n.


b) The number of iterations climbs by a reverse factor of n here, making the iteration graph logarithmic. O_(n log n)


c) This will return one iteration for each "bunny ears" (n) passed to it. If bunny ears is n, then I believe this is O_(n)

## Exercise II

Let's assume the egg looks something like:

    class Egg(intact=true, crack_threshold):
        def __init__(self):
            self.intact = intact
            self.crack_threshold = crack_threshold

        def crack(self):
            self.intact = false

        def drop(self, floor):
            if floor >= crack_threshold:
                self.crack()


Now we have an egg we can drop, if it's dropped from the floor of it's crack threshold or higher it will crack.

Now we need to devise a test cycle to test the eggs in our building. Seems like a good place for binary search. We'll go to the center floor of the building and see if the egg cracks. If it does, we're at or above the crack threshold so we should test again halfway between our current floor and the ground floor to see if we can get below and narrow it (search lower); if not then we'll search half way between ourselves and the roof and see if that will break the egg (search up). This allows us to cut off half the unsearched floors with each iteration. (O_(log n) runtime.)

This is psuedo-y but it should get the point across:

def find_threshold(building, carton, min_floor = None, max_floor = None):
    if min_floor is None and max_floor is None:
        min_floor = 0
        max_floor = len(building) - 1
    
    if min floor > max_floor:
        return -1

    if min_floor == max_floor:
        carton[0].drop()
        if carton[0] is intact:
            carton.remove(0)
            return "These eggs don't break fom any floor in this building."
        else:
            carton.remove(0)
            return search_floor
    else: 
        search_floor = (min_floor + max_floor) // 2
        carton[0].drop()

        if carton[0] is intact:
            carton.remove(0)
            return find_threshold(building, carton, search_floor, max_floor)
        elif carton[0] is not intact:
            carton.remove(0)
            return find_threshold(building, carton, min_floor, search_floor)

        
    