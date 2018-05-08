'''IPND Stage 2 Final Project'''

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.
import time

# To help you get started, we've provided a sample paragraph that
# you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!



'''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''



# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
answers_test = {"___1___": "test1", "___2___": "test2"}
answers1 = {"___1___": "world","___2___": "python","___3___":"print","___4___": "html"}
answers2 = {"___1___":"function","___2___": "argument","___3___":"none","___4___": "list"}
answers3 = {"___1___":"class","___2___": "method","___3___":"__init__","___4___": "instance", "___5___": "__repr__", "___6___": "__add__", "___7___": "__sub__", "___8___": "__lt__", "___9___": "__gt__", "___10___": "__eq__"}
quesprompt = ["___1___", "___2___", "___3___", "___4___", "___5___","___6___", "___7___", "___8___", "___9___", "___10___"]
instructions = "You will get 5 guesses per problem\
\nThe current paragraph reads as such:\n"
###
test = "test ___1___ test. Test ___2___ test."
spl1 = '''A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in:
___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.'''

spl2 = ''' A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

spl3 = '''When you create a ___1___, certain ___2___s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a ___1___, you almost always include at least the ___3___ ___2__, defining
variables for when ___4___s of the ___1___ get made.  Additionally, you generally
want to create a ___5___ ___2___, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like ___6___ and ___7___, which
allow + and - to be used by ___4___s of the ___1___.  Similarly, ___8___,
___9___, and ___10___ allow ___4___s of the ___1___ to be compared
(with <, >, and ==).'''


# word = raw_input("Please select a game difficulty by typing it in!\n"
#   "Possible choices include easy, medium, and hard.\n")
# word = word.lower()
###

# Pseudo Code Step 1---> Select Difficulty level

def selectdiff():
  # returns sample and answers based off of difficulty level 
  diffdict = {'test': [test, answers_test], 'easy': [spl1, answers1], 'medium': [spl2, answers2], 'hard':[spl3, answers3]}
  lvlselect = raw_input("Please select a game difficulty by typing it in!\n"
  "Possible choices include easy, medium, and hard.\n")
  lvlselect = lvlselect.lower()
  if lvlselect in diffdict:
    print ("You have chosen " + lvlselect + "!")
    return diffdict[lvlselect]


  
def play_game():
  script, answers = selectdiff()
  # Plays game 
  print "\nYou will get 5 guesses per problem\nThe selection reads:\n " + script
  scrlist = []
  for prompt in quesprompt:
    counter = 0
    correct = False
    #print scrlist
    if prompt in scrlist:
      #print scrlist
      #print prompt
      #print counter
      continue
    elif prompt in answers:
      counter_function(prompt, scrlist, script, answers, counter, correct)
    else: 
      print "Congratulations you won!!!!!!!!"
      
def counter_function(prompt, scrlist, script, answers, counter, correct):
  while counter <= 5 and correct == False:
    user_input = raw_input("What word replaces " + prompt + " in the selection?\n")
    answer = answers.get(prompt)
    if user_input.lower() == answer:
      scrlist.append(prompt)
      #print "Scrlist: ", scrlist
      script = script.replace(prompt, answer)
      print "\nCorrect! The selection now reads\n " + script
      correct = True
      break
    else:
      num = 5 - counter
      counter += 1
      print ("Incorrect. Please try again.\nYou have  %d tries remaining" % (num))
      print counter
  else:
    print "Answer is incorrect. Out of tries\n GAME OVER BITCH"

 

play_game()



    



      

    
