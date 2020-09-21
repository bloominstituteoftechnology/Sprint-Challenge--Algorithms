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
    

    def end_of_list(self):
        while self.light_is_on():
            if self.compare_item() == 1:
                self.swap_item()
                self.set_light_off()
            elif self.can_move_left():
                self.move_left()
            else:
                self.set_light_off()
                return self._list
            
        while self.light_is_on() is False:
            if self.can_move_left():
                self.move_left()
            else:
               return self.sort()
            


    def sort(self):
        """
        Sort the robot's list.
        """
        """
        1) Grab first item in list, set light on, move to right
        2) If item in list is greater than what the robot is holding, swap items
        3) Repeat this until you reach end of the list
        4) If robot reaches end, swap item at the end of the list if robot's item is greater than item in list and move to the start of the list
        5) Elif the item isn't greater than the robot's item, move left, repeat step 4. 
        6) If the robot has an item and returns to the start point after reaching the endpoint and compares each number (can_move_left is False), swap the item with position 0 (which should be none)
        7) Turn light off, return list

        """
        self.set_light_on()
        while self.light_is_on():  
            if self.compare_item() == None:
                self.swap_item()
            if self.can_move_right() is False:
                self.end_of_list()
            if self.compare_item() == -1:
                self.swap_item()
                self.move_right()
            else:
                self.move_right()
        
        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    # l = [5, 4, 3, 2, 1]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)