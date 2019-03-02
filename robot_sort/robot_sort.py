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

    #  l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 6, 58]
    def sort(self):
        """
        Sort the robot's list.
        """

        print(f"before while", self.light_is_on()) # False
        print(f"holding", self._item)
        # remember robot light starts off
        while self.light_is_on() is False:  # as long as light is off
            print("while 1 light on?", self.light_is_on())
            self.set_light_on() # flip light on, then
            
            while self.can_move_right(): # while can move right, do these executions
                print(f"while 2", self.can_move_right())
                self.swap_item()
                self.move_right()
                print(f"is light on?", self.light_is_on())

                if self.compare_item() == 1: # if robot number greater, do this
                    print(f"if > holding: ", self._item)
                    self.swap_item()
                    print(f"if > swap 1: ", self._item)
                    self.move_left()
                    self.swap_item()
                    print(f"if > swap 2: ", self._item)
                    self.move_right()

                    self.set_light_off() # flip the light off
                    # light will stay off as long as in while2
                    # in its final pass, there should NOT be any greater than numbers on the left.
                    # we continue iterating through while2, the while2 else and back to the while1, where the light flips on.
                    # because there are no longer any nums greater than on the left, the light is not flipped off.
                    # it makes its way to while2/if, doesn't execute because light is on == True
                    # goes to while1, doesn't execute because lightison == True, not False, which ends while1
            
                if self.compare_item() == -1 or 0: # if robot number less than, do this 
                    print(f"if < holding: ", self._item)
                    self.move_left()
                    self.swap_item()
                    print(f"if < swap: ", self._item)
                    self.move_right()

                if self.compare_item() == 0: # if robot number the same, do this
                    print(f"if same holding: ", self._item)
                    self.move_left()
                    self.swap_item()
                    print(f"if same swap: ", self._item)
                    self.move_right()
            
            # moves robot back back to the beginning of array
            # the if loop checks if the light is off, if it is then
            # while there is space to move left
            # move left.
            # 
            # this if statement works with the inner while loop (while2).
            # while2 is checking cmr. As long as cmr, do this (the swaps, the inner ifs)
            # this IF is while2's else. When this else executes, the inner while stops, moves to while1
            # is the lightoff? then start while1 again.
            if self.light_is_on() is False: # if the light is off/set to false
                while self.can_move_left(): #as long as there is space to move left, then:
                    self.move_left() # move_left / position-1
            
                



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 6, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


