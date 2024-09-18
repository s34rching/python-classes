import random
import html


def print_answer(question):
    print(f"The correct answer is: {question.answer}")


class QuizBrain:
    def __init__(self, questions):
        self.current_question = None
        self.index = 0
        self.display_number = 0
        self.score = 0
        self.questions = questions

    def format_question(self, question):
        return f"Q.{self.display_number}: {html.unescape(question['question'])}"

    def print_score(self):
        print(f"Your current score is: {self.score}/{self.display_number}")

    def has_questions(self):
        return len(self.questions) > 0

    def next_question(self):
        index = random.randint(0, len(self.questions) - 1)
        self.index = index
        self.display_number += 1

        self.current_question = self.questions[index]
        self.questions.pop(index)

        return self.current_question

    def get_user_answer(self, question):
        return input(self.format_question(question)).title()

    def check_answer(self, answer):
        is_correct = self.current_question['correct_answer'] == answer.title()

        if is_correct:
            self.score += 1

        return is_correct

    def play(self):
        while self.has_questions():
            question = self.next_question()
            answer = self.get_user_answer(question)

            if self.check_answer(answer):
                print("You've got it")
            else:
                print("Unfortunately...")

            print_answer(question)
            self.print_score()

            if not self.has_questions():
                print("\nYou've completed a quiz!")
                self.print_score()
