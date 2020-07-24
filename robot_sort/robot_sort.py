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

        You may NOT store any variables. (=)
        You may NOT access any instance variables directly. (self._anything)
        You may NOT use any Python libraries or class methods. (sorted(), etc.)
        You may define robot helper methods, as long as they follow all the rules.
        """
        # Fill this out

        # What do we know?
            # has method `can_move_right()` which returns false if robot is at end of list
            # has method `can_move_left()` which returns false if robot is at beginning of list
            # has method `move_right()` which moves to the right by 1 increment
            # has method `move_left()` which moves to the left by 1 increment
            # can `swap_item()` which swaps currently held item with list item in front
            # `compare_item()` will return 1 if item in fron of robot is greater, -1 if less, 0 if equal
            # has methods for its light as well but the other methods don't seem to depend on this ...
            # Default position is 0

        # First pass approach:
        # Start at beginning of list and compare
        # If return is None (item > None), swap and move right. Else, move right.
        # Then, move to right and compare
        # If -1, then swap again and move right
        # If 1 or 0, move to right and compare
        # Do this until end of list, and should be holding smallest item
        # Next, iterate back to beginning of list (should be holding smallest item) and compare
        # If -1, move right; if 1 swap and move right; if none swap and move right

        
        # Adding base case for when robot is at end of list
        if not self.can_move_right():
            return

        # in beginning, able to move right
        while self.can_move_right():
            # Compare
            if self.compare_item() == None:
                # swap and move right
                self.swap_item()
                self.move_right()

            # if item is greater or equal
            if self.compare_item() == 1 or self.compare_item() == 0:
                # skip it, move right
                self.move_right()
            # otherwise, item is less than
            else:
                # so swap and move right
                self.swap_item()
                self.move_right()

        # once at end, should have smallest item, but can have it work
        # back to beginning and check along the way 
        while self.can_move_left() and self.compare_item() != None:
            # Compare
            if self.compare_item() == 1:
                self.swap_item()
                # keep moving left
                self.move_left()

            else:
                # skip and move left
                self.move_left()

        # Now, robot should be back at beginning of list and holding smallest item, so
        # we can swap and start over again
        self.swap_item()
        self.move_right()
        self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    small_list = [5, 4, 3, 2, 1]

    robot = SortingRobot(small_list)

    robot.sort()
    print(robot._list)