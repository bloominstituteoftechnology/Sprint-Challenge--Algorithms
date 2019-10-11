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

    def swap_right(self):
        """
        Iterates right and turns on the light if a swap has been made.
        """
        #  turns off the swap flag
        self.set_light_off()

        # print('starting right pass')
        # print('item', self._item)
        # print('position', self._position)
        # print('list', self._list)

        #Move to the last position of the list
        while self.can_move_right():
            # we want to swap items in one situation, if the held item is smaller, this moves items to the right
            if self.compare_item() < 0:
                
                # print('swapping right') 
                # print('item', self._item)
                # print('position', self._position)
                # print('list', self._list)
                
                self.swap_item()
                self.move_right()
                
                # print('swapped right now holding')
                # print('item', self._item)
                # print('position', self._position)
                # print('list', self._list)   

                # set our light on as a flag to iterate again
                self.set_light_on()

            # if held item is equal or > next item, just move right
            else:
                # print('no swap', self._item, self._position)
                self.move_right()
            
        
        # print('end of right pass', self._item, self._position)
        # print('light equals', self._light)
        # print(self._list)

        # we always call a left pass b/c that picks up the nonetype
        self.swap_left()

    def swap_left(self):
        """
        Iterates to the first position of the list, swapping backwards, grabs the none if the light is off.
        """
        # print('starting left pass')
        # print('item', self._item)
        # print('position', self._position)
        # print('list', self._list)


        # moves left to the first position
        while self.can_move_left():

            # now we are moving left and comparing right
            # this means that if the item we are holding is bigger, we want to swap it right to take the smallest item back
            if self.compare_item() > 0:
                # print('swapping left ', self._item, self._position)
                self.swap_item()
                self.move_left()
                # print('swapped left now holding x at x ', self._item, self._position)
                
                # set our light off as backwards swaps can be the smallest item percolating downwards
                self.set_light_off()
            
            # if our held item is less or equal we want to hold it and move left
            else:
                # print('no swap', self._item, self._position)
                self.move_left()
        
        # print('end of left pass', self._item, self._position)
        # print('light equals', self._light)
        # print(self._list)

        # at the begining of the list, we should be 'over' the nonetype but have the smallest element in our hand
        # so if there were no swaps right, we should swap the smallest for the nonetype, otherwise we iterate again with the smallest element
        

        if self.compare_item() == None and self.light_is_on() == False:
            # this is the situation where we pick up the none type if the light is off
            self.swap_item()    
            # print('Got the None! No more swaps!', self._item)
            # print('light equals', self._light)
         
        else:
            # if there has been a swap we call a right pass
            # print('calling another right swap')
            # print('light equals', self._light)
            self.swap_right()

    def bubble_sort(self):
        "bubble sorts the list using a recursive call right"
        # we swap once to get rid of the None type in our hand
        self.swap_item()
        # iterate to the end of the list
        self.swap_right()


    # def selection_sort(self):
    #     """
    #     Performs insertion sort on the robo list.
    #     """
        # grab first item to get rid of NoneType
        self.swap_item()

    #     # first loop to iterate along list
    #     while self.can_move_right() == True:



       
    def sort(self):
        """
        Sort the robot's list.
        """
        # print('sorting list: ', self._list)
        
        # This is the bubble sort implementation
        self.bubble_sort()
        

        # selection_sort implementation
        

       


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 
    6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 
    37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    l2 = [3, 2, 1]

    l3 = [5, 4, 3, 2, 1]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)