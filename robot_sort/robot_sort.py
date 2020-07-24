# Understand:
#
# Using the methods provided in the SortingRobot class, we need to sort from lowest
# to highest the values of the list that is passed in to the instance of SortingRobot. We were told
# that we needed to understand very well the sorting methods of bubble and selection sort. Given the
# constraints given to accomplish this sort, the only method that does not involve storing any variables
# is the bubble sort method.

# Plan:

# Turn the robots light on to start the program.

# Given the list [5,4,3,2,1], the robot should pick up the first item in the list and deposit the None value.
# It should move right as far as possible comparing the value it holds to each value in front of it along the way. If the value held is
# greater than the value in front of it then it should swap so that when it is at its rightmost position it should be holding the
# lowest value in the unsorted list. It should then move left to the None value, deposit its low value and move the None value one position
# to the right, thereby seperating the sorted array from the unsorted array.

# This process should be repeated until the None value is at the rightmost position, indicating that the full list has been sorted.

# The robot should then switch off its light causing the program to exit.


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
        # Execute:

        # Turn the light on to initiate the sort
        self.set_light_on()

        while self.light_is_on():

            # Drop the None value and pick up the item in the list in front of the robot
            self.swap_item()

            # While moving right till the end of the list
            while self.can_move_right():
                self.move_right()

                # Check if the value held is greater, it it is
                # pick up the lower value
                if self.compare_item() == 1:
                    self.swap_item()

            # When the robot is at the rightmost position, it should hold the lowest
            # value and should then move back left until it reaches the None value.
            while self.can_move_left() and self.compare_item() is not None:
                self.move_left()

            # Drop the low value and pick up None
            self.swap_item()

            # Move one position to the right
            if self.can_move_right():
                self.move_right()

            else:
                # Turn the robot's light off to terminate the program's outer while loop
                # and exit the program
                self.set_light_off()

# REFLECT:

# There may be a way to move left and right comparing greater values one way and lesser values the other direction
# that may improve the runtime of this sort, however time does not allow for refactoring the above code in this case.


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
