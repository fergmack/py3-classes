from random import randrange 

class Pet():
  # class variables to thresholds - if scores go over these - action happens
  boredom_decrement = 4
  hunger_decrement = 6
  boredom_threshold = 5
  hunger_threshold = 10 
  sounds = ['Mrrp']

  def __init__(self, name = 'Kitty'):
    self.name = name 
    self.hunger = randrange(self.hunger_threshold)
    self.boredom = randrange(self.boredom_threshold)
    # below we copy the class attribute, so that when we make changes to it we won't affect the other instances of Pets in the class
    # i.e. copy everything [:] in the sounds list 
    self.sounds = self.sounds[:]

  # methods
  def clock_tick(self):
    self.boredom += 1
    self.hunger += 1

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold: 
      return "Happy"
    elif self.hunger > self.hunger_threshold:
      return "Hungry"
    else:
      return "Bored"


  # produce current state 
  def __str__(self):
    state = " I'm " + self.name + "."
    state += " I feel " + self.mood() + ". "
    return state

  def reduce_boredom(self):
    # max so that it doesn't select a minus number - it will just select 0
    self.boredom = max(0, self.boredom - self.boredom_decrement)
  
  def reduce_hunger(self):
    self.hunger = max(0, self.hunger - self.hunger_decrement)

  # interaction methods
  def hi(self):
    # print a random sound
    print(self.sounds[randrange(len(self.sounds))])
    self.reduce_boredom()

  def teach(self, word):
    self.sounds.append(word)
    self.reduce_boredom()

  def feed(self):
    self.reduce_hunger()

# Create an instance of a pet 
p1 = Pet('Fido')
print(p1)

# time passes
for i in range(10):
  p1.clock_tick()
  print(p1)
  
# he's bored and hungry - feed him, say hi, and teach him a word
p1.feed()
p1.hi()
p1.teach('Boo')

for i in range(10):
  p1.hi()

print(p1)
p1.feed() 
print(p1)
p1.hi()
p1.teach('Yo')
p1.hi()


