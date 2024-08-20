from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.paddle = []
        self.create_paddle(positions)

    def create_paddle(self, positions):
        for position in positions:
            block = Turtle("square")
            block.shape("square")
            block.color("white")
            block.penup()
            block.setposition(position)
            self.paddle.append(block)

    def up(self):
        print(self.paddle[2].ycor())
        if self.paddle[2].ycor() < 240:
            for block in self.paddle:
                block.setheading(90)
                block.forward(60)
    
    def down(self):
        if self.paddle[0].ycor() > -240:
            for block in self.paddle:
                block.setheading(270)
                block.forward(60)

            
        