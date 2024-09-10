import pandas
from state_name import StateName
from turtle import Turtle, Screen

states_image = "./states/blank_states_img.gif"

screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.addshape(states_image)

turtle = Turtle()
turtle.shape(states_image)

states_data = pandas.read_csv("./states/50_states.csv")
all_states = states_data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    title = ""

    if len(guessed_states) > 0:
        title = f"{len(guessed_states)}/50 States Correct"
    else:
        title = "Guess the state"

    user_guess = screen.textinput(title, "Guess another one state name:")
    state_name = str.title(user_guess)

    if state_name == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        states_to_learn = pandas.DataFrame({"States": missing_states})
        states_to_learn.to_csv("./states/states_to_learn.csv", mode="w")

        break

    found_state = states_data[states_data["state"] == state_name]

    if len(found_state) == 1 and state_name not in guessed_states:
        x_cor = found_state["x"].item()
        y_cor = found_state["y"].item()

        guessed_states.append(state_name)

        StateName(state_name, x_cor, y_cor)
