from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.show_score()

    def show_score(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.refresh_score()
        

    def refresh_score(self):
        self.write(f"{self.score_1} {self.score_2}", align="center", font=("Courier", 30, "normal"))
    
    def increase_paddle_1_score(self):
        self.clear()
        self.score_1 += 1
    
    def increase_paddle_2_score(self):
        self.clear()
        self.score_2 += 1
    
    def show_game_over(self):
        self.clear()
        self.write(f"GAME OVER", align="center", font=("Courier", 30, "normal"))