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

    def bubble_right(self):
        while self.can_move_right():
            self.swap_item() # grab item to compare
            self.move_right() # go to next item up
            if self.compare_item() == 1: # 1 means we are holding a larger item
                self.swap_item() # so swap because they are out of order
                self.set_light_on() # turn light on, so we know we made a swap
            self.move_left()
            self.swap_item() 
            self.move_right()

    def bubble_left(self): # same as bubble right, but reversed
        while self.can_move_left():
            self.swap_item()
            self.move_left()
            if self.compare_item() == -1:
                self.swap_item()
                self.set_light_on()
            self.move_right()
            self.swap_item()
            self.move_left()

    def sort(self):
        """
        Sort the robot's list.
        """
        # One simple sorting algorithm that would be possible to do given the robots limited capabilities is bubble sort
        # We can use the light as a boolean to determine if our list is sorted
        # If the robot can make a complete pass through the list without picking up any items, the list is sorted
        # Since the robot must traverse the list one item at a time, we should bubble sort both ways.

        # First turn the light on
        self.set_light_on()
        
        # Then set up a while loop to keep going while the light is on
        while self.light_is_on():

            # Inside the while loop, turn the light off
            self.set_light_off()

            # Then check each item against it's neighbor, initially moving right
            self.bubble_right()

            # While moving right
                # To do the check pick up an item, move right, and compare
                # If the neighbor is larger, move back and drop the item, and move forward again
                # If, however, the neighbor is smaller, swap items, move left, drop the item, and move forward
                # Also turn the light on

            # If the light is off we break, as no items were swapped so the list is sorted
            # Otherwise we turn the light back off
            if not self.light_is_on():
                break
            self.set_light_off()

            # While moving left
            # Do everything in the list above in reverse, going right to left
            # We need this check to see if we didn't bubble anything going right
            # If so there is no poing trying to bubble items going left

            self.move_left() # Move left to avoid repeats

            self.bubble_left()



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)