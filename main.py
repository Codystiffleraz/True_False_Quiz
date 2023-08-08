from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# Loops through dictionary and adds each input to a question bank
for dic in question_data:
    question_bank.append(Question(dic['question'], dic['correct_answer']))
        
quiz = QuizBrain(question_bank)

# Runs the quiz
while quiz.still_has_questions():
    quiz.next_question()
  
# Prints final score  
quiz.completed()

