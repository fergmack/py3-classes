from random import randrange 

# ************************ >>>CLASS>>> ***************************
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

# ************************ ^^^CLASS^^^ ***************************

# Create an instance of a pet 
p1 = Pet('Fido')
# print(p1)

# time passes
for i in range(10):
  p1.clock_tick()
  # print(p1)
  
# he's bored and hungry - feed him, say hi, and teach him a word
# ************* TEST OUT THE ABOVE **************
# p1.feed()
# p1.hi()
# p1.teach('Boo')

# for i in range(10):
#   p1.hi()

# USE THE BELOW TO PLAY AROUND WITH THE CODE ABOVE
# print(p1)
# p1.feed() 
# print(p1)
# p1.hi()
# p1.teach('Yo')
# p1.hi()

# ************ CODE BELOW MAKES IT INTERACTIVE FOR THE USER *******
# function to select pet from the pet list
def whichone(petlist, name):
  for pet in petlist:
    if pet.name == name:
      return pet
  return None # no pet name matched in list

dog = Pet('dog')
cat = Pet('cat')
fish = Pet('fish')

# Left off can't really get this to work***

# function to run the game
def play():
  animals = []
  option = ''
  base_prompt = '''
  Commands: 
  Adopt <petname_with_no_spaces>  
  Greet  <petname>
  Teach <petname> <word>
  Feed <petname>

  To exit, type "Quit".
  
  Choice: '''
  feedback = '''\n'''
  while True:
    action = input(feedback + '\n' + base_prompt)
    feedback = '' 
    words = action.split()
    # *** what does words above contain CHECK WITH PRINT***
    if len(words) > 0: 
      command = words[0]
    else:
      command = None

# COMMANDS FOR THE PET - e.g. adopt, greet, teach, feed etc. 
    if command == 'Quit':
      print('Exited...')
      return 
    elif command == 'Adopt' and len(words) > 1:
      # words[1] selects the pet name from the input 'Adopt <pet>'
      # animals is the pet list, and word[1] is the pet name - if it's in the list then the player already has it so return feedback
      if whichone(animals, words[1]):
        feedback += '\nYou already havea pet with that name\n' 
      else: 
        # add the pet to your list if not already in it
        animals.append(Pet(words[1]))
    elif command == 'Greet' and len(words) > 1:
      # get the inputted pet from the list
      pet = whichone(animals, words[1])
      if not pet:
        feedback += "\nI don't recognise that pet name. Pleas try another.\n"
      else:
        pet.hi()
    # Making sure the length of the word list is greater than the words in the command to confirm the right phrase was entered
    elif command == 'Teach' and len(words) > 2:
      pet = whichone(animals, words[1])
      if not pet:
        feedback += "\nI don't recognise that pet name. Pleas try another.\n"
      else:
        # [2] because the way the command is structured 'teach <pet> <word>'
        pet.teach(words[2])
    elif command == 'Feed' and len(words) > 1:
      pet = whichone(animals, words[1])
      if not pet:
        feedback += "\nI don't recognise that pet name. Pleas try another.\n"
      else:
        pet.feed()
    else:
     # Nothing was understood - feedback
     feedback += "\nI don't recognise that pet name. Pleas try again.\n"

    for pet in animals:
      pet.clock_tick()
      feedback += "\n" + pet.__str__()


play()
