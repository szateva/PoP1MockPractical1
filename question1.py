""" Question 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 6 marks
Implement a function
number_of_above_averages(n, m, A)
that takes a matrix of integers A with n rows and m columns and returns a number of
positions (i; j) where an element at this position in A is greater than the average of all
the elements in A. You may assume that the matrix is specified correctly in a standard
way a list of lists.
Indicative test cases:
assert number_of_above_averages(2,2, [[1,1], [2,4]])== 1
assert number_of_above_averages(2,3, [[1,2,3], [4,5,6]]) == 3 """

def number_of_above_averages(n, m, A):
    items_in_matrix = 0
    total = 0
    for row in range(len(A)):
        for col in range(len(A[row])):
            items_in_matrix += 1
            total += A[row][col]
    average = total/items_in_matrix

    bigger_than_average = 0
    for row in range(len(A)):
        for col in range(len(A[row])):
            if A[row][col] > average:
                bigger_than_average += 1
    return bigger_than_average

assert number_of_above_averages(2,2, [[1,1], [2,4]])== 1
assert number_of_above_averages(2,3, [[1,2,3], [4,5,6]]) == 3