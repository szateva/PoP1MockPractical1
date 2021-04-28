""" Question 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 15 marks
Implement a function
shortest_continuous_segment(s)
which takes a non-empty list s containing integer numbers. Find the shortest segment
where the same number occurs continuously in s. The function must return a tuple
(I,N) where I is the number and N is the length of this shortest sequence. If there are
several numbers for which the shortest continuous sequence has the same length, print
the required information for the greatest number. Do not import any libraries.
Indicative test cases:
assert shortest_continuous_segment([1,1,2,2,2,1,1,1]) == (1, 2)
assert shortest_continuous_segment([5,5,5,2,2,2,2,3,3,3]) == (5, 3) """