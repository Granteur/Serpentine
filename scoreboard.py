from turtle import Turtle
CENTER = "center" #alignment for scoreboard
FONT = "Arial", 24, " normal" #font for scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
    
    def update_score(self):
        self.write(f"Score: {self.score}", False, CENTER, FONT)

        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, CENTER, FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, CENTER, FONT)

