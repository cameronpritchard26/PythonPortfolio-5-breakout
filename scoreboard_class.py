from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.score = 0
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(200, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.write(f"Level: {self.level} Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, added_score) -> None:
        self.score += added_score
        self.update_scoreboard()
    
    def level_up(self) -> None:
        self.level += 1
        self.update_scoreboard()