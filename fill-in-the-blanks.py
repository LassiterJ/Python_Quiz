ANSWERS = {
  'test': {
    '___1___': 'test1',
    '___2___': 'test2'
  },
  'easy': {
    '___1___': 'world',
    '___2___': 'python',
    '___3___': 'print',
    '___4___': 'html'
  },
  'medium': {
    '___1___': 'function',
    '___2___': 'argument',
    '___3___': 'none',
    '___4___': 'list'
  },
  'hard': {
    '___1___': 'class',
    '___2___': 'method',
    '___3___': '__init__',
    '___4___': 'instance',
    '___5___': '__repr__',
    '___6___': '__add__',
    '___7___': '__sub__',
    '___8___': '__lt__',
    '___9___': '__gt__',
    '___10___': '__eq__'
  }
}

PARAGRAPHS = {
  'test': 'test ___1___ test. Test ___2___ test.',
  'easy': '''
    A common first thing to do in a language is display
    'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
    is type in:
    ___3___ "Hello ___1___!"
    Of course, that isn't a very useful thing to do. However, it is an
    example of how to output to the user using the ___3___ command, and
    produces a program which does something, so it is useful in that capacity.
    
    It may seem a bit odd to do something in a Turing complete language that
    can be done even more easily with an ___4___ file in a browser, but it's
    a step in learning ___2___ syntax, and that's really its purpose.
  ''',
  'medium': '''
    A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.
  ''',
  'hard': '''
    When you create a ___1___, certain ___2___s are automatically
    generated for you if you don't make them manually. These contain multiple
    underscores before and after the word defining them.  When you write
    a ___1___, you almost always include at least the ___3___ ___2__, defining
    variables for when ___4___s of the ___1___ get made.  Additionally, you generally
    want to create a ___5___ ___2___, which will allow a string representation
    of the method to be viewed by other developers.
    
    You can also create binary operators, like ___6___ and ___7___, which
    allow + and - to be used by ___4___s of the ___1___.  Similarly, ___8___,
    ___9___, and ___10___ allow ___4___s of the ___1___ to be compared
    (with <, >, and ==).
  '''
}

quiz = {
  'errorCount': 0,
  'correctCount': 0,
  'running': False,
  'difficulty': None,
  'paragraph': None
}


def start_quiz():
  # begins quiz by changing settings in the quiz dict. calling difficulty and fill_blanks functions 
  # accordingly
  quiz['running'] = True
  quiz['difficulty'] = difficulty_prompt()
  fill_blanks()


def difficulty_prompt():
  # selects difficulty from user input. If selection in PARAGRAPH keys then makes
  # "difficulty" in the quiz dictionary user input. Else function restarts.
  difficulty_selection = raw_input(
    'Please select a game difficulty by typing it in. (Possible choices include easy, medium, and hard.)\n'
    '--> '
  ).lower()

  if difficulty_selection in PARAGRAPHS.keys():
    return difficulty_selection
  else:
    print 'Invalid difficulty selection'
    return difficulty_prompt()


def fill_blanks():
  # Prints appropriate paragraph, resets error count, determines if GAME OVER requirements have been met
  paragraph = PARAGRAPHS[quiz['difficulty']]
  print paragraph
  print '\nYou have 5 attempts per blank'

  for q, a in sorted(list(ANSWERS[quiz['difficulty']].items())): # defines q and a which is question and answer respectively
    quiz['errorCount'] = 0
    if quiz['running'] == False:
      print '\nGAME OVER!'
      break
    else:
      paragraph = blank_prompt(q, a, paragraph)


def blank_prompt(q, a, paragraph):
  # Prompts user for input based on question "q". And determines if answer 
  # is True and updates error count accordingly
  print 'The paragraph reads:'
  print paragraph

  user_answer = raw_input( 'Fill in for blank ' + q + ':\n' \
   + '--> '
  )

  if a.lower() != user_answer.lower():  # If answer is false update errorCount + 1 
    quiz['errorCount'] = quiz['errorCount'] + 1
    print '\nIncorrect, you have ' + str(abs(quiz['errorCount'] - 5)) + ' attempts left!'
    if quiz['errorCount'] == 5: # If you exceed max tries then quiz ends
      quiz['running'] = False
    else:
      return blank_prompt(q, a, paragraph) # restarts function to issue same prompt
  else:
    quiz['correctCount'] = quiz['correctCount'] + 1
    paragraph = paragraph.replace(q, a)   # Replaces question prompt in paragraph with answer
    print '\nCorrect!'
    if quiz['correctCount'] == len(list(ANSWERS[quiz['difficulty']].items())):
      print paragraph, '\n\nCongratulations, you filled in all blanks correctly!'
    else:
      return paragraph

start_quiz()
