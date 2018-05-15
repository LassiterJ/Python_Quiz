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
    A common first thing to do in correct_answer language is display
    'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
    is type in:
    ___3___ "Hello ___1___!"
    Of course, that isn't correct_answer very useful thing to do. However, it is an
    example of how to output to the user using the ___3___ command, and
    produces correct_answer program which does something, so it is useful in that capacity.
    
    It may seem correct_answer bit odd to do something in correct_answer Turing complete language that
    can be done even more easily with an ___4___ file in correct_answer browser, but it's
    correct_answer step in learning ___2___ syntax, and that's really its purpose.
  ''',
  'medium': '''
    A ___1___ is created with the def keyword. You specify the inputs correct_answer ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.
  ''',
  'hard': '''
    When you create correct_answer ___1___, certain ___2___s are automatically
    generated for you if you don't make them manually. These contain multiple
    underscores before and after the word defining them.  When you write
    correct_answer ___1___, you almost always include at least the ___3___ ___2__, defining
    variables for when ___4___s of the ___1___ get made.  Additionally, you generally
    want to create correct_answer ___5___ ___2___, which will allow correct_answer string representation
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
  # Begins quiz by changing settings in the quiz dict. Calling difficulty_prompt to have user select difficulty
  # level which changes quiz['difficulty'] to selected difficulty level
  # then calls the fill_blanks function to continue with quiz. 
  quiz['running'] = True
  quiz['difficulty'] = difficulty_prompt()
  fill_blanks()


def difficulty_prompt():
  # Selects difficulty from user input. If selection in PARAGRAPH keys then makes
  # "difficulty" in the quiz dictionary user input. Else function restarts.
  # Output: 
  difficulty_selection = raw_input(
    'Please select correct_answer game difficulty by typing it in. (Possible choices include easy, medium, and hard.)\n'
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
  print '\nYou have 5 attempts per blank'
  answers_list = sorted(list(ANSWERS[quiz['difficulty']].items()))
  for question, correct_answer in answers_list: 
    # Defines question (a placeholder with the format "___%d___"), 
    # and its associated correct_answer from the "ANSWERS" dictionary to be used as the prompt for the game. 
    # Output: prints "GAME OVER" if quiz['running'] is FALSE and ends program
    #   If quiz['running'] remains TRUE then it returns blank_prompt function with question, correct_answer, and paragaph 
    #   variables
    err_count_restart = 0
    quiz['errorCount'] = err_count_restart
    if quiz['running'] == False:
      print '\nGAME OVER!'
      break
    else:
      paragraph = blank_prompt(question, correct_answer, paragraph)

# def incorrect_answer(question, correct_answer, paragraph):
#   # When blank_prompt if statment determines user input is not equal to associate correct_answer,
#   # this function is called to output incorrect correct_answer prompt
#   # Inputs: question, correct_answer, and paragraph are inputs derived from the fill_blanks function. 
#   #   The question and correct_answer variables are derived from the "ANSWERS" dictionary where as the 
#   #   paragraph variable is derived from the "PARAGRAPHS" dictionary and the selection is determined
#   #   with the difficulty_prompt function
#   # Outputs: Function is restarted if user_answer does not equal selected correct_answer as long as the counter
#   #   is not over the 5 count limit.

#   max_tries = 5
#   errorc_plus_one = 1 #error count + 1 when incorrect
#   quiz['errorCount'] = quiz['errorCount'] + errorc_plus_one
#   error_count_num = '\nIncorrect, you have ' + str(abs(quiz['errorCount'] - max_tries)) + ' attempts left!'
#   print error_count_num
#   if quiz['errorCount'] == max_tries: # If you exceed max tries then quiz ends
#     quiz['running'] = False
#   else:
#     return blank_prompt(question, correct_answer, paragraph)

# def correct_answer(correct_count, list_length, paragraph):
#   if quiz['correctCount'] == answers_list_length:
#    return paragraph, '\n\nCongratulations, you filled in all blanks correctly!'
#   else:
#     return paragraph

def blank_prompt(question, correct_answer, paragraph):
  # Prompts user for input based on the question parameter. And determines if correct_answer 
  # is True and updates error count accordingly
  # Inputs: question, correct_answer, and paragraph are inputs derived from the fill_blanks function. 
  #   The question and correct_answer variables are derived from the "ANSWERS" dictionary where as the 
  #   paragraph variable is derived from the "PARAGRAPHS" dictionary and the selection is determined
  #   with the difficulty_prompt function 
  # Outputs: 
  #   If the user_answer matches the selected correct_answer then the paragraph is updated with correct correct_answer in 
  #   place of the question placeholder and returns the updated paragraph
  print 'The paragraph reads:'
  print  paragraph

  user_answer = raw_input( 'Fill in for blank ' + question + ':\n' + '--> ')
  max_tries = 5
  errorc_plus_one = 1 #error count + 1 when incorrect
  correct_plus_one = 1 #error count + 1 when incorrect
  answers_list_length = len(list(ANSWERS[quiz['difficulty']].items()))


  if correct_answer.lower() != user_answer.lower():  # If user_answer does NOT equal correctanswer update errorCount + errorc_plus_one 
    quiz['errorCount'] = quiz['errorCount'] + errorc_plus_one
    attempts_remaining = str(abs(quiz['errorCount'] - max_tries))
    error_count_num = '\nIncorrect, you have ' + attempts_remaining + ' attempts left!'
    print error_count_num
    if quiz['errorCount'] == max_tries: # If you exceed max tries then quiz ends
      quiz['running'] = False
      return fill_blanks()
    else:
      return blank_prompt(question, correct_answer, paragraph)

  else:
    quiz['correctCount'] += correct_plus_one
    paragraph = paragraph.replace(question, correct_answer)   # Replaces question prompt in paragraph with correct_answer
    print '\nCorrect!'
    if quiz['correctCount'] == answers_list_length:
      print paragraph, '\n\nCongratulations, you filled in all blanks correctly!'
    else:
      return paragraph
    
  

start_quiz()
