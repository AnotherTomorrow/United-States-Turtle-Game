import turtle
from turtle import Turtle, Screen
# from states import Variable
import pandas

screen = Screen()
screen.title("Name The States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# Reads the data in CSV file and saves it as a variable.
data = pandas.read_csv("50_states.csv")
# Creates all_states into a list with all states in 50_states CSV file.
all_states = data.state.to_list()
correct_guesses = []

# While the amount of correct_guesses aren't over 50 continue the game.
while len(correct_guesses) < 50:
    # Creates a text input box asking user for a state. It's title also handles the score.
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt=f"Name a state!").title()

    # If the user decides to type in "Exit" the script saves all missing states into a list and saves it in a CSV file.
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        save = pandas.DataFrame(missing_states)
        save.to_csv("states_to_learn.csv")
        break

    # If the state answer is correct, it will append it to correct_guesses, create a turtle, and send it to the state.
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        state_data = data[data.state == answer_state]
        tom.goto(int(state_data.x), int(state_data.y))
        tom.write(answer_state)
