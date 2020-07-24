#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n). As the number of (n) increases, the number of operations scales linearly. The loop will run as many times as (n) increases.

b) Looks like O(n log n). You could quicksort the problem. Split it into two loops where the first one loops through all of (n) making it O(n). The second loop is different, the operations are increasing but at a slower rate than O(n). That's where I think the log(n) comes into play. O(n) \* O(log n) = O(n log n).

c) O(n). Whatever (n) is, you recurse (n) times. Base case is bunnies == 0, so you'll always have the one base case operation, plus n recursions.

## Exercise II

'''
You're going to use a binary search algorithm. It's a physical building so you know ground floor is 0 and you have a 8 story building. Go to the middle floor, or floor 4 and throw the egg off. If the egg cracks when thrown then you know you're higher than floor f. At that point go to the new middle floor, floor 2. If you throw the egg off and it doesn't crack, you know floor 2 or floor 3 is possibly floor f. To find out whether floor 2 or floor 3 is floor f then you'll need to throw the egg one more time. If it cracks from floor 3 then you know floor 2 is floor f, if it doesn't crack from floor 3 then you can know floor 3 is floor f.
'''

# Start with low_floor = 0

# high_floor is the last number in the list (len(arr))

# mid_floor cuts the list in half (len(arr)) / 2

# start at mid_floor

# check if egg breaks

    # if midpoint breaks egg
      # set new height of building to be bottom half of previous arr
      # keep checking if egg breaks and repeat slicing in half above or below mid_floor

    # if egg does not break from mid_floor
      # set new height of building to be top half of previous arr
      # throw egg from new mid_floor
      # repeat moving from top or bottom half of new building's height until f floor is found.

runtime coomplexity: O(log n)
