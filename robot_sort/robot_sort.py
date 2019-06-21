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

        """
            Understand:
                Objective is to sort list elements.

                What are the provided functions:
                Can move right - returns True unless at end of list
                Can move left - returns True unless at beginning of list
                Move right - increments position and returns True if possible
                Move left - decrements position and returns True if possible
                Swap item - exchanges item for el at position
                Compare item - compare item to el at position 
                    1 if item is larger
                    -1 if item is smaller
                    None if None
                    else 0
                Set light on
                Set light off
                Light is on

            Plan:
                - turn on light
                - loop in while loop of is light on
                    - pick up item
                    - while can move right
                        - move right
                        - compare
                            - if -1 (less)
                                - swap

                    if can not move right
                        light is off
                                    
                    - while can move left
                        - move left
                        - compare
                            if 1 ( greater )
                                light is on
                        - pick up item

            New Plan:
                - turn on light
                - loop while light is on
                    - pick up item
                    - if can move right
                        - move right
                    -while can move right
                        - is item in hand greater than el in position? (1)
                            -swap
                        - move right
                    
                    - if can move left
                        - move left
                    
                    - turn light off

                    -while can move left
                        - is item in hand greater than in position? (1)
                            - turn light on
                            - if can move right
                                - move right
                                - swap

            Yet another plan:
                - set light on

                - swap

                - while can move right
                    - move right
                    - is item greater than next item? (1)
                        swap

                if can NOT move right AND compare == None:
                    set light off

                - while can move left

                    - is item less than? (-1)
                        - move left
                    - is item greater than the next item? (1)
                        - move right
                        - swap
                        - set light on
                    - is None
                        swap
            

            Another NEW Plan:

                - set light on
                
                while light is on
                    
                    if None:
                        swap


                    while can move right is True
                        move right

                        if 1:
                            Don't swap!

                        elif -1:
                            swap!
                        
                        if can NOT move right AND 1:
                            swap!

                    while can move left is True
                        move left

                        if 1:
                            Swap!

                        elif -1:

                            Don't swap!

                        elif None and can move right:
                            Swap!
                            
                            move right

                            break

                        elif None and can NOT move right:
                            set light off
                            break
        """

        self.set_light_on()
        
        while self.light_is_on() == True:

            if self.compare_item() == None:
                self.swap_item()

            while self.can_move_right() == True:

                self.move_right()

                if self.compare_item() == -1 and self.can_move_right() == True:
                    self.swap_item() 

                elif self.can_move_right() == False and self.compare_item() == 1:
                    self.swap_item() # Will this work??


            while self.can_move_left() == True:

                self.move_left()

                if self.compare_item() == 1:
                    self.swap_item()

                elif self.compare_item() == None and self.can_move_right() == True:
                    self.swap_item()
                    self.move_right()

                    if self.can_move_right() == False and self.compare_item() == None:
                        self.set_light_off()

                    break

                elif self.compare_item() == None and self.can_move_right() == False:
                    self.set_light_off()
                    break


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)