""" Question 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 12 marks
Implement a class ManhattanTaxi that keeps track of the following features of a taxi vehicle:
 cons: an integer representing number of litres consumed per km of distance
 pos: a tuple (pair) of integers representing a position of the taxi on a map (assume
that the taxi can only be in one of the positions of the grid where the distance
between adjacent nodes is 1 km)
 fuel: a float number representing the current fuel level in litres.

Implement the following methods:
 constructor: takes four integer parameters (in the specied sequence) initX,
initY, consumption and init_fuel, where (initX, initY) represents initial
location of the taxi, consumption represents the consumption (litre/km) and
init_fuel represents the initial fuel level
 moveto: takes two integer parameters X and Y representing the location where the
taxi needs to go to. If the taxi has enough fuel to travel there from its current
location, the method moves it there, updates remaining fuel level, and returns
True. Otherwise, the taxi does not move and False is returned.
 add_fuel: takes one integer parameter indicating how many litres of fuel are
added. No value returned.

It is important that the taxi operates in Manhattan, therefore when it travels from the
position (X1; Y1) to (X2; Y2) it follows the street block grid and covers the distance
|X2 - X1| + |Y2 - Y1|.

Indicative test cases:
t789 = ManhattanTaxi(5, 5, 1, 30)
assert t789.moveto(3,9) == True
assert t789.pos[0] == 3 and t789.pos[1]==9
assert abs(t789.fuel - 24) < 0.01"""