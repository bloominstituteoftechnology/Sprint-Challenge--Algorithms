Add your answers to the Algorithms exercises here.
a) Linear
b) Exponental
c) Linear

    def droppedEggs(fl)
        eggState = 1 # "binary code for 'safe' egg state
        if eggState == 0: # base case
            print(f"Your egg has broken on floor: {fl}")
        
        dropEgg()

        print (f"Your egg survived being dropped off of floor: {fl}")
        return droppedEggs(fl-1)

This is a linear function that checks the eggstate at each floor
beginning at the top and working its way down until the safety
point is found.