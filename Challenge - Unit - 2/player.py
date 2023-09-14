'''
Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
'''

# Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batsmam
class Batsman:
  def play(self):
    print("The Batsmam is playing cricket.")

# Define the derived class Bowler
class Bowler:
  def play(self):
    print("The Bowler is playing cricket.")

# Create object of Batsmam and Bowler classes
batsmam = Batsman()
bowlwe = Bowler()

# call the play() method for each object
batsmam.play()
bowlwe.play()
