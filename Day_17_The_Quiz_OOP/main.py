from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for dic in question_data:
    question = Question(dic['text'], dic['answer'])
    question_bank.append(question)

QuizBrain1 = QuizBrain(question_bank)

for question in question_bank:
    if QuizBrain1.next_question():
        print("You got it right!")
    else:
        print("Incorrect!")
    print(QuizBrain1.current_score())