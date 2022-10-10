from turtle import Turtle


class Variable(Turtle):

    # Initializes class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.all_states = []
        self.hideturtle()
        self.penup()

    # Every time a state is created the score goes up, turtle is hidden, pen is up, and goes to position with name made.
    def create_state(self, position, name):
        self.score += 1
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(position)
        new_state.write(f"{name}")
        self.all_states.append(new_state)
