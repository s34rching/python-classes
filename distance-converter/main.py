from tkinter import Tk, Button, Label, Entry

window = Tk()
window.title("Miles Distance Converter")
window.minsize(width=250, height=100)
window.config(padx=30, pady=20)


def convert_to_miles():
    user_input = float(distance_input.get())
    converted = round((user_input * 1.609), 2)
    converted_label.config(text=converted)


miles_label = Label(text="miles")
equal_to_label = Label(text="is equal to")
converted_label = Label(text="0")
kilometers_label = Label(text="km")

distance_input = Entry(width=5)

convert_button = Button(text="Convert", command=convert_to_miles)

distance_input.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
equal_to_label.grid(row=1, column=0)
converted_label.grid(row=1, column=1)
kilometers_label.grid(row=1, column=2)
convert_button.grid(row=2, column=1)

window.mainloop()
