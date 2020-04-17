#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n)


b) nlogn


c) O(n)

## Exercise II



def eggFloor():
  starting_floor = n // 2
  egg_status = test_egg(starting_floor)

  if egg_status == True:
    up_floor = starting_floor
    while egg_status != False:
      up_floor += 1
      egg_status = test_egg(up_floor)

 if egg_status != True:
    down_floor = starting_floor
    while egg_status != True:
      up_floor -= 1
      egg_status = test_egg(down_floor)


O(n)