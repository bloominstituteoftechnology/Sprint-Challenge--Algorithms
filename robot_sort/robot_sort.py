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
        # Note on selected approach: Time is only incremented in the provided prompt functions when the robot 
        # moves right or left along the list --> so we're actually trying to minimize movement here, 
        # not actual runtime. Considering this and given the robot's limited memory, merge sort 
        # (which at O(nlogn) Big O is more efficient than bubble sort, insertion sort, selection sort) 
        # seemingly is not possible or ideal here.
        # 
        # Given the constraints on the robot's movement (time is measured by moves right or left 
        # as above, not as actual runtime) and functionality, bubble sort seems to be a more 
        # "time"-efficient (where time is defined as # of moves left or right, as noted above) 
        # algorithm in this case. We can use the light to keep track of whether or not 
        # >=1 swaps were performed in our previous pass-through (>=1 swaps if light is on), 
        # because that is our only way of doing so (only memory available -- can't store any 
        # variables as per prompt).
        
        # Turn light on to enter the while loop the first time:
        self.set_light_on()
        # Repeatedly pass through the entire array and bubble sort it until every element is 
        # in order (0 swaps performed in the previous pass-through):
        while self.light_is_on():
            # Set light off as default to start (# swaps = 0);
            self.set_light_off()
            # Move to the start of the array:
            while self.can_move_left():
                self.move_left()
            # One bubble sort pass through of the entire list/array:
            while self.can_move_right():
                # Move to next index and pick up the item there:
                self.swap_item()
                self.move_right()
                # If held item's (item at previous position) value > value "in front of" the robot, 
                # swap the values in the current index (item "in front of" the robot) and 
                # previous index (item held by robot):
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    # Turn on light (only form of memory allowed) to signify >=1 swaps have been 
                    # performed in this pass-through:
                    self.set_light_on()
                # Otherwise, put the currently held item back at the previous index:
                else:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
