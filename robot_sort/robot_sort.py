class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out



#   Bubble Sort 
#   This works but I didn't use any of the defs to get my answer
       
        # nums = self._list
        # for i in range(len(nums)):
        #     # print("Current List:  ",nums)
        #     swapped = False
        #     i = 0

        #     while i < len(nums) - 1:                   # compare adjacent elements 
        #         if nums[i] > nums[i+1]:                   # when the 1st number is greater than the 2nd
        #             nums[i], nums[i+1] = nums[i+1], nums[i]     # swap numbers
        #             # print("Swapped values: ", nums[i], nums[i+1])
        #             swapped = True                  # swapped tracker
        #         i = i+1                             # move to the next indexed numbers
        #         # print( i)
            
        #     if swapped == False:                    # no more numbers to swap; at the last index
        #         break
        # return
#########################################################################################

# Final Attempt:  WORKING ! ! !
#  
        print("Starting position:  ",self._position)
        print("List at Start: ", self._list)
        print("Item held: ", self._item)
        print("Robot Starting: Light is ON")
  
        self.set_light_on()                     # turn light on to show that there is still swapping to be done
        
        
        while self.light_is_on() == True:       # Resets light to off when done
            self.set_light_off()
        
            while self.can_move_right():        # If you can move right:
                self.swap_item()                # swap items 
                self.move_right()               # move right
               
                if self.compare_item() == 1:    # if the item you are holdng is higher than the item in front
                    self.swap_item()            # swap items to place the higher item
                    self.set_light_on()         # light is on to show that there is more swapping to do
                            
                self.move_left()                # otherwise, move left
                self.swap_item()                # swap items to place the lower item
                self.move_right()               # move right
               
                # print("Position':  ",self._position)
                # print("Item held: ", self._item)
            
            while self.can_move_left():         # If you can move left:
                self.swap_item()                # swap items 
                self.move_left()                # move left

                if self.compare_item() == -1:   # if the item you are holding is lower than the item in front
                    self.swap_item()            # swap items to place lower item
                    self.set_light_on()         # light is on to show that there is more swapping to do

                self.move_right()               # otherwise, move right
                self.swap_item()                # swap items to place the higher item
                self.move_left()                # move left

                # print("Position':  ",self._position)
                # print("Item held: ", self._item)
        print("Ending position':  ",self._position)
        print("Item held: ", self._item)
        print("Robot Done: Light is OFF")
               


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [5,3,1,4,2]
    #l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)
    # print("Sorting Robot: ", SortingRobot(l))

    robot.sort()
    print("Sorted List:")
    print(robot._list)

    
################################################################
"""
Plan #1:
    * Start with robot light on and current_position at 0
    * Work left to right
    * Examine each item and compare it to items on its left
    * Insert the item in the correct position in the list
    * Turn light off when list is sorted


Plan #2:
    * Merge Sort in Place - This didn't work out so well for me !

Plan #3: 
    *Bubble Sort - would be easiest to implement but very efficient for larger lists
    * Was able to do this, but need to implement this logic into correct format
    """

