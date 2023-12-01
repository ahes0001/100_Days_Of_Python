# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're the ed of the quiz

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number-1].text} (True/False)?: ")
        if user_answer == self.question_list[self.question_number-1].answer:
            self.score += 1
            return True
        else:

            return False


    def current_score(self):
        return f"Your current score is: {self.score}/{self.question_number}\n"


    def correct_answer(self):
        return self.question_list[self.question_number-1].answer

