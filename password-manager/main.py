from password_generator import generate_password as create_password
from tkinter import Tk, Label, Button, Entry, PhotoImage, Canvas, messagebox
import pyperclip

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
FONT_CONFIG = ("Narkisim", 12, "normal")


def generate_password():
    new_password = create_password(5, 5, 5)
    password_input.delete(0, 'end')
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


def reset_form():
    website_input.delete(0, 'end')
    username_input.delete(0, 'end')
    password_input.delete(0, 'end')


def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    password_row = f"{website} | {username} | {password}\n"

    if len(website) > 0 and len(username) > 0 and len(password) > 0:
        is_confirmed = messagebox.askokcancel("Password Manager",
                                              message=f"Please double-check the password data:\n"
                                                      f"Website: {website}\n"
                                                      f"Username: {username}\n"
                                                      f"Password: {password}\n"
                                                      f"Are you ok with that?")

        if is_confirmed:
            with open('./password-manager/passwords.txt', mode="a") as passwords_file:
                passwords_file.write(password_row)

            reset_form()
    else:
        messagebox.showinfo("Password Manager Error",
                            "Unable to save password. Some of the form data is missing")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

lock_image = PhotoImage(file='./password-manager/logo.png')
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=lock_image)

website_label = Label(text="Website", font=FONT_CONFIG, width=20)
username_label = Label(text="Username", font=FONT_CONFIG, width=20)
password_label = Label(text="Password", font=FONT_CONFIG, width=20)

website_input = Entry(width=40)
username_input = Entry(width=40)
password_input = Entry(width=21)

generate_button = Button(text="Generate password", font=FONT_CONFIG, width=17, command=generate_password)
add_button = Button(text="Add", font=FONT_CONFIG, width=42, command=save_password)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)
username_label.grid(row=2, column=0)
username_input.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

website_input.focus()

window.mainloop()
