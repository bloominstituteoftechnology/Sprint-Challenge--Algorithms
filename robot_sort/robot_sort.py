class SortingRobot:
    def __init__(self, lis):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = lis        # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)
        self._direction = True  # The direction of the robot

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
    
    def check_direction(self):
        """
        Returns the direction of the robot
        """
        return self._direction

    def toggle_direction(self):
        """
        Toggles direction between true and false
        """
        self._direction = not self._direction

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
        # Grab first item and initialize light to on
        self.swap_item()
        self.set_light_on()
        # Traverse until no swaps are made
        while self.light_is_on():
            # Turn light off, only toggle on if swap is made
            self.set_light_off()
            self.traverse()
            # Swap directions after traversing the list
            self.toggle_direction()
        # Do the final swap between held and None
        self.swap_item()

    def traverse(self):
        # Moves a direction until it can't, turns on light if a swap is made
        if self.check_direction():
            # Move right, swapping when possible
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == -1:
                    self.swap_item()
                    # If a swap is made, turn on the light
                    self.set_light_on()
            # Once we reach right end we're holding largest item, swap
            if self.compare_item() == 1:
                self.swap_item()
                self.set_light_on()
            # Check for duplicates
            while self.compare_item() == 0:
                self.move_left()
                # Swap once past duplicates
                if self.compare_item() == 1:
                    self.swap_item()
            # Toggle light off in None is on the left, signifying end
            self.move_left()
            if self.compare_item() is None:
                self.set_light_off()
            else:
                self.move_right()
        else:
            # Move left until not possible
            while not self.compare_item() is None:
                self.move_left()
                # Swap if greater than
                if self.compare_item() == 1:
                    self.swap_item()
                    self.set_light_on()
            # If none, we're at the left bound and swap can be made
            self.swap_item()
            self.move_right()
            self.swap_item()
            self.set_light_on()
        return


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    lis = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(lis)

    robot.sort()
    print(robot._list)
