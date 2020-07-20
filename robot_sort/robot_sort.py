"""
    U - This looks like an opportunity for a recursive bubble sort. We can start at the beginning of 
        the list (on the left side) and check each element against the next element in the list.

    P - NAIVE & GREEDY IMPLEMENTATIONS
        1) Determine if we can move to the right. 

            If so, grab item at the beginning of the list.

                2) Determine - 

                    if held item < compared item:
                        grab compared item and drop held item.
                        turn the light on. This indicates we've performed a swap on that pass.
                        move to the right
                    else (if they're already in the right order):
                        move to the right.

            else:
                2) Move left in the list until we can't move left anymore.

        3) Repeat this process until we arrive at the end of the list. The larger values in this    
           implementation will "bubble" toward the end of the list. At the end, we want to exit when 
           we can't move right anymore AND the light is off.
        
        ADDENDUM - GREEDY: 
        
        I had a thought for a faster version of the bubble sort. Since we're under the assumption that
        the robot is a physical thing that needs to be moving back and forth, it doesn't make sense for 
        the robot to move all the way back to the beginning of the list with each iteration.

        With the values of this sort method becoming more sorted over time (larger values bubbling to the 
        right, smaller values bubbling to the left), we could cut our execution time by comparing items 
        from left to right AND right to left. Then we could further decrease the size of our list by 
        changing our starting positions since a full pass going from the start to the end and then back 
        to the start will sort our largest item all the way to the right and our smallest item all the 
        way to the left.

        # before a full range sorting pass - largest value and smallest values are not sorted.
        items = [ 8, 6, 7, 2, 5, 4, 3, 1]

        # after a full range sorting pass - largest and smallest values are sorted.
        items = [ 1, 6, 7, 2, 5, 4, 3, 8]

        # We can increase the efficiency of our algorithm by incrementing our starting position 
        # and decrementing our ending position.

        # before another sorting pass 
        items = [1, (6, 7, 2, 5, 4, 3), 8] # we only sort from inside the parentheses

        # after another sorting pass
        items = [1, (2, 6, 5, 4, 3, 7), 8] # we only sort from inside the parentheses

        # incremented again - 
        items = [1, 2, (6, 5, 4, 3,) 7, 8] # we only sort from inside the parentheses
        
        This should reduce our execution time from an O(n) loop to an O(n-2) on each pass of the loop 
        because we're reducing the total number of passes we'd have to do by 2 each time we complete 
        a loop iteration.   
        


    E - Write everything out.

    R - Look for ways of reducing the total number of steps required to perform the operation.
    
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

        # We're wanting to return when the robot can't move right anymore. We're using the light to keep track of whether a swap has occurred.
        if self.can_move_right() == False and self.light_is_on() == False:
            return

        # Grab the card in front.
        self.swap_item()

        # while we're able to move right and have the first card
        while self.can_move_right():
            # move to the right
            self.move_right()

            # check the value of the held card against the card in front of it.
            if self.compare_item() == -1:
                # if the card the robot is holding is LESS THAN the value of the card in front of it, grab the card in front.
                self.swap_item()
                self.set_light_on()
        # Once we reach the end of the row, the robot can't move right anymore and it should be holding the highest value it encountered. Grab that value.
        self.swap_item()
        self.set_light_off()

        # Now we go back the other way. We handle our None values here to make sure those are filtered out of the list.
        while self.can_move_left() and self.compare_item() is not None:

            # Start moving left.
            self.move_left()

            # This time if the value that the robot is holding is MORE THAN the value of the card in front of it, we grab that card. We want the smallest value.
            if self.compare_item() == 1:
                # grab it!
                self.swap_item()
                self.set_light_on()

        # Now we have the smallest value. We're gonna deposit that value all the way to the left
        self.swap_item()
        

        # Now we move to the right so we're not starting from the beginning of the list again and restart.
        self.move_right()
        self.set_light_off()
        self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
