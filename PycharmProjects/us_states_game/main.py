import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()

correct_guesses = []

while len(correct_guesses) != 50:



    if len(correct_guesses) == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ")

    if answer_state == "Exit":
        break

    answer_state = answer_state.title()

    if answer_state in states:
        state_guessed = data[data.state == answer_state]

        coords = (int(state_guessed.x), int(state_guessed.y))

        print(f" These are the {coords}")
        correct_guesses.append(answer_state)

        writer = turtle.Turtle()
        writer.color("RoyalBlue4")
        writer.penup()
        writer.ht()
        writer.goto(coords)

        writer.write(answer_state, align="center", font=("Courier", 8, "bold"))

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name? ")


 # states to learn csv

states_missed = []

for s in states:
    if s not in correct_guesses:
        states_missed.append(s)

d = {
    "States To Review": states_missed
}


review_data = pandas.DataFrame(d)

review_data.to_csv("states_review.csv")




