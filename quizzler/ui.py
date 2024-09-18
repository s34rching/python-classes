from tkinter import Tk, Button, Label, Canvas, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_CONFIG = ("Arial", 20, "italic")
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.listener = None

        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            font=("Arial", 15, "normal"),
            bg=THEME_COLOR,
            fg="white"
        )

        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.question_text = self.canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            text="Question Text",
            font=FONT_CONFIG,
            width=280
        )

        true_image = PhotoImage(file="./quizzler/images/true.png")
        false_image = PhotoImage(file="./quizzler/images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.submit_true)
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.submit_false)

        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.has_questions():
            if self.listener is not None:
                self.window.after_cancel(self.listener)

            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            question = self.quiz.next_question()
            question_t = self.quiz.format_question(question)

            self.canvas.itemconfig(self.question_text, text=question_t)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've reached out the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_answer_correct):
        if is_answer_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def submit_true(self):
        is_correct = self.quiz.check_answer('True')
        self.give_feedback(is_correct)
        self.listener = self.window.after(1000, self.next_question)

    def submit_false(self):
        is_correct = self.quiz.check_answer('False')
        self.give_feedback(is_correct)
        self.listener = self.window.after(1000, self.next_question)
