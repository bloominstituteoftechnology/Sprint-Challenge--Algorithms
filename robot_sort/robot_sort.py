"""
Proposed Strategy

* Model the robot sorting mechanism as a "bubble sort"
* The robot will use its powers to compare adjacent list elements
  as it traverses from left to right (`move_right` & `can_move_right` methods)
* It will swap adjacent elements if the right element is less than the left element (`swap_item` method)
* The robot will then shift back the beginning (far left) and repeat the process (`move_left` & `can_move_left` methods)
* When a left to right pass has been completed without a swap, the sorting process is done
    * The robot can use it's memory capability (`set_light_on`, `set_light_off`, `light_is_on` methods)
"""

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

    def foo(self):
        pass
    
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

    def back_to_start(self):
        # Can we move left? If so, repeated move to the left
        while self.can_move_left():
            self.move_left()

        # Can't move any further left; should be back at the start of the list
        return

    # process_elm_pairs proceses adjacent element
    def process_elm_pairs(self):
        # Can the robot move to the right?
        if not self.can_move_right:
            # Can't move to the right, no processing can be done
            return

        self.swap_item()        # swap: item = #1 val; #1 elm = None
        self.move_right()       # move right: (pos = #2 elm)

        # Is the item (#1 val) > #2 val?
        if self.compare_item() == 1:
            # Yes, the item (#1 val) > #2 val
            self.swap_item()    # swap: #2 elm = #1 val; item = #2 val
            self.set_light_on() # turn on the robot's light
            self.move_left()    # move left: pos = #1 elm
            self.swap_item()    # swap: #1 elm = #2 val; item = None
            self.foo()
        else:
            # Yes, the item (#1 val) < #2 val
            #   item back to None
            self.move_left()    # move left: pos = #1 elm
            self.swap_item()
            self.foo()

        # Move back again to the right (to pos: #2 elm)
        self.move_right()

        return


    def sort(self):
        """
        Sort the robot's list.
        """

        # Turn on the robot's light (proxy: swap indicator)
        self.set_light_on()

        # Iterate through the list comparing adjacent elements (call fn: process_elm_pairs)
        while self.light_is_on():
            self.set_light_off() 

            # Traverse down the robot's list from left to right
            while self.can_move_right():
                # Process two adjacent list elements
                self.process_elm_pairs()

                # Can we move to the right?
                if not self.can_move_right():
                    # no: break out of the iteration
                    break

            # Has a swap been made in this traversal (light is on)?
            if self.light_is_on():
                # Swap made; shift to the beginning (far left) and iterate again
                self.back_to_start()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
