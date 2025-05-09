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
        self.new_five_blocks = False
        self.new_ten_blocks = False
        self.remove_block = False
        self.remove_five_blocks = False

        self.head_up = pygame.image.load('SnakeHeadTop.png').convert_alpha()
        self.head_down = pygame.image.load('SnakeHeadBottom.png').convert_alpha()
        self.head_right = pygame.image.load('SnakeHeadRight.png').convert_alpha()
        self.head_left = pygame.image.load('SnakeHeadLeft.png').convert_alpha()

        self.tail_up = pygame.image.load('SnakeTailTop.png').convert_alpha()
        self.tail_down = pygame.image.load('SnakeTailBottom.png').convert_alpha()
        self.tail_right = pygame.image.load('SnakeTailRight.png').convert_alpha()
        self.tail_left = pygame.image.load('SnakeTailLeft.png').convert_alpha()

        self.body_vertical = pygame.image.load('SnakeBodyTopBottom.png').convert_alpha()
        self.body_horizontal = pygame.image.load('SnakeBodyLeftRight.png').convert_alpha()

        self.body_turntr = pygame.image.load('SnakeTurnRight.png').convert_alpha()
        self.body_turntl = pygame.image.load('SnakeTurnLeft.png').convert_alpha()
        self.body_turnbl = pygame.image.load('SnakeTurnBottom.png').convert_alpha()
        self.body_turnbr = pygame.image.load('SnakeTurnTop.png').convert_alpha()

        self.customize_head_up = pygame.image.load('ColoredSnakeHeadTop.png').convert_alpha()
        self.customize_head_down = pygame.image.load('ColoredSnakeHeadBottom.png').convert_alpha()
        self.customize_head_right = pygame.image.load('ColoredSnakeHeadRight.png').convert_alpha()
        self.customize_head_left = pygame.image.load('ColoredSnakeHeadLeft.png').convert_alpha()

        self.customize_tail_up = pygame.image.load('ColoredSnakeTailTop.png').convert_alpha()
        self.customize_tail_down = pygame.image.load('ColoredSnakeTailBottom.png').convert_alpha()
        self.customize_tail_right = pygame.image.load('ColoredSnakeTailRight.png').convert_alpha()
        self.customize_tail_left = pygame.image.load('ColoredSnakeTailLeft.png').convert_alpha()

        self.customize_body_vertical = pygame.image.load('ColoredSnakeBodyTopBottom.png').convert_alpha()
        self.customize_body_horizontal = pygame.image.load('ColoredSnakeBodyLeftRight.png').convert_alpha()

        self.customize_body_turntr = pygame.image.load('ColoredSnakeTurnRight.png').convert_alpha()
        self.customize_body_turntl = pygame.image.load('ColoredSnakeTurnLeft.png').convert_alpha()
        self.customize_body_turnbl = pygame.image.load('ColoredSnakeTurnBottom.png').convert_alpha()
        self.customize_body_turnbr = pygame.image.load('ColoredSnakeTurnTop.png').convert_alpha()
                                                    

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        elif self.new_five_blocks == True:
            body_copy = self.body[:]
            for x in range(5):
                body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_five_blocks = False
        elif self.new_ten_blocks == True:
            body_copy = self.body[:]
            for x in range(10):
                body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_ten_blocks = False
        elif self.remove_block == True:
            body_copy = self.body[:]
            body_copy.pop()
            self.body = body_copy[:]
            self.remove_block = False
        elif self.remove_five_blocks == True:
            body_copy = self.body[:]
            for x in range(5):
                body_copy.pop()
            self.body = body_copy[:]
            self.remove_five_blocks = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def add_five_blocks(self):
        self.new_five_blocks = True

    def add_ten_blocks(self):
        self.new_ten_blocks = True

    def subtract_block(self):
        self.remove_block = True

    def subtract_five_blocks(self):
        self.remove_five_blocks = True

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * 40)
            y_pos = int(block.y * 40)
            block_rect = pygame.Rect(x_pos, y_pos, 40, 40)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else: 
                previous_block = self.body[index +1] - block
                next_block = self.body[index -1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1:
                        screen.blit(self.body_turntl, block_rect)
                    elif previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_turntl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1:
                        screen.blit(self.body_turnbl, block_rect)
                    elif previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_turnbl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1:
                        screen.blit(self.body_turntr, block_rect)
                    elif previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_turntr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1:
                        screen.blit(self.body_turnbr, block_rect)
                    elif previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_turnbr, block_rect)

    def customize_update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.customize_head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.customize_head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.customize_head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.customize_head_down

    def customize_update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.customize_tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.customize_tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.customize_tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.customize_tail_up

    def customize_snake(self):
        self.customize_update_head_graphics()
        self.customize_update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * 40)
            y_pos = int(block.y * 40)
            block_rect = pygame.Rect(x_pos, y_pos, 40, 40)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else: 
                previous_block = self.body[index +1] - block
                next_block = self.body[index -1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.customize_body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.customize_body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1:
                        screen.blit(self.customize_body_turntl, block_rect)
                    elif previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.customize_body_turntl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1:
                        screen.blit(self.customize_body_turnbl, block_rect)
                    elif previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.customize_body_turnbl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1:
                        screen.blit(self.customize_body_turntr, block_rect)
                    elif previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.customize_body_turntr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1:
                        screen.blit(self.customize_body_turnbr, block_rect)
                    elif previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.customize_body_turnbr, block_rect)


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
            self.snake.add_ten_blocks()
        if self.banana.pos == self.snake.body[0]:
            self.banana.randomize()
            self.snake.subtract_block()
        if self.blueberry.pos == self.snake.body[0]:
            self.blueberry.randomize()
            self.snake.add_five_blocks()
        if self.trash.pos == self.snake.body[0]:
            self.trash.randomize()
            self.snake.subtract_five_blocks()

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
        self.draw_grass()
        self.apple.draw_apple()
        self.snake.draw_snake()
        self.dragonfruit.draw_dragonfruit()
        self.banana.draw_banana()
        self.blueberry.draw_blueberry()
        self.trash.draw_trash()

    def draw_grass(self):
        grass_color = (69, 5, 40)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

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
game_font = pygame.font.Font('KOMIKAX_.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = GamePlay()

def main():
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
            
        screen.fill(pygame.Color(23, 3, 17))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()