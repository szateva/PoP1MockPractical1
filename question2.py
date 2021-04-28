""" Question 2  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 7 marks
Implement a function
common_elements(list1, list2)
which returns a list that contains the common elements of the lists of integers list1
and list2 in the increasing order and without duplicates. The input lists may be
unordered, of unequal size, and may contain duplicates.
Indicative test cases:
assert common_elements([3,1,2], [2,4,3])== [2,3]
assert common_elements([3,3,2], [3,3,4,5])== [3] """

def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_set =set1.intersection(set2)
    common_list = list(common_set)
    common_list.sort()
    return common_list

assert common_elements([3,1,2], [2,4,3])== [2,3]
assert common_elements([3,3,2], [3,3,4,5])== [3]