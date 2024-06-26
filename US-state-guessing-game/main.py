import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725,height=491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        # missing_states = []
        # for states in all_states:
        #     if states not in guessed_state:
        #         missing_states.append(states)
        df = pandas.DataFrame(missing_states)
        df.to_csv("States to learn.csv")
        #print(missing_states)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x),int(state_data.y))
        tim.write(answer_state)
        #tim.write(state_data.state.item())

#states_to_learn.csv


screen.exitonclick()
