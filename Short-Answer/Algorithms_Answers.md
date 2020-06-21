#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a). 0(1)- no matter how big `n` gets the number of operations will now change.



b) 0(n) for loop is traversing through `n`. if `n` is less than one then nothing happen. but if `n` is greater than one the number of operation will increase as lonng as `j` is lesser than `n`.

 `j` will increase by 2

c) Exponetial 0(c^2) - the bunny function is recursive. So the input bunnies is slightly increase. The time will move as a much faster rate.

## Exercise II

def floor_game(f):
  egg_count = 10

  for i in range(f + 1):
    if i < 6: 
      egg_count -= 1
      print('Egg didnt break', i)
    
    else:
      if i > 5:
        egg_count -= 1
        print('Egg did break', i)

The time complexity is 0(n) because `i` will change the input of `f` by 1. Then if `f` is < floor 6 one egg will drop off each floor and not break.

else is `f` > floor 5 one egg will drop and the egg will be break. So the `For loop in range()` line changes the value of `f` by adding floors.

