import pygame
from pygame.math import Vector2
import random
import sys

class AppleFruit():

    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_apple(self):
        apple_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        pygame.draw.rect(screen, (126, 166, 114) , apple_rect)


class DragonfruitFruit():

    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_dragonfruit(self):
        dragonfruit_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        pygame.draw.rect(screen, (255, 0, 255), dragonfruit_rect)


class BananaFruit():

    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_banana(self):
        banana_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        pygame.draw.rect(screen, (255, 255, 224), banana_rect)


class BlueberryFruit():

    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_blueberry(self):
        blueberry_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        pygame.draw.rect(screen, (45, 63, 255), blueberry_rect)


class TrashPile():

    def __init__(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_trash(self):
        trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        pygame.draw.rect(screen, (128, 128, 128), trash_rect)


class Snake():

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * 40, block.y * 40, 40, 40)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

apple = AppleFruit()
dragonfruit = DragonfruitFruit()
banana = BananaFruit()
blueberry = BlueberryFruit()
trash = TrashPile()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
        
    screen.fill(pygame.Color(175, 215, 70))

    apple.draw_apple()
    dragonfruit.draw_dragonfruit()
    banana.draw_banana()
    blueberry.draw_blueberry()
    trash.draw_trash()
    snake.draw_snake()

    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
    main()