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
  # then calls the fill_blanks function to initiate the rest of the quiz. 
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
  # Prints game rules and starting paragraph. 
  # Then calls question_loop defining answers_list for question_loop's input
  quiz["paragraph"] = PARAGRAPHS[quiz['difficulty']]
  paragraph = quiz["paragraph"]
  print '\nYou have 5 attempts per blank'
  print "\n The paragraph reads:\n" , paragraph
  answers_list = sorted(list(ANSWERS[quiz['difficulty']].items()))
  question_loop(answers_list)

def question_loop(answers_list):
  for question, correct_answer in answers_list: 
    # Defines question (a placeholder with the format "___%d___"), 
    #   and its associated correct_answer from the "ANSWERS" dictionary to be used as the prompt for the game. 
    # Output: prints "GAME OVER" if quiz['running'] is FALSE and ends program
    #   If quiz['running'] remains TRUE then it returns game_running function with question, correct_answer, and paragaph 
    #   variables
    if quiz['running'] == False:
      print '\nGAME OVER!'
      break
    else:
      game_running(question,correct_answer)
def game_running(question, correct_answer):
      # Asks for user input and runs check_user_answer if its correct.
      # If check_user_answer returns True then functions on_correct_user_answer and check_end_questions run
      #   and loop is broken.
      # If check_user_answer is False on_incorrect_user_answer and too_many_attempts runs
      # Inputs question, correct_answer
      while quiz['running'] == True:
        user_answer = ask_question(question)
        is_correct = check_user_answer(correct_answer, user_answer)
        if (is_correct == True):
          on_correct_user_answer(question, correct_answer)
          check_end_questions()
          break

        else:
          on_incorrect_user_answer()
          too_many_attempts()
          

def ask_question(question):
  # Prompts user to fill in the blank
  # Inputs: question
  # outputs user's answer to question prompt 
  answer = raw_input( '\nFill in for blank ' + question + ':\n' + '--> ')
  return answer

def check_user_answer(correct_answer, user_answer):
  # Checks if user_answer matches the correct_answer
  # Inputs: correct_answer, user_answer
  # Output: True or False
  if (correct_answer == user_answer):
    return True
  else:
    return False

def check_end_questions():
  # Checks if there are any questions left in the game. 
  # If there are none then game is won and paragraph is printed with congratulations prompt
  # Else returns False
  paragraph = quiz['paragraph']
  answers_list_length = len(list(ANSWERS[quiz['difficulty']].items()))
  if quiz['correctCount'] == answers_list_length:
    print paragraph, '\n\nCongratulations, you filled in all blanks correctly!'
    quiz['running'] = False
  else:
    return False


def on_correct_user_answer(question, correct_answer):
  # When user gets question correct this function resets error count, adds 1 to correct count,
  #   replaces question prompt with correct answer and prints new paragraph
  # Inputs: question, and correct_answer
  correct_plus_one = 1
  err_count_restart = 0
  quiz['errorCount'] = err_count_restart  
  paragraph = quiz['paragraph']
  quiz['correctCount'] += correct_plus_one
  # print "quiz['correctCount']:\n", quiz['correctCount']
  quiz['paragraph'] = paragraph.replace(question, correct_answer)
  print "Your paragraph now reads:\n",quiz["paragraph"] 

def on_incorrect_user_answer():
  # When user gets the question incorrect this function adds 1 to the error count
  # prints incorrect prompt with remaining attempts count and reprints paragraph
   max_tries = 5
   errorc_plus_one = 1 #error count + 1 when incorrect
   quiz['errorCount'] = quiz['errorCount'] + errorc_plus_one
   attempts_remaining = str(abs(quiz['errorCount'] - max_tries))
   error_count_num = '\nIncorrect, you have ' + attempts_remaining + ' attempts left!'
   print error_count_num
   print quiz["paragraph"]
   

def too_many_attempts():
  # When the user uses up all attempts this function sets game['running'] to False and
  #   runs question_loop to end game 
  max_tries = 5
  answers_list = sorted(list(ANSWERS[quiz['difficulty']].items()))
  if quiz['errorCount'] == max_tries: # If you exceed max tries then quiz ends
      quiz['running'] = False
      question_loop(answers_list)
      
  

start_quiz()
