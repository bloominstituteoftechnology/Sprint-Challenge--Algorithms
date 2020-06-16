## Robot pseudo code requirements

You have been given a robot with very basic capabilities:

  * It can move left or right.
  * It can pick up an item
    * If it tries to pick up an item while already holding one, it will swap the items instead.
  * It can compare the item it's holding to the item in front of it.
  * It can switch a light on its head on or off.

Your task is to program this robot to sort lists using ONLY these abilities.

##### Rules

Inside the `robot_sort` directory you'll find the `robot_sort.py` file. Open it up and read through each of the robot's abilities. Once you've understood those, start filling out the `sort()` method following these rules:

  * You may use any pre-defined robot methods.
  * You may NOT modify any pre-defined robot methods.
  * You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
  * You may use comparison operators. (`>`, `>=`, `<`, `<=`, `==`, `is`, etc.)
  * You may use iterators. (`while`, `for`, `break`, `continue`)
  * You may NOT store any variables. (`=`)
  * You may NOT access any instance variables directly. (`self._anything`)
  * You may NOT use any Python libraries or class methods. (`sorted()`, etc.)
  * You may define robot helper methods, as long as they follow all the rules.


****IMPORTANT ROBOT INFO****
 Compare the held item with the item in front of the robot:
    If the held item's value is greater, return 1. if the item equals 1 
    If the held item's value is less, return -1. if the item equals -1
    If the held item's value is equal, return 0. if the item equals 0 
    If either item is None, return None. if the item is None 


****NEED TO PRINT EVERYTHING****

Initial Thoughts are to set it up like a Bubble Sort because there the robots light needs to be on to move(?)

****POSSIBLE STEPS/THOUGHT PROCESS****
Like Bubble sort setting condition to run while true or false 
That would involve using while loop
Could set the robots light to off to start(false)
Then turn the light on to start the sorting I guess
Can use multiple while loops and some if statements to keep it going until conditions are met 
Need to have a loop for when the robot can move to to the right because that gives True fo False
If the robot can move to the right (which is forward I guess) then it would have to need to be able swap the numbers and keep moving
BUT compare method says if the robot the number is holding is greater than the number in front, it should equal 1 
So that would mean the robot is trying to move forward so swap and then turn light off because the robot is done(?)
May need additional movement after light is turned off 

Repeat for moving backward...