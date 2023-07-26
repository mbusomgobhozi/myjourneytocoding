import pandas
import turtle

# create screen and add background
screen = turtle.Screen()
screen.title("U.S. States Game")

# this is how to set a background image onto a screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# need to create a new turtle
guess = turtle.Turtle()
guess.hideturtle()
guess.penup()
# set the game to true so it may keep running in the while loop
game_is_on = True

while game_is_on:
    # create a dictionary for guesses
    guesses = []
    # score
    score = 0
    # ask user for their input screen prompt
    answer_state = screen.textinput(
        title="Guess the state", prompt="Guess A State"
    ).title()

    # read the csv file and convert to a dictionary
    data = pandas.read_csv("50_states.csv")
    data_dict = data.to_dict()

    # I could've use data[data['state'] == data[answer_state]]
    # loop through the file to find the x and y coords especially if the guess is correct
    for index in range(0, len(data_dict["state"])):
        if data_dict["state"][index] == answer_state:
            x = data_dict["x"][index]
            y = data_dict["y"][index]
            # add the guess to the dictionary to check later if they have guessed it or not
            guesses.append(answer_state)
            score += 1
    # send the guessed answer to their respective co-ordinates
    guess.goto(x, y)
    guess.write(f"{answer_state}")

    # the above works funny enough, but after the first correct I kind of need the title to change
    while score < 50:
        answer_state = screen.textinput(
            title=f"{score}/50 States Correct", prompt="Guess A State"
        ).title()

        for index in range(0, len(data_dict["state"])):
            if data_dict["state"][index] == answer_state:
                x = data_dict["x"][index]
                y = data_dict["y"][index]
                # add the guess to the dictionary to check later if they have guessed it or not
                guesses.append(answer_state)
                score += 1
                # now that we have the y and x axis we need to write it onto the screen
                guess.goto(x, y)
                guess.write(f"{answer_state}")
        if answer_state == "Exit":
            states = data.state.to_list()
            # shortened the code by a few lines all good using list comprehension
            missing_states = [state for state in states if state not in guesses]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv", index=False)
            score = 51
        # game rules
        if len(guesses) == len(data_dict["state"]):
            screen.write(
                f"You Guessed All The States: {score}/50",
                align="centre",
                font="Courier",
            )
            score = 51

    if score == 51:
        game_is_on = False
