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

answers1 = {"___1___":"function","___2___": "argument","___3___":"none","___4___": "list"}
instructions = "You will get 5 guesses per problem\
\nThe current paragraph reads as such:\n"
###
spl1 = ''' A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
spl2 = "Test2"
spl3 = "test3"

# word = raw_input("Please select a game difficulty by typing it in!\n"
#   "Possible choices include easy, medium, and hard.\n")
# word = word.lower()
###

# Pseudo Code Step 1---> Select Difficulty level
def selectdiff():
  # returns sample based off of difficulty level 
  diffdict = {'easy': spl1, 'medium': spl2, 'hard':spl3}
  lvlselect = raw_input("Please select a game difficulty by typing it in!\n"
  "Possible choices include easy, medium, and hard.\n")
  lvlselect = lvlselect.lower()
  if lvlselect in diffdict:
    return diffdict[lvlselect]
    
    
#print selectdiff()

def popdict():
  #populates dictionary with sample
  quesdict = {}
  sample = selectdiff()
  sample = sample.split()
  #return sample
  for placeholder in sample:
    if placeholder in answers1:
      return placeholder
    
    
print popdict()  


key = "___1___"
script = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
words = script.split()
#print y
#print x in y
def example():
  dict = {}
  for word in words:
    if key in word:
      print "hi"
      script = script.replace(word, "Eban  is a beast" )
  print script
#print example()
#print script


  

'''
def selectdiff():
  # returns selected sample or asks to input again if invalid
  lvlselect = raw_input("Please select a game difficulty by typing it in!\n"
  "Possible choices include easy, medium, and hard.\n")
  lvlselect = lvlselect.lower()
  while True:
    if lvlselect == "easy":
      return spl1
    elif lvlselect == "medium":
      return spl2
    elif lvlselect == "hard":
      return spl3
    else: 
      return "Incorrect input. Please try again"
#print selectdiff(lvlselect) 

# Pseudo Code Step 2 ---> Identify placeholders in script
def word_in_placeholders(word, placeholders):
  for pholder in placeholders:
    if pholder in word:
      return pholder
  return None
#print word_in_placeholders("___1___", spl1.split())


# Pseudo Code Step 3 ----> Incorporate word_in_placeholders into a loop to iterate the sample(spl)
spl = selectdiff()
spl = spl.split()
qprompt = word_in_placeholders(word, placeholders)
#print spl
def play_game(spl):
  for 
  
    if word in placeholders:
      return "What should be substituted for " + word
#print play_game(spl)








 def word_in_diff( word, diff):
  #word = word.lower()
 # print "word" word
  for lvl in diff:
    #lvl = lvl.lower()
   # print (" print lvl: " + lvl)
    if lvl in word:
      return lvl
    return None
#print (" print word_in_diff(word, diff) : " + str(word_in_diff( word, diff )))

def sample_choice():
  difflvl = word_in_diff( word, diff)
  print ("difflvl: " + difflvl)
  while difflvl != None:
    if difflvl == "easy":
      return " You have selected easy mode!"
    elif difflvl == "medium":
      return " You have selected medium mode"
    elif difflvl == "hard":
      return " You have selected hard mode"
  else: return "Choice invalid. Please try again"
print sample_choice()
    
#def play_game(ml_string, parts_of_speech):    
#     replaced = []
#     ml_string = ml_string.split()
#     for word in ml_string:
#         replacement = word_in_pos(word, parts_of_speech)
#         if replacement != None:
#             user_input = raw_input("Type in a: " + replacement + " ")
#             word = word.replace(replacement, user_input)
#             replaced.append(word)
#         else:
#             replaced.append(word)
#     replaced = " ".join(replaced)
#     return replaced
     

def difficultylvl():
  sample = "placeholder"
  replacement = "placeholder"   
  script = "You have chosen " + replacement + instructions + sample
  difficulty = raw_input("Please select a game difficulty by typing it in!\n"
  "Possible choices include easy, medium, and hard.\n")
  while difficulty == "easy" or "medium" or "hard":
      replacement = difficulty
      sample = word.replace(replacement, )
      script = "You have chosen "  + replacement + "! " + instructions +
      return script

instructions =  "\n You will get 5 guesses per problem\n\
The current paragraph reads as such:\n"
difficulty = raw_input("Please select a game difficulty by typing it in!\n")



def difflvl():
  while difficulty is "easy" or "medium" or "hard":
    print difficulty
    if difficulty == "easy":
      replacement = difficulty
      time.sleep(1)
      print "\n You have chosen easy!\n"
      time.sleep(2)
      return instructions + spl1
    elif difficulty == "medium":
      time.sleep(1)
      print "\n You have chosen medium"
      time.sleep(2)
      return instructions + spl2
    elif difficulty == "hard":
      time.sleep(1)
      print "\nI bet you like it hard\n"
      time.sleep(2)
      return instructions + spl2
  else:
    return "Error, Please try again."
print difflvl()

#def play_game(): 
'''