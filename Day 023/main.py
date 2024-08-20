import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()




screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.show_game_over()

    if player.has_finished_race():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()