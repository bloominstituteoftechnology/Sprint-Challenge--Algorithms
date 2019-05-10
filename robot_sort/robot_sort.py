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
        # set the light on to get into the first loop
        self.set_light_on()
        self.swap_item()

        # this will loop until the robot has traversed
        # the array and has not turned its light on,
        # meaning that it hasn't found any items that
        # are out of order and, thus, the array is sorted
        while self.light_is_on():
            self.set_light_off()
            
            # pick up the first item in the list
            if self.compare_item() == None:
                self.move_right()
                if self.compare_item() == None:
                    self.move_left()
                    self.swap_item()
                elif self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.set_light_on()
                elif self.compare_item() == -1:
                    self.move_left
                    self.swap_item()
                    self.set_light_on()
                else:
                    self.move_left()
                    

            # move left until the robot can't move left anymore
            # compare the item the robot is holding
            # if the item in the list is greater than the item the
            # robot is holding, swap the items and turn the robot's light
            # into the on position
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == None:
                    self.move_right()
                    if self.compare_item() == None:
                        self.move_left()
                        self.swap_item()
                    else:
                        self.move_left()
                        self.swap_item()
                        self.set_light_on()
                elif self.compare_item() == 0:
                    self.swap_item()
                elif self.compare_item() == -1:
                    if self.can_move_left:
                        self.move_left()
                        if self.compare_item() == None:
                            self.swap_item()
                            self.move_right()
                        else:
                            self.move_right()
                            self.swap_item()
                            if not self.light_is_on():
                                self.set_light_on()
                else:
                    continue
                    
            # when the robot cannot move right anymore, it
            # is at the end of the list
            # on the first pass it will hold the largest value of 
            # the list at the last position
            # so it will need to do one last swap with the value 
            # currently in the last position
            # on subsequent passes the largest value will always be
            # in the last position so the code below will always fail
            if self.compare_item() == 1:
                self.swap_item()
                self.move_left()
            elif self.swap_item() == None:
                self.swap_item()
                self.move_left()
            
            # now the robot has to traverse back to the first position
            # it will also have to "drop" the item that it is currently
            # holding in the first empty position it finds.
            # move left until the robot can't move left anymore
            # the first empty spot the robot sees, drop the 
            # item it was holding.
            
            while self.can_move_left():
                if self.compare_item() == None:
                    if self.can_move_right():
                        self.move_right()
                        if self.compare_item() == None:
                            self.move_left()
                        else:
                            self.move_left()
                            self.swap_item()
                elif self.compare_item() == 1:
                    self.move_right()
                    if self.compare_item() == None:
                        self.swap_item()
                        self.move_left()
                        if self.can_move_left():
                            self.move_left()
                        
                    else:
                        self.move_left()
                        self.swap_item()
                        self.set_light_on()
                self.move_left()
            if not self.can_move_left():
                if self.compare_item() == None:
                    self.move_right()
                    if self.compare_item() == None:
                        self.move_left()
                        if self.light_is_on():
                            self.swap_item()
                    else:
                        self.move_left()
                        self.swap_item()
                else:
                    self.swap_item()

            # finally, if the robot has reached the beginning of the 
            # list, then swap
        return self._list
        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    #l = [3,5,5,4,5]
    #l = [5,4,3,2,1]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)