# Snake

from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH/SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT/SPACE_SIZE) - 1)) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food): 
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))  # INsert into the beginning of the list

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        
        global score
        
        score += 1
        
        label.config(text = "Score : {}".format(score))

        canvas.delete("food") # Deleting using tag "food". We can also do this using object name canvas.delete(food). Here food is the object.

        food = Food()

    else:

        del snake.coordinates[-1]  # Delete the last coordinates
        canvas.delete(snake.squares[-1])  # Delete the last squares in the list
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        root.after(SPEED, next_turn, snake, food)

def change_direction(newDirection):

    global direction

    if newDirection == "left":
        if direction != "right":
            direction = newDirection
    elif newDirection == "right":
        if direction != "left":
            direction = newDirection
    elif newDirection == "up":
        if direction != "down":
            direction = newDirection
    elif newDirection == "down":
        if direction != "up":
            direction = newDirection

def check_collisions(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font = ("consolas", 70), text = "GAME OVER !", fill = "red")


root = Tk()
root.title("Snake Game")
root.resizable(False, False)

score = 0
direction = "down"

label = Label(root, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

root.update()

win_width = root.winfo_width()
win_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (win_width/2))
y = int((screen_height / 2) - (win_height/2))

root.geometry(f"{win_width}x{win_height}+{x}+{y}")

root.bind('<Left>', lambda event: change_direction("left"))
root.bind('<Right>', lambda event: change_direction("right"))
root.bind('<Up>', lambda event: change_direction("up"))
root.bind('<Down>', lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

root.mainloop()