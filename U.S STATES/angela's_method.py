import pandas
import turtle

# create screen and add background
screen = turtle.Screen()
screen.title("U.S. States Game")

# this is how to set a background image onto a screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?"
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_missed.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
