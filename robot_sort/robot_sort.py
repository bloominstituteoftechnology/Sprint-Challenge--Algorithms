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
       # sinsertion sort it is!!
        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
    # MYYY PLAN!!

    # well since the robot can only conpare 2 items at a time and only hold one at a time i decied to use insertion sort i think but i would have to make new varibable right?

# Decide if we should use recursion to solve the problem by looking for clues in the problem description.
    # i dont think so at least not for the first pass
# Find similar problems that we’ve already solved and analyze those problems to see if they help us solve this problem.
    # i couldnt find anythign too useful - mainly because i am not sure what sorting method to use --- maybe BUBBLE SORT // takes longer idk
# Draw a diagram for a small input and study the diagram to help understand any potential solutions.
    # on paper
# If we use recursion, discover the base case or base cases.
# If we use recursion, discover the recursive case.
# Write out our algorithm as pseudocode.
# EXAMPLE FROM TK
# def bubble_sort(arr):
    # Your code here
    # swapped = True // how do i do this without delcaring a variable (it could be self.item?? try it?)

    # while swapped:
    #     swapped = False
    #     # loop through
    #     for idx in range(len(arr) - 1):
    #         num1 = arr[idx]
    #         num2 = arr[idx + 1]
    #         if num1 > num2:
    #             arr[idx], arr[idx+1] = arr[idx + 1], arr[idx]
    #             swapped = True

    # return arr

    # def bubble_sort(arr):
    # Your code here
    # item = True // how do i do this without delcaring a variable (it could be self.item?? try it?)

    # while Item:
    #     Item = False
    #     # loop through
    #     for idx in range(len(arr) - 1):
    #         num1 = arr[idx]  // maybe switch this out with self.position
    #         num2 = arr[idx + 1]
    #         if num1 > num2:
    #             arr[idx], arr[idx+1] = arr[idx + 1], arr[idx]
    #             swapped = True

    # return arr


# Change each line of pseudocode into actual code.
# Test out our code and see if it is returning the outputs that we would expect.
