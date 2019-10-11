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
        # CONSTRAINTS
            # Output should be a sorted list. i.e. [3, 1, 2] -> return [1, 2, 3]

            # What sorting algorithm to use?
                # Bubble? (Fit nicely with the swappig methon)
                # Insertion? (Dioes not seem to mesh well with the 'swap items')
                # Selection sort is impossible since we're not allowed to declare any variables

            # No efficiency requirement, but should run in less than 1 second
            # The user swaps a 'None' with the value in the list
            # What use does the light have? Is it to indicate it is carrying something?
            # Robot starts at list[0]

        # APPROACH W/ INSERTION SORT
            # Example list = [2,4,1,3]
            # item = None
            # Move over to the right (list[1] = 4)

            # Loop over the remaining unsorted list
                # Swap item at list[1]
                    # list = [2, None, 1, 3]
                    # item = 4

                # Move left until item in list <= item in inventory (which means that we've reached the correct location for the item)
                    # Move left (robot.position = 0)
                    # robot.compare == 1 (hence, item is larger than item in list, so no need to swap - same with being equal)
                    # If it were smaller, we would swap

                # Then loop over all items between robot.location and the right until we run into None
                    # Move one to the right and swap those items. (list = [2, 4, 1, 3], item = None)

                    # if robot.item == None:
                    #     break


                # Then move one to the right



            # Loop terminates when canMoveRight == false

        # Move robot over to the right to make list[0] be sorted
        robot.move_right()

        # Move over every item in the list
        for i in range(self._list):
            # Swap first unsorted item with None

            # Move to the left
                # If item in inventory > item in list (This means that the item in inventory is the biggest in the so-far sorted list)
                    # Move right
                    # Swap items.

                # elif item in list <= item in inventory 
                # OR 
                # If we're at index o of the array (can_move_left == False)
                    # Swap item in inventory with the one in list
                    # loop to the right
                        # Swap item in inventory with the one in list
                    

                        # If item in inventory is None,
                            # break



        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)