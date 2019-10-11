'''
Objective: Utilize given methods on robot class to sort through a list.
Plan :
The given abilities of the robot most closely resemble the activities of a bubble sort or a selection sort.
I am able to grab and hold values and compare the values in front of the robot to the ones it is holding.
I will have to use the move methods to resemble an index looping through an array.
- the robot will compare the # in front of it to the # to its left and swap them if the # to left is higher than
the # to its right. It will continue to do so until it has gone through all the #'s and by the end the list it looped
through will be sorted bubble sort style.
- new plan will try to implement selection sort instead
psuedocode
* Robot can only compare the # he holds to number he is infront of *

for i in range(0, len(list)):
    index_of_smallest_# = i (Might have to pick up item at this step)
    #robot has to move along with loop

    for j in range(i + 1, len(list)):
    #robot has to move along with loop

        if item_holding > item_infront_of_robot:
            # Re assign the index of the smallest number
            index_of_smallest_# = j

        #store value of list[i] in temp var
        temp = list[i]
        #swap the value of list[i] for the value of the list[index_of_smallest_num]
        #robot has to perform this swap ...
        #How can the robot swap these two items.
        #He has to hold on and be in front of the other one
        list[i] = list[index_of_smallest_num]
        arr[index_of_smallest_num] = temp

    return list

'''
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

    def sort(self, list):
        for i in range(0, len(list)):
            index_of_smallest_num = i #Does the robot have to pick this up? If it picks it up and no item is > how does it have to drop it back off?
            self.swap_item() # Trying out picking up item in order to figure out how to compare down the list.

            print(f"Robot holding (1st loop) = {robot._item}")
            print(f"Robot return position (1st loop)= {robot._position}")

            #if i > 0:
            #self.move_right()
            print(f"Robot return position + 1 = {robot._position}\n")

            for j in range(i + 1, len(list)):
                #if j > 1:
                self.move_right()
                print(f"Robot index > 0 (2nd loop) = {robot._position}")

                if self.compare_item == 0:
                    #drop item back off at where it picked it up
                    pass
                if self.compare_item() == 1:
                    # Re assign the index of the smallest number
                    index_of_smallest_num = j # -> this is the index the robot needs to be in in order to swap with the item its holding.
                    print(f"SMALLEST # = {list[index_of_smallest_num]}")

                print(f"Swap position : {index_of_smallest_num} current position (2nd loop) = {robot._position}\n")
                #self.swap_item()
                #print(f"Robot holding SWAP = {robot._item}")

                temp = list[i]
                list[i] = list[index_of_smallest_num]
                list[index_of_smallest_num] = temp

                print(f"Robot holding (2nd loop) = {robot._item}")
                print(f"Robot index (2nd loop) = {robot._position}")

        return list


l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21]

robot = SortingRobot(l)

print(f"{robot.sort(l)}")

'''# store value of list[i] in temp var
temp = list[i] # -> The value that was picked up at first

# swap the value of list[i] for the value of the list[index_of_smallest_num]
# robot has to perform this swap ...
# How can the robot swap these two items.
# He has to hold one and be in front of the other one
list[i] = list[index_of_smallest_num]
print(f"Robot holding (2nd loop) = {robot._item}")
list[index_of_smallest_num] = temp'''''

#print(f"Robot index = {robot._position}")
#print(f"Robot holding = {robot._item}")
#print(f"light is = {robot._light}")


'''if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)'''