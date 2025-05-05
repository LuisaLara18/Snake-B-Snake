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
trash = TrashPile()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(pygame.Color(175, 215, 70))
    apple.draw_apple()
    trash.draw_trash()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
    main()