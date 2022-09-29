"""
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].
"""


# Code
def delete_nth(order, max_e):
    new_list = []
    for i in order:
        if new_list.count(i) < max_e: # if the number of times the number appears in the list is less than the max number of times it can appear
            new_list.append(i)
    return new_list
# Test 1,2,3:
print(delete_nth([20,37,20,21], 1)) # [20,37,21]
print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) # [1, 1, 3, 3, 7, 2, 2, 2]
print(delete_nth([1,1,1,1,1], 5)) # [1, 1, 1, 1, 1]