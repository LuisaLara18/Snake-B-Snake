import pygame
from pygame.math import Vector2
import random
import sys

class AppleFruit():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_apple(self):
        apple_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(apple, apple_rect)


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


class SecondTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_second_trash(self):
        second_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(second_trash_pile, second_trash_rect)


class ThirdTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_third_trash(self):
        third_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(third_trash_pile, third_trash_rect)


class FourthTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_fourth_trash(self):
        fourth_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(fourth_trash_pile, fourth_trash_rect)


class FifthTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_fifth_trash(self):
        fifth_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(fifth_trash_pile, fifth_trash_rect)


class SixthTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_sixth_trash(self):
        sixth_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(sixth_trash_pile, sixth_trash_rect)


class SeventhTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_seventh_trash(self):
        seventh_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(seventh_trash_pile, seventh_trash_rect)


class EighthTrashPile():

    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_eighth_trash(self):
        eighth_trash_rect = pygame.Rect(self.pos.x * 40, self.pos.y * 40, 40, 40)
        screen.blit(eighth_trash_pile, eighth_trash_rect)


class Snake():

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.new_three_blocks = False
        self.new_five_blocks = False
        self.new_ten_blocks = False
        self.remove_block = False
        self.remove_five_blocks = False
        self.remove_ten_blocks = False
        self.remove_twenty_blocks = False

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

    def add_block(self):
        self.new_block = True

    def add_three_blocks(self):
        self.new_three_blocks = True

    def add_five_blocks(self):
        self.new_five_blocks = True

    def add_ten_blocks(self):
        self.new_ten_blocks = True

    def subtract_block(self):
        self.remove_block = True

    def subtract_five_blocks(self):
        self.remove_five_blocks = True

    def subtract_ten_blocks(self):
        self.remove_ten_blocks = True

    def subtract_twenty_blocks(self):
        self.remove_twenty_blocks = True

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        elif self.new_three_blocks == True:
            body_copy = self.body[:]
            for x in range(3):
                body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_three_blocks = False
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
        elif self.remove_ten_blocks == True:
            body_copy = self.body[:]
            for x in range(10):
                body_copy.pop()
            self.body = body_copy[:]
            self.remove_ten_blocks = False
        elif self.remove_twenty_blocks == True:
            body_copy = self.body[:]
            for x in range(20):
                body_copy.pop()
            self.body = body_copy[:]
            self.remove_twenty_blocks == False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

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


class GamePlay():

    def __init__(self):
        self.snake = Snake()
        self.apple = AppleFruit()
        self.dragonfruit = DragonfruitFruit()
        self.banana = BananaFruit()
        self.blueberry = BlueberryFruit()
        self.trash = TrashPile()
        self.second_trash = SecondTrashPile()
        self.third_trash = ThirdTrashPile()
        self.fourth_trash = FourthTrashPile()
        self.fifth_trash = FifthTrashPile()
        self.sixth_trash = SixthTrashPile()
        self.seventh_trash = SeventhTrashPile()
        self.eighth_trash = EighthTrashPile()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def check_collision(self):
        if self.apple.pos == self.snake.body[0]:
            self.apple.randomize()
            self.snake.add_block()
            for block in self.snake.body[1:]:
                if block == self.apple.pos:
                    self.apple.randomize()
            if self.apple.pos == self.dragonfruit.pos:
                self.apple.randomize()
            if self.apple.pos == self.banana.pos:
                self.apple.randomize()
            if self.apple.pos == self.blueberry.pos:
                self.apple.randomize()
            if self.apple.pos == self.trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.second_trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.third_trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.fourth_trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.fifth_trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.sixth_trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.seventh_trash.pos:
                self.apple.randomize()
            if self.apple.pos == self.eighth_trash.pos:
                self.apple.randomize()
        elif self.dragonfruit.pos == self.snake.body[0]:
            self.dragonfruit.randomize()
            self.snake.add_ten_blocks()
            for block in self.snake.body[1:]:
                if block == self.dragonfruit.pos:
                    self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.apple.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.banana.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.blueberry.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.second_trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.third_trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.fourth_trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.fifth_trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.sixth_trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.seventh_trash.pos:
                self.dragonfruit.randomize()
            if self.dragonfruit.pos == self.eighth_trash.pos:
                self.dragonfruit.randomize()
        elif self.banana.pos == self.snake.body[0]:
            self.banana.randomize()
            self.snake.add_three_blocks()
            for block in self.snake.body[1:]:
                if block == self.banana.pos:
                    self.banana.randomize()
            if self.banana.pos == self.apple.pos:
                self.banana.randomize()
            if self.banana.pos == self.dragonfruit.pos:
                self.banana.randomize()
            if self.banana.pos == self.blueberry.pos:
                self.banana.randomize()
            if self.banana.pos == self.trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.second_trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.third_trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.fourth_trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.fifth_trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.sixth_trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.seventh_trash.pos:
                self.banana.randomize()
            if self.banana.pos == self.eighth_trash.pos:
                self.banana.randomize()
        elif self.blueberry.pos == self.snake.body[0]:
            self.blueberry.randomize()
            self.snake.add_five_blocks()
            for block in self.snake.body[1:]:
                if block == self.blueberry.pos:
                    self.blueberry.randomize()
            if self.blueberry.pos == self.apple.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.dragonfruit.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.banana.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.second_trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.third_trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.fourth_trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.fifth_trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.sixth_trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.seventh_trash.pos:
                self.blueberry.randomize()
            if self.blueberry.pos == self.eighth_trash.pos:
                self.blueberry.randomize()
        elif self.trash.pos == self.snake.body[0]:
            self.trash.randomize()
            self.snake.subtract_five_blocks()
            for block in self.snake.body[1:]:
                if block == self.trash.pos:
                    self.trash.randomize()
            if self.trash.pos == self.apple.pos:
                self.trash.randomize()
            if self.trash.pos == self.dragonfruit.pos:
                self.trash.randomize()
            if self.trash.pos == self.banana.pos:
                self.trash.randomize()
            if self.trash.pos == self.blueberry.pos:
                self.trash.randomize()
            if self.trash.pos == self.second_trash.pos:
                self.trash.randomize()
            if self.trash.pos == self.third_trash.pos:
                self.trash.randomize()
            if self.trash.pos == self.fourth_trash.pos:
                self.trash.randomize()
            if self.trash.pos == self.fifth_trash.pos:
                self.trash.randomize()
            if self.trash.pos == self.sixth_trash.pos:
                self.trash.randomize()
            if self.trash.pos == self.seventh_trash.pos:
                self.trash.randomize()
            if self.trash.pos == self.eighth_trash.pos:
                self.trash.randomize()
        elif self.second_trash.pos == self.snake.body[0]:
            self.second_trash.randomize()
            self.snake.subtract_ten_blocks()
            for block in self.snake.body[1:]:
                if block == self.second_trash.pos:
                    self.second_trash.randomize()
            if self.second_trash.pos == self.apple.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.dragonfruit.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.banana.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.blueberry.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.trash.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.third_trash.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.fourth_trash.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.fifth_trash.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.sixth_trash.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.seventh_trash.pos:
                self.second_trash.randomize()
            if self.second_trash.pos == self.eighth_trash.pos:
                self.second_trash.randomize()
        elif self.third_trash.pos == self.snake.body[0]:
            self.third_trash.randomize()
            self.snake.subtract_block()
            for block in self.snake.body[1:]:
                if block == self.third_trash.pos:
                    self.third_trash.randomize()
            if self.third_trash.pos == self.apple.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.dragonfruit.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.banana.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.blueberry.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.trash.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.second_trash.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.fourth_trash.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.fifth_trash.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.sixth_trash.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.seventh_trash.pos:
                self.third_trash.randomize()
            if self.third_trash.pos == self.eighth_trash.pos:
                self.third_trash.randomize()
        elif self.fourth_trash.pos == self.snake.body[0]:
            self.fourth_trash.randomize()
            self.snake.subtract_five_blocks()
            for block in self.snake.body[1:]:
                if block == self.fourth_trash.pos:
                    self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.apple.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.dragonfruit.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.banana.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.blueberry.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.trash.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.second_trash.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.third_trash.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.fifth_trash.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.sixth_trash.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.seventh_trash.pos:
                self.fourth_trash.randomize()
            if self.fourth_trash.pos == self.eighth_trash.pos:
                self.fourth_trash.randomize()
        elif self.fifth_trash.pos == self.snake.body[0]:
            self.fifth_trash.randomize()
            self.snake.subtract_ten_blocks()
            for block in self.snake.body[1:]:
                if block == self.fifth_trash.pos:
                    self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.apple.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.dragonfruit.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.banana.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.blueberry.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.trash.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.second_trash.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.third_trash.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.fourth_trash.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.sixth_trash.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.seventh_trash.pos:
                self.fifth_trash.randomize()
            if self.fifth_trash.pos == self.eighth_trash.pos:
                self.fifth_trash.randomize()
        elif self.sixth_trash.pos == self.snake.body[0]:
            self.sixth_trash.randomize()
            self.snake.subtract_block()
            for block in self.snake.body[1:]:
                if block == self.sixth_trash.pos:
                    self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.apple.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.dragonfruit.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.banana.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.blueberry.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.trash.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.second_trash.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.third_trash.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.fourth_trash.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.fifth_trash.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.seventh_trash.pos:
                self.sixth_trash.randomize()
            if self.sixth_trash.pos == self.eighth_trash.pos:
                self.sixth_trash.randomize()
        elif self.seventh_trash.pos == self.snake.body[0]:
            self.seventh_trash.randomize()
            self.snake.subtract_five_blocks()
            for block in self.snake.body[1:]:
                if block == self.seventh_trash.pos:
                    self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.apple.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.dragonfruit.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.banana.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.blueberry.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.trash.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.second_trash.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.third_trash.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.fourth_trash.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.fifth_trash.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.sixth_trash.pos:
                self.seventh_trash.randomize()
            if self.seventh_trash.pos == self.eighth_trash.pos:
                self.seventh_trash.randomize()
        elif self.eighth_trash.pos == self.snake.body[0]:
            self.eighth_trash.randomize()
            self.snake.subtract_twenty_blocks()
            for block in self.snake.body[1:]:
                if block == self.eighth_trash.pos:
                    self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.apple.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.dragonfruit.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.banana.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.blueberry.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.trash.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.second_trash.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.third_trash.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.fourth_trash.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.fifth_trash.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.sixth_trash.pos:
                self.eighth_trash.randomize()
            if self.eighth_trash.pos == self.seventh_trash.pos:
                self.eighth_trash.randomize()

    def game_over(self):
        self.snake.reset()

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
        self.dragonfruit.draw_dragonfruit()
        self.banana.draw_banana()
        self.blueberry.draw_blueberry()
        self.trash.draw_trash()
        self.second_trash.draw_second_trash()
        self.third_trash.draw_third_trash()
        self.fourth_trash.draw_fourth_trash()
        self.fifth_trash.draw_fifth_trash()
        self.sixth_trash.draw_sixth_trash()
        self.seventh_trash.draw_seventh_trash()
        self.eighth_trash.draw_eighth_trash()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_second_score()

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

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (255, 255, 255))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        snake_head_rect = snake_head.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(snake_head_rect.left, snake_head_rect.top, snake_head_rect.width + score_rect.width + 6, snake_head_rect.height)
        pygame.draw.rect(screen, (255, 209, 84), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(snake_head, snake_head_rect)
        pygame.draw.rect(screen, (204, 151, 4), bg_rect, 2)

    def draw_second_score(self):
        second_score_text = str(len(self.snake.body) - 3)
        second_score_surface = game_font.render(second_score_text, True, (255, 255, 255))
        second_score_x = int(95)
        second_score_y = int(40)
        second_score_rect = second_score_surface.get_rect(center = (second_score_x, second_score_y))
        snake_head_rect = snake_head.get_rect(midright = (second_score_rect.left, second_score_rect.centery))
        bg_rect = pygame.Rect(snake_head_rect.left, snake_head_rect.top, snake_head_rect.width + second_score_rect.width + 6, snake_head_rect.height)
        pygame.draw.rect(screen, (255, 209, 84), bg_rect)
        screen.blit(second_score_surface, second_score_rect)
        screen.blit(snake_head, snake_head_rect)
        pygame.draw.rect(screen, (204, 151, 4), bg_rect, 2)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

apple = pygame.image.load('AppleFruit.png').convert_alpha()
trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
second_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
third_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
fourth_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
fifth_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
sixth_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
seventh_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
eighth_trash_pile = pygame.image.load('TrashPile.png').convert_alpha()
dragonfruit = pygame.image.load('DragonfruitFruit.png').convert_alpha()
banana = pygame.image.load('BananaFruit.png').convert_alpha()
blueberry = pygame.image.load('BlueberryFruit.png').convert_alpha()
game_font = pygame.font.Font('KOMIKAX_.ttf', 25)
snake_head = pygame.image.load('SnakeHeadBottom.png').convert_alpha()

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