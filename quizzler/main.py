from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from data import question_data

quiz = QuizBrain(question_data)
quiz_interface = QuizInterface(quiz)
