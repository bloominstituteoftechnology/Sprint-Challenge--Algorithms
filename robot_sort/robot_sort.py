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

    def bubble_compare(self):
        self.move_right()
        self.swap_item()
        self.move_left()
        return self.compare_item()
    
    def bubble_swap(self):
        self.swap_item()
        self.move_right()
        self.swap_item()
        self.set_light_on()
        #print("swapped, light ON")

    def bubble_put_back(self):
        self.move_right()
        self.swap_item()
    
    def reset_position(self):
        self.set_light_off()
        while self.can_move_left():
            self.move_left()

    def sort(self):
        
        if self.can_move_right() == False and self.light_is_on() == True:
            self.reset_position()
            #print("Position reset at 0, light OFF")
        if self.can_move_right() == False and self.light_is_on() == False:
            if self.bubble_compare() == 1:
                self.bubble_put_back()
            else:
                self.bubble_swap()
            #print("list sorted")
            return
        while self.can_move_right() == True:
            if self.bubble_compare() == 1:
                self.bubble_put_back()
            else:
                self.bubble_swap()
            #print(self._list)
        self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    '''
     Bubble Sort Algo

     Pick up first item, if can move right then compare it to the item immediately adjacent to the one picked up.
     If held item is bigger than the item in the list then swap for the smaller item then put the smaller item in the
     empty list index to the left. If its smaller than the one not being held then you put the held item back into its original index
     and then pick up the item in the second index and compare it to the third index item. Continue this until  you're at the end
     of the list.
     
     Once at the end put down the largest
     item that was found using this process in the last position and put the item previously in that spot into the next-to-last
     index position that is empty.
     After this return all the way to the beginning of the list by moving left until you can't anymore. Pick up the first item
     and begin this process all over again. 

     To know when the list is finished being sorted, on each pass of the comparison loop, if two items in the list swap positions
     even once then the light on the robot's head is turned on. That way once the list is completely sorted, what will happen
     is that the robot will reach the right most position of the list with its light off and when it does so we know that
     the list is completely sorted and we can exit the function.
    '''



    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)