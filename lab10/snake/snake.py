import pygame
import random
import time
from database import get_user, create_user, save_score  # подключаем функции из database.py

# Ввод имени пользователя
username = input("Enter your username: ")
user = get_user(username)
if user:
    user_id = user[0]
    print(f"Welcome back, {username}!")
else:
    user_id = create_user(username)
    print(f"Hello, new user {username}!")

pygame.init()

# screen sizes and setting screen
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 20

# font option
font_go = pygame.font.SysFont("Times New Roman", 72)
text_go = font_go.render("Game Over", True, "red")
font_s_l = pygame.font.SysFont("Times New Roman", 24)
font_food_weight = pygame.font.SysFont("Times New Roman", 18)

def draw_grid(color):
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, color, (i * CELL, j * CELL, CELL, CELL), 1)

def display_attribute(score, level):
    font_s_l = pygame.font.SysFont("Times New Roman", 18)
    text_sc = font_s_l.render(f" Score {score} ", True, "black", "white")
    text_lv = font_s_l.render(f" Level {level} ", True, "black", "white")
    screen.blit(text_sc, (3, 3))
    screen.blit(text_lv, (text_sc.get_width() + 5, 3))

def game_over(score, level):
    text_sc = font_s_l.render(f"Score {score}", True, "black")
    text_lv = font_s_l.render(f"Level {level}", True, "black")
    screen.fill("gray")
    screen.blit(text_go, ((WIDTH - text_go.get_width()) // 2, HEIGHT // 2 - text_go.get_height()))
    screen.blit(text_lv, ((WIDTH - text_lv.get_width()) // 2, HEIGHT // 2))
    screen.blit(text_sc, ((WIDTH - text_sc.get_width()) // 2, HEIGHT // 2 + text_sc.get_height()))
    pygame.display.flip()
    time.sleep(3)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.score = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

        if self.direction == "RIGHT":
            self.body[0].x += 1
        if self.direction == "LEFT":
            self.body[0].x -= 1
        if self.direction == "DOWN":
            self.body[0].y += 1
        if self.direction == "UP":
            self.body[0].y -= 1

        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, (255, 102, 0), (head.x * CELL, head.y * CELL, CELL, CELL), 0, 2)
        for segment in self.body[1:]:
            pygame.draw.rect(screen, (255, 204, 0), (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 1)
    
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += food.weight
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)
            food.random_weight()
        
    def check_collision_body(self, food):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x != food.pos.x and head.y == segment.y != food.pos.y:
                return True

class Food:
    def __init__(self):
        self.pos = Point(9, 9)
        self.weight = random.randint(1, 5)

    def draw(self):
        pygame.draw.rect(screen, "lightgreen", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), 0, 10)

    def generate_random_pos(self, body):
        self.pos.x = random.randint(1, WIDTH // CELL - 2)
        self.pos.y = random.randint(1, HEIGHT // CELL - 2)
        for i in range(len(body)):
            if body[i].x == self.pos.x and body[i].y == self.pos.y:
                self.generate_random_pos(body)
        pygame.time.set_timer(FOOD_TIME_EVENT, 5000)

    def random_weight(self):
        self.weight = random.randint(1, 5)

FOOD_TIME_EVENT = pygame.USEREVENT + 1

class Level:
    def __init__(self):
        self.num = 1
    
    def check_score(self, snake):
        if snake.score >= 10 and snake.score < 20:
            self.num = 2
        elif snake.score >= 20:
            self.num = 3
        
    def levels(self, snake, food):
        if self.num == 2:
            screen.fill("gray")
            head = snake.body[0]
            pygame.draw.rect(screen, (48, 45, 255), (head.x * CELL, head.y * CELL, CELL, CELL), 0, 2)
            for segment in snake.body[1:]:
                pygame.draw.rect(screen, (84, 154, 255), (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 1)
            pygame.draw.rect(screen, "yellow", (food.pos.x * CELL, food.pos.y * CELL, CELL, CELL), 0, 10)
        else:
            screen.fill((255, 193, 119))
            head = snake.body[0]
            pygame.draw.rect(screen, (222, 30, 86), (head.x * CELL, head.y * CELL, CELL, CELL), 0, 2)
            for segment in snake.body[1:]:
                pygame.draw.rect(screen, (255, 82, 40), (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 1)
            pygame.draw.rect(screen, "violet", (food.pos.x * CELL, food.pos.y * CELL, CELL, CELL), 0, 10)

    def speed(self):
        if self.num == 2:
            FPS = 7
        elif self.num == 3:
            FPS = 10
        else:
            FPS = 5
        return FPS

# --- Создание объектов ---
food = Food()
snake = Snake()
level = Level()
clock = pygame.time.Clock()

# --- Основной игровой цикл ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                snake.change_to = "LEFT"
            elif event.key == pygame.K_DOWN:
                snake.change_to = "DOWN"
            elif event.key == pygame.K_UP:
                snake.change_to = "UP"
            elif event.key == pygame.K_p:
                print("Game paused and saved!")
                save_score(user_id, snake.score, level.num)

        if event.type == FOOD_TIME_EVENT:
            food.generate_random_pos(snake.body)

    screen.fill("black")
    draw_grid("black")
    snake.move()

    if snake.check_collision_body(food):
        running = False
        game_over(snake.score, level.num)

    snake.check_collision(food)
    level.check_score(snake)

    if level.num == 1:
        snake.draw()
        food.draw()
    else:
        level.levels(snake, food)

    text_food_weight = font_food_weight.render(f"{food.weight}", True, "red") 
    screen.blit(text_food_weight, (food.pos.x * CELL + 5, food.pos.y * CELL))
    FPS = level.speed()
    display_attribute(snake.score, level.num)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

