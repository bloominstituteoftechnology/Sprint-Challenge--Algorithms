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
        # the robot's light "on" and "off" can indicate if/when a swap has occured
        # We can begin by setting his light on to enter a loop that will begin the
        # swapping process
        self.set_light_on()

        # we need to check each element agtainst its proceeding neighbor
        # moving the robot to the right until it can't move anymore
        # we can then place the held None value at the end
        # We can move this None value slowly to the left of the list
        # acting as a wall between the unsorted list and the sorted
        # list

        while self.can_move_right():
            self.move_right()  # move robot all the way to the right
        
        self.swap_item()  # swap items so None value is in last spot

        # create the loop based on the light system
        while self.light_is_on():
            # start by setting the light back to off
            self.set_light_off()

            # make sure robot is as far left as it can go
            while self.can_move_left():
                self.move_left()

            # create loop that runs as long as robot can move to the right
            while self.can_move_right():
                # have robot compare items
                # if item robot is holding has value less than item it is comparing
                # swap the items
                if self.compare_item() == - 1:
                    self.swap_item()
                    self.set_light_on  # a swap occured, so switch light on
                    self.move_right()  # move right once
                
                # while comparinjg items, if robot runs into None value, that means it
                # has reached end of the unsorted list.
                # Swap the value the robot is holding (which should be the highest value
                # in the unsorted list up to this point) with the None value
                elif self.compare_item() is None:
                    self.swap_item()
                    if self.can_move_left():  # check if robot can move left
                        self.move_left()  # move left
                        self.swap_item()  # swap item (this creates the new end of unsorted list)
                        self.set_light_on()  # swap occured so switch light on
                        if self.can_move_left():  # check if robot is at the first position in the list
                            while self.can_move_right():  # while robot can move right
                                self.move_right()  # move right
                        else:  # if robot is at first position
                            self.set_light_off()  # turn light off - we have sorted everything we can
                            while self.can_move_right():  # while robot can move right
                                self.move_right()  # move right

                else:
                    self.move_right()  # move right one position

            if self.compare_item() is None:
                self.swap_item()
                if self.can_move_left():
                    self.move_left()
                    self.swap_item()
                    self.set_light_on()
                
            while self.can_move_left():
                self.move_left()

            # this code is used for the placement of the final value
            # completing the sorted list - ensures the last item the 
            # robot holds is the None value
            if self.compare_item() is None:
                self.swap_item()
                
"""
Inside the `robot_sort` directory you'll find the `robot_sort.py` file. Open it up and read through each of the robot's abilities. Once you've understood those, start filling out the `sort()` method following these rules:

  * You may use any pre-defined robot methods.
  * You may NOT modify any pre-defined robot methods.
  * You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
  * You may use comparison operators. (`>`, `>=`, `<`, `<=`, `==`, `is`, etc.)
  * You may use iterators. (`while`, `for`, `break`, `continue`)
  * You may NOT store any variables. (`=`)
  * You may NOT access any instance variables directly. (`self._anything`)
  * You may NOT use any Python libraries or class methods. (`sorted()`, etc.)
  * You may define robot helper methods, as long as they follow all the rules.
"""


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)