import turtle;
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape('blank_states_img.gif') # add this first to use this image as shape in turtle
turtle.shape("blank_states_img.gif")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

states_data = pandas.read_csv('50_states.csv')

guessed_states = []


while len(guessed_states) < 50:
    guess = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name").title()
    if guess == "Exit":
        missed_states = [state for state in states_data.state.to_list() if state not in guessed_states]

        state_dict = {
            'Missed States': missed_states
        }

        missed_state_df = pandas.DataFrame(state_dict)

        missed_state_df.to_csv('missed_states.csv')
        break  
    if guess in states_data.state.to_list():
        guessed_states.append(guess)
        state_row = states_data[states_data.state == guess]
        state_x = state_row["x"]
        state_y = state_row["y"]
        print(int(state_x), int(state_y))
        pen.goto(int(state_x), int(state_y))
        pen.write(guess)


