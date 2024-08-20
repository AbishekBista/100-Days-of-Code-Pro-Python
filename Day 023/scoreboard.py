from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f'Level: {self.score}', align="center", font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def show_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
