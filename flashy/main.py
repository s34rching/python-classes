from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random

FRENCH = "French"
ENGLISH = "English"
CARD_WIDTH = 800
CARD_HEIGHT = 526
BACKGROUND_COLOR = "#b1ddc6"

card_flip = None
words_list = []
current_word = {}


def get_words_data():
    global words_list

    try:
        data = pandas.read_csv("./flashy/data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("./flashy/data/french_words.csv")
    words_list = [{ENGLISH: row.English, FRENCH: row.French} for (_, row) in data.iterrows()]


def update_words_to_learn():
    global words_list

    words_list.remove(current_word)
    updated_data = pandas.DataFrame(words_list)
    updated_data.to_csv('./flashy/data/words_to_learn.csv', columns=[FRENCH, ENGLISH], index=False)


def flip_card():
    global current_word

    card_canvas.itemconfig(card_image, image=back_card_image)
    card_canvas.itemconfig(language_label, text=ENGLISH, fill="white")
    card_canvas.itemconfig(word_label, text=current_word[ENGLISH], fill="white")


def draw_random_word():
    global current_word
    global card_flip

    if card_flip is not None:
        window.after_cancel(card_flip)

    current_word = random.choice(words_list)
    card_canvas.itemconfig(card_image, image=front_card_image)
    card_canvas.itemconfig(language_label, text=FRENCH, fill="black")
    card_canvas.itemconfig(word_label, text=current_word[FRENCH], fill="black")

    card_flip = window.after(3000, flip_card)


def set_word_known():
    update_words_to_learn()
    draw_random_word()


get_words_data()


window = Tk()
window.config(padx=50, pady=50, bg="#b1ddc6")
window.title("Flashy")

front_card_image = PhotoImage(file="./flashy/images/card_front.png")
back_card_image = PhotoImage(file="./flashy/images/card_back.png")
card_canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = card_canvas.create_image(CARD_WIDTH / 2, CARD_HEIGHT / 2, image=front_card_image)
language_label = card_canvas.create_text(CARD_WIDTH / 2, 150, text=FRENCH, font=("Arial", 40, "italic"))
word_label = card_canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 2, text="word", font=("Arial", 60, "bold"))

right_image = PhotoImage(file="./flashy/images/right.png")
wrong_image = PhotoImage(file="./flashy/images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=set_word_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=draw_random_word)

card_canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

draw_random_word()

window.mainloop()
