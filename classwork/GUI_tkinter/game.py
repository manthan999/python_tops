import tkinter as tk
import random
import colorsys

GAME_WIDTH = 1100
GAME_HEIGHT = 750
SPACE_SIZE = 25
SNAKE_SPEED = 90
BODY_PARTS = 5
BG_COLOR = "#000000"

# global restart btn
restart_button = None


# -------- Gradient Color Generator -------- #
def gradient_color(index, total):
    hue = (index / total) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return "#%02x%02x%02x" % (int(r*255), int(g*255), int(b*255))


# -------------- Snake Class ---------------- #
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(self.body_size):
            self.coordinates.append([0, 0])

        self.draw_snake()

    def draw_snake(self):
        for index, (x, y) in enumerate(self.coordinates):
            color = gradient_color(index, len(self.coordinates) + 10)
            square = canvas.create_oval(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=color, outline=""
            )
            self.squares.append(square)

    def update_colors(self):
        for index, square in enumerate(self.squares):
            color = gradient_color(index, len(self.squares) + 10)
            canvas.itemconfig(square, fill=color)


# ---------------- Food Class ---------------- #
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        # Glowing food effect
        self.food = canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill="#ffea00", outline="#ffaa00", width=3
        )


# ---------------- Game Logic ---------------- #
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

    snake.coordinates.insert(0, [x, y])

    color = gradient_color(0, len(snake.coordinates) + 10)
    square = canvas.create_oval(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE,
        fill=color, outline=""
    )
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        canvas.delete(food.food)
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    snake.update_colors()

    if check_collisions(snake):
        game_over()
        return

    window.after(SNAKE_SPEED, next_turn, snake, food)


def change_direction(new_dir):
    global direction
    if new_dir == "left" and direction != "right":
        direction = new_dir
    elif new_dir == "right" and direction != "left":
        direction = new_dir
    elif new_dir == "up" and direction != "down":
        direction = new_dir
    elif new_dir == "down" and direction != "up":
        direction = new_dir


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body in snake.coordinates[1:]:
        if x == body[0] and y == body[1]:
            return True
    return False


def restart_game():
    global snake, food, restart_button, direction
    canvas.delete("all")
    if restart_button:
        restart_button.destroy()

    direction = "right"
    snake = Snake()
    food = Food()
    next_turn(snake, food)


def game_over():
    global restart_button

    canvas.create_text(
        GAME_WIDTH/2,
        GAME_HEIGHT/2 - 50,
        text="GAME OVER",
        fill="red",
        font=("Arial", 60, "bold")
    )

    restart_button = tk.Button(
        window,
        text="RESTART",
        font=("Arial", 20, "bold"),
        bg="white",
        command=restart_game
    )
    restart_button.place(x=GAME_WIDTH/2 - 90, y=GAME_HEIGHT/2 + 20)


# ---------------- MAIN WINDOW ---------------- #
window = tk.Tk()
window.title("Animated Snake Game")
window.resizable(False, False)

direction = "right"

canvas = tk.Canvas(window, bg=BG_COLOR,
                   width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()

snake = Snake()
food = Food()

window.bind("<Left>", lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))
window.bind("<Up>", lambda e: change_direction("up"))
window.bind("<Down>", lambda e: change_direction("down"))

next_turn(snake, food)

window.mainloop()
