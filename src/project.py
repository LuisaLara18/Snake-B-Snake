import pygame
from pygame.math import Vector2
import random
import sys
import time

class AppleFruit():

    def __init__(self):
        self.randomize()
        self.start_time = time.time()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def timer(self):
        if time.time() - self.start_time >= 4:
            self.kill()

    def draw_apple(self):
        apple_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(apple, apple_rect)
        # pygame.draw.rect(screen, (126, 166, 114) , apple_rect)


class DragonfruitFruit():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_dragonfruit(self):
        dragonfruit_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(dragonfruit, dragonfruit_rect)
        # pygame.draw.rect(screen, (255, 0, 255), dragonfruit_rect)


class BananaFruit():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_banana(self):
        banana_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(banana, banana_rect)
        # pygame.draw.rect(screen, (255, 255, 224), banana_rect)


class BlueberryFruit():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_blueberry(self):
        blueberry_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(blueberry, blueberry_rect)
        # pygame.draw.rect(screen, (45, 63, 255), blueberry_rect)


class TrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_trash(self):
        trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(trash_pile, trash_rect)
        # pygame.draw.rect(screen, (128, 128, 128), trash_rect)


class Snake():

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.remove_block = False

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        if self.remove_block == True:
            body_copy = self.body[:]
            body_copy.pop()
            self.body = body_copy[:]
            self.remove_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def subtract_block(self):
        self.remove_block = True

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * 40, block.y * 40, 40, 40)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)


class GamePlay():

    def __init__(self):
        self.snake = Snake()
        self.apple = AppleFruit()
        self.dragonfruit = DragonfruitFruit()
        self.banana = BananaFruit()
        self.blueberry = BlueberryFruit()
        self.trash = TrashPile()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def check_collision(self):
        if self.apple.pos == self.snake.body[0]:
            self.apple.randomize()
            self.snake.add_block()
        if self.dragonfruit.pos == self.snake.body[0]:
            self.dragonfruit.randomize()
        if self.banana.pos == self.snake.body[0]:
            self.banana.randomize()
        if self.blueberry.pos == self.snake.body[0]:
            self.blueberry.randomize()
        if self.trash.pos == self.snake.body[0]:
            self.trash.randomize()
            self.snake.subtract_block()

    def game_over():
        pygame.quit()
        sys.exit()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < 20:
            self.game_over()
        if not 0 <= self.snake.body[0].y < 20:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_elements(self):
        self.apple.draw_apple()
        self.snake.draw_snake()
        self.dragonfruit.draw_dragonfruit()
        self.banana.draw_banana()
        self.blueberry.draw_blueberry()
        self.trash.draw_trash()


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

apple = pygame.image.load('AppleFruit.png').convert_alpha()
trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
dragonfruit = pygame.image.load('DragonfruitFruit.png').convert_alpha()
banana = pygame.image.load('BananaFruit.png').convert_alpha()
blueberry = pygame.image.load('BlueberryFruit.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = GamePlay()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
        
    screen.fill(pygame.Color(175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
    main()