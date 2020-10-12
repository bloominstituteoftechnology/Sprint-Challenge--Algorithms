UNDERSTAND
This is a sorting robot
- It will put items in ascending order
-   * It can pick up an item
    * If it tries to pick up an item while already holding one, it will swap the items instead.
- The light will be used to indicate the list has been sorted.


PLAN
Start at the beginning:
To indicate the list is unsorted -> set.set_light_on()

In order for me to start the sort, the robot needs to swap the None, in his hand with the item in the first position in order to move right.
while set.light_is_on():
    if self.compare_value == None:
        self.swap_item()

Since this will be a loop, I need to check that it can move right, and move right.
while self.can_move_right():
    self.move_right()

As I am moving right, I am comparing what the robot has in it's hands to the list item. If it is greater or None, then I will swap items. I want to swap if it's None because, otherwise it cannot correctly account for the None as it goes through the list.
    if self.compare_items() == 1 or self.compare_items() == 1:
        self.swap items()

When I've gone through to the right and can't go any further, I need to see if I can move back left and the robot does not have None in its hand. (I do not want None because the robot will automatically swap.)
    while self.can_move_left() and self.compare_item != None:
        self.move_left()

To check that the list is fully sorted, I test if the robot cannot go any further to the right and that it holds None in its hand. If this is true, I can turn off the light to indicate it is sorted and break
    while.self.can_move_right() == False and self.compare_items() == None:
        self.set_light_off()
        break