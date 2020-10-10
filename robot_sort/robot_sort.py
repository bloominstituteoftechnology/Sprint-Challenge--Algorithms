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

    def right_traverse(self):
        self.move_right()
        if self.compare_item() == 1:
            self.swap_item()

    def left_traverse(self):
        self.move_left()
        if self.compare_item() == -1:
            self.swap_item()

    def sort(self):
        """
        Sort the robot's list.
        """

        self.set_light_on()
        while self.light_is_on():

        # * check to see if can move right
        # pick up item
        # move right 
        # check if held is bigger than location
        # if bigger than loaction, swap with location
        # move left
        # swap with none
        # move right
        # pick up item...
        # if smaller than location
        # move left
        # swap with none
        # move right
        # pick up item...
        # * when can move right is false, then at end of list

        # Fill this out
        
        # turn light on to start the while loop
        self.set_light_on()
        # using the light to check if a swap was made
        while self.light_is_on():
            # turns off light so that if no swap was made, the sort function ends
            self.set_light_off()
            if self.can_move_right():
                while self.can_move_right():
                    self.swap_item()
                    self.move_right()
                    if self.compare_item() == 1:
                        self.set_light_on()
                        self.swap_item()
                        self.move_left()
                        self.swap_item()
                        self.move_right()
                    elif self.compare_item() == -1 or 0:
                        self.move_left()
                        self.swap_item()
                        self.move_right()
            if self.can_move_left():
                while self.can_move_left():
                    self.move_left()

                # while self.can_move_left():
                #     self.move_left()
                #     if self.compare_item() == 1:
                #         self.set_light_on()
                #         self.swap_item()
                #         self.move_right()
                #         self.swap_item()
                #         self.move_left()
                #     elif self.compare_item == -1:
                #         self.move_right()
                #         self.swap_item()
                #         self.move_left()
        
        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    k = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60]
    l = [15, 41, 58, 49, 26, 4, 28, 8, -15, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    lVar = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, 18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

    
    # while light is on
        # turn light off 
        # if cannot move right and compare == none
            # turn light off (list is sorted)
        

        # def right_traverse(self):
            # self.move_right()
            # if self.compare_item() == 1:
                # self.swap_item()
        
        # def left_traverse(self):
            # self.move_left()
            # if self.compare_item() == -1:
                # self.swap_item()

    # light on indicates moving right
    # light off indicates moving left
    # if can move right and light off
        # turn light on
        # traverse right
    # if cannot move right and compare == none:
        # break (everything is sorted)
    # if cannot move right and light on:


    # start with swap first item, then start traverse_right
