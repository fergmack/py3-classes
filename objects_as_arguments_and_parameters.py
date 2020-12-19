# So here we have a class, and a function
# Remember, although both are similar, a method exists inside the class, and a function is standalone. 

import math 

# Define the Point class 
class Point:
  """Point class for representing and manipulating x, y coordinates"""
  # Constructor: 
  def __init__(self, initX, initY):

    # Define and initialise instance variables
    self.x = initX
    self.y = initY

  # Ordinary methods- note x, and y are the instance variables defined above
  def getX(self):
    return self.x

  def getY(self):
    return self.y 

  def distanceFromOrigin(self):
    return ((self.x ** 2) + (self.y ** 2) ) ** 0.5

# Define the Function 
def distance(point1, point2):

  # Invoking constructors
  xdiff = point2.getX() - point1.getX() 
  ydiff = point2.getY() - point1.getY()

  dist = math.sqrt( xdiff**2 + ydiff**2 ) 
  return dist 

# Instantiate a class Point with the points 4, 3 and origin 0, 0 etc
p = Point(4, 3)
q = Point (0, 0)

# note that p and q are class objects
print(type(p))

# These class objects are then passed to distance
print( distance (p, q) )

# -------------------------------------------------------------------------
# ***** SAME AS ABOVE BUT FUNCTION IS MOVED TO THE CLASS TO BECOME A METHOD
# -------------------------------------------------------------------------

import math 

class Point:
  """ Point class for representing and manipulating x, y coordinates """
  def __init__(self, initX, initY):

    self.x = initX 
    self.y = initY 

  def getX(self):
    return self.x 
  
  def getY(self):
    return self.y 

  def distanceFromOrigin(self):
    return ( (self.x **2 ) + (self.y **2)) ** 0.5

  # Now the distance 
  def distance(self, point2):
    xdiff = point2.getX() - self.getX()
    ydiff = point2.getY() - self.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4, 3)
q = Point(0, 0)


print(p.distance(q))

