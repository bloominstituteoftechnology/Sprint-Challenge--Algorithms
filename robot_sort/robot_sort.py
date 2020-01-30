# PSEUDOCODE
# ROBOT PICKS UP FIRST CARD (CARD A), CHECKS EACH SUBSEQUENT CARD (ITERATION OF CARD B) TO SEE IF THAT NEXT CARD IS
#  HIGHER THAN IT. IF NOT, CARD A CONTINUES ONWARD, CARD B BY CARD B, TO THE END OF THE LIST ONCE AT THE END OF THE
#  LIST, CARD A WHICH IS THE HIGHEST CARD SWAPS WITH THE CARD AT THE END OF THE LIST AND MOVES TO THE FRONT OF THE LIST
#  TO DROP THE CARD IN THE (NONE) SPOT. IF CARD A FINDS A CARD B
#  THAT IS HIGHER THAN IT, IT SWAPS WITH THAT CARD AND IS THE NEW CARD A WHICH CONTINUES CARD B BY CARD B TO THE END OF
#  THE LIST. ONCE AT THE END OF THE LIST, THE ROBOT CHECKS TO SEE IF IT CAN CONTINUE TO THE RIGHT. IF IT CANNOT, IT
#  FIRST CHECKS TO SEE IF THE CARD B AT THE END OF THE LIST IS HIGHER OR NOT, WHICH IT ONLY SWAPS IF THE CARD B IS
#  LOWER, IT SCROLLS ALL THE WAY BACK TO THE BEGINNING OF THE LIST AND DROPS THE STARTS THE PROCESS AGAIN BUT ALSO LOOKS
#  TO DROP A CARD A INTO THE (NONE) SLOT. IF (NONE) SLOT IS IN THE BEGINNING OF THE LIST, IT WILL END UP PICKING THE
#  SAME CARD BACK UP BECAUSE IT NEEDS TO CHECK IT AGAINST THE OTHER SWAPS.

#  ONCE CARD GOES ALL THE WAY TO THE END WITHOUT A SWAP, THE FINAL CARD IS CHECKED TO SEE IF IT IS HIGHER OR NOT, WHICH
#  IT WILL BE AT SOME POINT DURING PROPER SORTING. IF THE CARD AT THE END OF THE LIST IS HIGHER, THEN THE ROBOT MOVES
#  ONE STEP TO THE LEFT AT A TIME TO CHECK THE CARD B TO THE LEFT OF THE END OF THE LIST CARD B. IF HIGHER, THEN CARD IS
#  SWAPPED AND THE ROBOT AGAIN MOVES TO THE LEFT, CHECKING FOR SUBSEQUENT LOWER CARDS TO SWAP WITH AND TAKE FURTHER LEFT
#  , WHILE ALSO LOOKING FOR A (NONE) SPOT. IF CARD PLACED IN (NONE) SPOT, MOVE ROBOT ALL THE WAY TO THE LEFT OF THE LIST
#  AND START THE PROCESS OVER.

#  LIGHT TURNS ON IF A SWAP IS MADE DURING ONE PASS
#  LIGHT TURNS OFF WHEN THE ROBOT LOOPS ALL THE WAY BACK LEFT.

# THE CARDS MUST BE CHECKED AFTER THE END OF THE HIGH LEVEL FOR LOOP AT THE END OF EACH ITERATION IN ORDER TO ENSURE
#  ORDER.

#  WHEN NO SWAP MADE (SWAPS = 0 OR LIGHT OFF ON RETURN TO LEFT SIDE/LIST[0]), ROBOT MOVES ONE OVER TO THE RIGHT TO
#  CHECK IF THAT

# PSEUDOCODE 2
# SELECTION SORT
# ROBOT PICKS UP ITEM, COMPARES TO EACH ITEM ON RIGHT, IF ITEM ON RIGHT IS LOWER, SWAP CARD. CONTINUE TO END IN SAME
# PROCESS. IF NO SWAPS MADE, ROBOT MOVES ALL THE WAY BACK LEFT (ON THE WAY BACK, IT COMPARES EACH CARD TO CHECK FOR A
# 'NONE' READOUT, SWAPS WITH THE NONE, AND CONTINUES TO


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l  # The list the robot is tasked with sorting
        self._item = None  # The item the robot is holding
        self._position = 0  # The list position the robot is at
        self._light = "OFF"  # The state of the robot's light
        self._time = 0  # A time counter (stretch)

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

# # ITERATION 3
    def sort(self):
        """
        Sort the robot's list.
        """
        SortingRobot.swap_item(self)
        SortingRobot.move_right(self)
        for i in range(101):
            while SortingRobot.can_move_right(self) == True:
                if SortingRobot.compare_item(self) == None:
                    SortingRobot.swap_item(self)
                    SortingRobot.move_right(self)
                if (SortingRobot.compare_item(self) == None) and (SortingRobot.can_move_left(self) == False):
                    break
                if (SortingRobot.compare_item(self) == -1) and (SortingRobot.can_move_right(self) == True):
                    SortingRobot.swap_item(self)
                    SortingRobot.move_right(self)
                if (SortingRobot.compare_item(self) == 1) and (SortingRobot.can_move_right(self) == False):
                    SortingRobot.swap_item(self)
                if SortingRobot.compare_item(self) == 0:
                    SortingRobot.move_right(self)
                    SortingRobot.swap_item(self)
                    pass
                if SortingRobot.compare_item(self) == 1 and (SortingRobot.can_move_right(self) == True):
                    SortingRobot.move_right(self)
            if SortingRobot.can_move_right(self) == False:
                while SortingRobot.can_move_left(self) == True:
                    SortingRobot.move_left(self)
                    SortingRobot.swap_item(self)
            if (SortingRobot.compare_item(self) == -1) and (
                    SortingRobot.can_move_right(self) == False):
                while SortingRobot.can_move_left(self) == True:
                    SortingRobot.move_left(self)
                    SortingRobot.swap_item(self)
            if SortingRobot.compare_item(self) == 1 and (
                    SortingRobot.can_move_right(self) == False):
                SortingRobot.swap_item(self)
                while SortingRobot.can_move_left(self) == True:

                    SortingRobot.swap_item(self)
                    SortingRobot.move_left(self)






if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99,
         93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59,
         64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75,
         36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]




    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)