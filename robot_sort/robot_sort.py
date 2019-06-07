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
        while self.move_left():
            pass
        self.set_light_on()
        while self.light_is_on():
            # print('while self.light')
            self.set_light_off()
            while self.move_left():
                pass
     
            while True:
                self.swap_item()  # 0 is None, _item = @0                   
                if self.move_right() == False:
                    # print('inner loop can\'t more right', self._position, len(self._list), self._list[self._position], self._list, self._item)
                    self.swap_item() 
                    break

                # print('comparing',self._item, self._list[self._position])
                if self.compare_item() == 1:
                    self.move_left()
                    self.swap_item()
                    # print('greater None item?', self._item)
                    self.swap_item() # 0 to None, item to @0
                    self.move_right()
                    # print('before swap',self._position, self._list[self._position], self._item)
                    self.swap_item() # @1 gets @0, _item = @1
                    self.move_left() # back to 0
                    self.swap_item() # @0 gets @1, item is None
                    # print('after swap',self._position, self._list[self._position], self._item)                    
                    self.set_light_on()
                    if self.can_move_right():
                        self.move_right()
                    else:
                        break
                else:
                    self.move_left()
                    self.swap_item()
                    # print('not greater None item?', self._item)
                    self.move_right()                    
                    # print('nums + 1 not greater',self._position, self._list[self._position], self._item)
                    if self.can_move_right() == False:
                        # print('breaking for can\'t more right', self._position )
                        break
        # while self.move_right():
        #     pass
        # print('before end swap', self._position, self._list[self._position], self._item)
        if self._item is not None:
            self.swap_item()
        # else:
        #     print('skip end swap, null item')
        # print('after end swap', self._position, self._list[self._position], self._item)
        # if self._item is None:
        #     print('correct last setitem')
        # else:
        #     print('wrong last setitem',self._position, self._item)
        # print('last position', self._position, self._list[self._position], self._item)






        # self.move_right()
        # self.swap_item()  # second from left now is None; _item == second from left
        # print(self._list[1], self._item)
        # while self.move_right():
        #     if self.compare_item() == -1:
        #         print('moving right',self._position, self._list[self._position], self._item)
        #         # self.move_right()
        #         print(self._position)
        #         self.swap_item()
        #         print('moving right after swap',self._position, self._list[self._position], self._item)
        #     else:
        #         self.move_left()
        #         print('backing up before swap',self._position, self._list[self._position], self._item)
        #         self.swap_item()  # 3 from left = 2 from left; item = 3 from left
        #         print('backing up', self._position, self._list[self._position],self._list[self._position+1], self._item)
        #         # self.move_left()
        #         self.swap_item()  # 2 from left = 3 from left; _item == None 

        # while(self.move_left())
        # self.swap_item() # first left has None; _iten == first_left

        # self.move_right()
        # self.swap_item()  # 1st right has None _item == 1st right
        # if self.compare_item() == 1:
        #     self.swap_item() # previous 1st right is in < postion; _item == < item

        # while(self.move_left())
        # self.move_right()
        # self.swap_item()  # pivot - low   1st right == < item; _item == None
        # self.move_left() # on pivot
        # self.swap_item()  # pivot position == None; _item == pivot
        # self.move_right() # on 1st right
        # self.swap_item()  # pivot goes to 1st right
        # self.move_left()
        # self.swap_item() # < item goes to first left _item == None
        # while(self.move_left()):
        #     pass
        # self.swap_item() # last left position is None; _item = last left

        # while self.move_right():
        #     if self.compare_item() == -1:
        #         self.swap_item()
        #         if self.move_right == False:
        #             self.swap_item() # put the largest back
        #         while(self.move_left()) # suppress the next swap
        # if self.move_left():
        #     self.move_right()
        #     self.swap_item() # last right has largest; _item == previous last right
        # while(self.move_left()):






if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
        45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    # l = [41,15, 58, 49, 4, 28, 8, 61, 60, 21]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
