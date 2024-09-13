from tkinter import Tk, Button, Label, Canvas, PhotoImage
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_HEIGHT = 230
CANVAS_WIDTH = 210
CHECKMARK = "✔"
TIMER_DELAY = 1000
INITIAL_TIMER_VALUE = "00:00"
INITIAL_TITLE_TEXT = "Pomodoro"
step_number = 1
progress_text = ""
session_counter = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def transform_time(seconds):
    def add_leading_zero(stringified):
        return "{:02d}".format(stringified)

    return f"{add_leading_zero(math.floor(seconds / 60))}:{add_leading_zero(seconds % 60)}"


def set_session_completed():
    global progress_text

    progress_text += CHECKMARK
    progress_label.config(text=progress_text)


def start_timer():
    global step_number
    global progress_text

    start_button.config(state="disabled")

    if step_number < 9:
        if step_number == 8:
            loop_time_min = LONG_BREAK_MIN
            title_label.config(text="Break", fg=RED)
        elif step_number % 2 == 0:
            loop_time_min = SHORT_BREAK_MIN
            title_label.config(text="Break", fg=PINK)
        else:
            loop_time_min = WORK_MIN
            title_label.config(text="Work", fg=GREEN)

        loop_time_sec = loop_time_min * 60
        loop_time_ms = loop_time_sec * 1000

        if step_number % 2 != 0:
            window.after(loop_time_ms, set_session_completed)

        countdown(loop_time_sec)
        window.after(loop_time_ms + TIMER_DELAY, start_timer)
        step_number += 1


def reset_timer():
    global step_number
    global progress_text

    window.after_cancel(session_counter)

    start_button.config(state="normal")

    step_number = 1
    progress_text = ""
    progress_label.config(text=progress_text)
    title_label.config(text=INITIAL_TITLE_TEXT, fg=RED)
    canvas.itemconfig(countdown_text, text=INITIAL_TIMER_VALUE)


def countdown(count):
    global session_counter

    canvas.itemconfig(countdown_text, text=transform_time(count))
    if count > 0:
        session_counter = window.after(1000, countdown, count - 1)


window = Tk()
window.config(padx=75, pady=50, bg=YELLOW)
window.title("Pomodoro")
window.minsize(width=400, height=400)

tomato_image = PhotoImage(file="./pomodoro/tomato.png")
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_image)
countdown_text = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 20, text=INITIAL_TIMER_VALUE, fill="white",
                                    font=(FONT_NAME, 35, "normal"))

title_label = Label(text=INITIAL_TITLE_TEXT, bg=YELLOW, fg=RED, font=(FONT_NAME, 40, "bold"))
start_button = Button(text="Start", font=(FONT_NAME, 14, "normal"), highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="Reset", font=(FONT_NAME, 14, "normal"), highlightbackground=YELLOW, command=reset_timer)
progress_label = Label(text=progress_text, bg=YELLOW, fg=GREEN)

title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
progress_label.grid(row=3, column=1)

window.mainloop()
