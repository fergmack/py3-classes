L = ['Cherry', 'Apple', 'Blueberry']

print(sorted(L, key=len))
# or 
print(sorted(L, key=lambda x: len(x)) ) 

# When each of the items in a list is an instance of a class, you need to provide a function that takes one instance as an input, and returns a number. The instances will be sorted by their numbers.

# class Fruit():
#   def __init__(self, name, price):
#     self.name = name
#     self.price = price

# L = [Fruit('Cherry', 10), Fruit('Apple', 5), Fruit('Blueberry', 20)]

# for f in sorted(L, key=lambda x: x.price):
#   print(f.name)

  # Part 2

class Fruit():
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def sort_priority(self):
      return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
  print (f.name)

  print("---- one more way to do the same thing-----")
for f in sorted(L, key= lambda x: x.sort_priority() ):
  print(f.name)
