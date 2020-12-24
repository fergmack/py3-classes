# Suppose you have a point object and wish to find the midpoint halfway between it and some other target point. We would like to write a method, let’s call it halfway, which takes another Point as a parameter and returns the Point that is halfway between the point and the target point it accepts as input.


class Point:
  def __init__(self, initX, initY):
    self.x = initX
    self.y = initY

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def distance_from_origin(self):
    return ( (self.x ** 2) + (self.y ** 2) ** 0.5)

  def halfway(self, target):
    mx = (self.x + target.y)/2
    my = (self.y + target.y)/2
    return Point(mx, my)
    

  def __str__(self):
    return 'x = {}, y = {}'.format(self.x, self.y)

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())
