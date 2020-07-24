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
        # Quick Solution:
        # for i in range(len(l) - 1):
        #     for j in range(0, len(l) - i - 1):
        #         if l[j] > l[j + 1]:
        #             l[j], l[j + 1] = l[j + 1], l[j]

        self.swap_item()
        for i in range(len(l) - 1):
            self.moving_items_right(i)
            self.moving_items_left(i)
            return l

        #     while (self.move_left() and self.light_is_on(), not self.light_is_on(), self.move_right() and self.light_is_on()):
        #         self.moving_items_right()
        #         self.moving_items_left()

    def moving_items_right(self, item=None):
        if self.can_move_right():
            self.move_right()
            if not self.can_move_right(): # Means I'm at the end
                if self.compare_item() == 1: # Greatest item in my hand
                    self.swap_item()
                    self.set_light_on() # Indicate this item goes here
                self.set_light_on() # Greatest item was already here. Signify it stays
                return
            if self.compare_item() == -1:
                self.swap_item() # Swapping my lesser item for the greater
                self.moving_items_right() # Do this again and again until I hit the end and turn the light on.

    def moving_items_left(self, item=None):
        if self.can_move_left():
            self.move_left()
            if not self.can_move_left(): # Means I'm at the beginning
                if self.compare_item() == None: # I took it in the beginning
                    self.swap_item()
                    self.set_light_on() # Indicate this item goes here
            if self.compare_item() == 1:
                self.swap_item() # Swapping my greater item for the lesser
                self.moving_items_left() # Do this again and again until I hit the end and turn the light on.


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

    '''
PLAN
    1. Check where I am at
        - Check left to verify I am at start
        - Check right to make sure I can move right
            - Should find out I am at the beginning of the list.

    2. Pick up the item at current position. (This should be item at index 0)

    3. (First case exception where I don't check if I can move right) Normally
    will check if I can move right or not.

    4. Move to next position

    5. Check if I can move right again
        - If I am at the very end I do not need to swap items if the item on the ground happens to be greater.
            This means the greatest number was found at the end and I don't want to swap it with my item
            just to swap it back. Wasting moves.

    6. Compare the item in my hand to the item on the ground.
        - If the item in my hand < the item on the ground
            - Swap
        - Else
            - My item is greater so I keep it
        - Check right
            - Move right if there is space 

    7. Repeat steps 3, 4 & 5 until I reach the end.

    8. Once I am at the end I either swap to put the greatest item down or leave the item on the ground there
    because it is the greatest item.
        - I want to turn my light on indicating this number goes in this spot.

    9. Check if I can go left
        - Move position left.

    10. Check I can go left again

    11. Compare the item in my hand to the item on the ground.
        - If the item in my hand > the item on the ground
            - Swap
        - Else
            - My item is less so I keep it

    12. Repeat step 9, 10 & 11 until I reach the other end.

    13. Once I am at the beginning again I compare my items to see if I want to swap
    or not (I either have the most less number or it is on the ground).
        - I turn my light on to indicate this number goes in this spot.
'''