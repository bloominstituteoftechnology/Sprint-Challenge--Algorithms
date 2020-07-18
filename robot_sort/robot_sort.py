
"""
    U - This looks like an opportunity for a bubble sort. We can start iteratively at the beginning of 
        the list (on the left side) and check each element against the next element in the list.

        We're going to use the bit of memory for the robot's light as a way of indicating whether we've sorted the list at least 1 time or not. If we make it through a full pass of the list and the robot's light doesn't go off, we're good to go. 

        Otherwise, we reset the robot's light to "OFF" at the end of the loop before it starts on another pass.

    P - 
        1) Determine if we can move to the right. 

            If so, grab item at the beginning of the list.


                2) Determine - 

                    if held item > compared item:
                        grab compared item and drop held item.
                        turn the robot's light on.
                        move to the right
                    else (if they're already in the right order):
                        move to the right.

            else:
                2) Move left in the list until we can't move left anymore.
                   Turn the robot's light off. This indicates we're at the beginning 


        3) Repeat this process until we arrive at the end of the list. The larger values in this    
           implementation will "bubble" toward the end of the list.

        4) If we make it through an iteration of the entire list and the robot's light doesn't turn on,
           we can assume that the list is sorted.


    E - Write everything out.

    R - I had a thought for a faster version of the bubble sort. Since we're under the assumption that 
        the robot is a physical thing that needs to be moving back and forth, it doesn't make sense for the robot to move all the way back to the beginning of the list with each iteration.

        With the values of this sort method becoming more sorted over time (larger values bubbling to the right, smaller values bubbling to the left), we could cut our execution time by comparing items from left to right AND right to left. Then we could further decrease the size of our list by changing our starting positions since a full pass going from the start to the end and then back to the start will sort our largest item all the way to the right and our smallest item all the way to the left.

        # before a full range sorting pass - largest value and smallest values are not sorted.
        items = [ 8, 6, 7, 2, 5, 4, 3, 1]

        # after a full range sorting pass - largest and smallest values are sorted.
        items = [ 1, 6, 7, 2, 5, 4, 3, 8]

        # We can increase the efficiency of our algorithm by incrementing our starting position and 
        # decrementing our ending position.

        # before another sorting pass 
        items = [1, (6, 7, 2, 5, 4, 3), 8] # we only sort from inside the parentheses

        # after another sorting pass
        items = [1, (2, 6, 5, 4, 3, 7), 8] # we only sort from inside the parentheses

        # incremented again - 
        items = [1, 2, (6, 5, 4, 3,) 7, 8] # we only sort from inside the parentheses

        etc....
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

        # 1) Determine if we can move to the right and cannot move to the left. This is us at the beginning of the list. If these are true, grab item in front and move to the right.
        if (self.can_move_right() is True) and self.can_move_left() is False:
            self.set_light_off()
            self.swap_item()

            #   If we have the ability to move right
            while self.can_move_right() is True:
                self.move_right()
                # compare the values of the items. If the item in front is greater, swap them.
                if self.compare_item() == -1:
                    # we're indicating that we've swapped at least one item.
                    self.set_light_on()
                    self.swap_item()

        if (self.can_move_right() is True) and self.can_move_left() is False:
            self.set_light_off()
            self.swap_item()

            while self.move_left() is True:
                self.move_left()
                if self.compare() == 1:

        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
