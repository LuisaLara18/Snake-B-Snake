import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()