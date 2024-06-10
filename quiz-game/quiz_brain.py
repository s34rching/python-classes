from question import Question
import random


def check_answer(question, user_answer):
    return user_answer == question.answer


def create_question_bank(questions_data):
    question_bank = []

    for question_item in questions_data:
        question_bank.append(Question(question_item["text"], question_item["answer"]))

    return question_bank


def print_answer(question):
    print(f"The correct answer is: {question.answer}")


class QuizBrain:
    def __init__(self, questions):
        self.index = 0
        self.display_number = 0
        self.score = 0
        self.questions = create_question_bank(questions)

    def print_question(self, question):
        return f"Q.{self.display_number}: {question.text} (True/False)?: "

    def print_score(self):
        print(f"Your current score is: {self.score}/{self.display_number}")

    def has_questions(self):
        return len(self.questions) > 0

    def next_question(self):
        index = random.randint(0, len(self.questions) - 1)
        self.index = index
        self.display_number += 1

        question = self.questions[index]
        self.questions.pop(index)

        return question

    def get_user_answer(self, question):
        return (input(self.print_question(question))).title()

    def play(self):
        while self.has_questions():
            question = self.next_question()
            user_answer = self.get_user_answer(question)

            if check_answer(question, user_answer):
                print("You've got it")
                self.score += 1
            else:
                print("Unfortunately...")

            print_answer(question)
            self.print_score()

            if not self.has_questions():
                print("\nYou've completed a quiz!")
                self.print_score()
