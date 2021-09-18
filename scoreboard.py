from io import FileIO
from turtle import Turtle
CENTER = "center" #alignment for scoreboard
FONT = "Arial", 24, " normal" #font for scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, CENTER, FONT)

        
    def keep_score(self):
        self.score += 1
        self.update_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    
    #create/modify a text file to house the high score
    def save_game(self):
        with open("data.txt", mode="w") as highscore:
            FileIO.write(self.high_score)

    """ def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, CENTER, FONT) """

