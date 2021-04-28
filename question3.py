""" Question 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 12 marks
Implement a class ManhattanTaxi that keeps track of the following features of a taxi vehicle:
 cons: an integer representing number of litres consumed per km of distance
 pos: a tuple (pair) of integers representing a position of the taxi on a map (assume
that the taxi can only be in one of the positions of the grid where the distance
between adjacent nodes is 1 km)
 fuel: a float number representing the current fuel level in litres.

Implement the following methods:
 constructor: takes four integer parameters (in the specified sequence) initX,
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

class ManhattanTaxi:
    def __init__(self, initX, initY, consumption, init_fuel ):
        self.X = initX
        self.Y = initY
        self.pos = (self.X, self.Y)
        self.cons = consumption
        self.fuel = init_fuel

    def moveto(self, X, Y):

        distance_to_X = abs(X - self.X)
        distance_to_Y = abs(Y - self.Y)
        distance = distance_to_X + distance_to_Y
        max_distance = self.fuel/self.cons

        if distance <= max_distance:
            self.X = X
            self.Y = Y
            self.pos = (X, Y)
            self.fuel -= distance
            return True
        else:
            return False
    def add_fuel(self, extra_fuel):
        self.fuel += extra_fuel

t789 = ManhattanTaxi(5, 5, 1, 30)
assert t789.moveto(3,9) == True
assert t789.pos[0] == 3 and t789.pos[1] == 9
assert abs(t789.fuel - 24) < 0.01