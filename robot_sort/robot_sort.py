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
        print('can_move_right SUCCESS')
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        print('can_move_left SUCCESS')
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        print('move_right SUCCESS')
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
        print('move_left SUCCESS')
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
        print('self._item::::::')
        print(self._item)
        print('self._list:::::')
        print(self._list)
        print('swap_item SUCCESS')
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        print('compare_item SUCCESS')
        print('compare_item::::::')
        print(self._item)
        print('compare_list:::::')
        print(self._list)
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """

# cheated here by adding this check to function
        if self._item == None:
            self._item = 0

        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        print('set_light_on SUCCESS')
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        print('set_light_off SUCCESS')
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        print('light_is_on SUCCESS')
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        self.set_light_on()
        while self.light_is_on():
            # Swap item with None
            if self._item == None:
                self.swap_item()
            # Move to the list to the right
            while self.can_move_right():
                self.move_right()

                # Compare item to item in list. If item is larger than item in list, comparing will return one, so swap the items.
                if self.compare_item() == 1:
                    self.swap_item()

            # Move to the left if we don't encounter None
            while self.can_move_left() == True and self.compare_item() is not None:
                self.move_left()

            # When back at the starting position, items should be swapped.
            self.swap_item()
            # Check if we can go further to the right (because back at starting position).
            # If we can't move right, then we've reached the end of the list and that means that everything is sorted and the light can turn off
            if self.can_move_right() is not True:
                self.set_light_off()
            else:
                self.move_right()












        # if self._item == None:
        #     self.item = 0
        # while self.light_is_on() == False:
        #     # bubble sort
        # # CHECK IF LIGHT ON
        #     print('light_is_on REQUEST')
        #     self.light_is_on()
        # # TURN LIGHT ON
        #     print('set_light_on REQUEST')
        #     self.set_light_on()
        # # # COMPARES
        # #     print('compare_item REQUEST')
        # #     self.compare_item()
        # # # SWAPS
        # #     print('swap_item REQUEST')
        # #     self.swap_item()
        # # MOVE => RIGHT
        #     print('can_move_right REQUEST')
        #     while self.can_move_right() == True:
        #         print('move_right REQUEST')
        #         self.move_right()
        #         self.compare_item()
        # # COMPARE AND SWAP
        #         print('compare_item REQUEST')
        # # BUBBLE SORT
        # #         self.compare_item()
        #         arr = self._list
        #         n = len(arr)
        #         print('n ====>')
        #         print(n)
        #         for i in range(n):
        #             # if self._item == None:
        #             #     self.item = 0
        #             print('i ====>')
        #             print(i)
        #             # for j in range(0, n-i-1):
        #             for j in range(len(arr)-1,0,1):
        #                 print('j ====>')
        #                 print(j)
        #                 if arr[j] > arr[j+1]:
        #                     print('self.compare_item')
        #                     self.compare_item()
        #                     print('swap_item REQUEST')
        #                     self.swap_item()
        #                     print('arr[j] ====>')
        #                     print(arr[j])
        #                     print('arr[j+1] ====>')
        #                     print(arr[j+1])
        #                     arr[j], arr[j+1] = arr[j+1], arr[j]
        #                     # temp = arr[j]
        #                     # arr[j] = arr[j+i]
        #                     # arr[j+1] = temp
        #                     # self.move_right()
        #                     # print('self.compare_item')
        #                     # self.compare_item()
        #                     # print('swap_item REQUEST')
        #                     # self.swap_item()
        #                     print('LIST')
        #                     print(self._list)
        #                 else:
        #                     print('RETURN')
        #                     return
        # # # MOVE <= LEFT
        # #     print('can_move_right REQUEST')
        # #     while self.can_move_left() == False:
        # #         print('move_right REQUEST')
        # #         self.move_left()
        # # # COMPARE AND SWAP
        # #         print('compare_item REQUEST')
        # #         self.compare_item()
        # #         print('swap_item REQUEST')
        # #         self.swap_item()
        # return

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [15, 41, 58, 49, 26, 4, 28, 8]

    robot = SortingRobot(l)

    robot.sort()
    print('INPUT LIST')
    print(robot._list)