class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l   # The list the robot is tasked with sorting
        self._item = None   # The item the robot is holding
        self._position = 0    # The list position the robot is at
        self._light = "OFF"    # The state of the robot's light
        self._time = 0   # A time counter (stretch)

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
        while self.light_is_on is False:
            print("while 1 light on?", self.light_is_on())

            while self.can_move_right():
                print(f"while 2", self.can_move_right())
                self.swap_item() # swap the None for a num
                self.move_right()

                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()

                    self.

                
                if self.compare_item() == -1:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    # self.swap_item()

                if self.compare_item() == 0:
                    self.move_left()
                    self.swap_item()
                    self.move_right()


# starting position index 0/15, holding None, light is OFF

# as long as its OFF:

#     start iterating through my list:
#         swap with first item in list - NONE is in index 0, I hold 15
#         compare 15 to value to the right, which is 41 at index 1
#         15 is less than 41, so I go back to index 0, drop the 15, pick up None,
#             move to the right (to index 1 again), drop the None and pick up the 41.

#         compare 41 to value on right, which is 49 at index 2
#         41 is less than 49, so I go back to index 1, drop the 41, pick up None, move right to index 2, drop the None and pick up the 49

#         now im holding 49

#         compare 49 to value on the right, which is 58 at index 3
#         49 is less than 58, so I go back to index 2, drop the 49, pickup the None, move right to index 3, drop the None and pick up the 58

#         now Im holding the 58.

#         compare the 58 to value on the right, which is 26 at index 4.
#         58 is greater than 26. I move left to index 3, drop 58 and pick up None at index 3. Move right, drop None at index 4, pickup 26. Move left, drop the 28 at the index 3, pick up 58. Move right, drop the 58 and pickup None.

#         now I'm holding None.

# while light_is_on is False: #light off
#     while can_move_right:
#         swap None with item at current position/index
#         move_right

#         if item I hold > item at position:
#             move_left to previous position
#             swap (drop the highnum and pickup None)
#             move_right
#             swap ( drop the None and pickup lownum)
#             move_left
#             swap (drop the lownum, pickup the highnum)
#             move_right (to position+1, None)
#             swap (drop the 58, pickup the None)

#         if item I hold < item at position:
#             move_left to previous position
#             swap (drop the lownum and pickup None)
#             move_right
#             swap (drop the None, pickup the highnum)

#         if item I hold == item at position:
#             move_left
#             swap (drop the num and pickup None)
#             move_right


        # self.set_light_off()
        # while not self.light_is_on():
            
        #     self.set_light_on()
        #     print("move left:", self.can_move_left())

        #     while self.can_move_right(): # will stop at end of list
        #         # print(f"if can move right position:", self._position)
        #         print(self._item)
        #         self.swap_item() # pick up an item
        #         print(self._item)
        #         self.move_right()

        #         if self.compare_item() == 1: #first num is 15, 15 not greater
        #             print("in 1")
        #             self.swap_item() # pick up item/holding item
        #             print(self._item)
        #             self.move_left() #move to next item
        #             self.swap_item()
        #             print(self._item)
        #             # move left and put it down item and pick up item at index
        #             self.move_right()
        #             self.swap_item()
        #             print(self._item)

        #             self.set_light_off() # set false to go again
        #             # print(f"1 light:", self.light_is_on())
        #             # print(f"position greater than:", self._position)
                
        #         if self.compare_item() == -1: # if item to right is less than
        #             # self.swap_item()
        #             # print("in -1")
        #             self.move_left() # move to left(since it less than right)
        #             self.swap_item() # swap with left
        #             # print(self._item)
        #             self.move_right() # move back right

        #             # self.set_light_off()    # flip light false again

        #             # print(f"-1 light:", self.light_is_on())
        #             # print(f"position less than:", self._position)

        #         if self.compare_item() == 0: # if same num
        #             # print("in 0")
        #             self.move_left() # move back to place
        #             self.swap_item()    # swap
        #             self.move_right()    # move back left position

        #             self.set_light_off()
        #             # print(f"0 light:", self.light_is_on())
        #             # print(f"position same value", self._position)

        #         else:
        #             self.set_light_off()
   
                # if self.compare_item() == None:
                #     print("in None")
                #     self.move_right()
                #     self.swap_item()
                #     self.set_light_off()
                #     print(f"0 light:", self.light_is_on())
                #     print(f"position same value", self._position)
            
                
            

# sorting robot sort functions are similar to bubblesort
# robot starts with:
#   a list(l) to sort / the list is NOT Sorted
#   not holding an item
#   index 0 at the beginning of the list
#   its light is off

# setlighton = turns to true
# set light off = turns to false
# light is on = returns status True (on) or False (off)
# can_move_right = return True if can move right or False if at end of list
# move_right = if can move right, move right and return True
# swap_item = swap index
# compare_item = compare index with item, returns 1 if greater

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 6]

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


