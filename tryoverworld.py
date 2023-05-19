import pygame
from sys import exit


class LevelSelect:

    def run(self, screen):
        background = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/menu.png')
        screen.blit(background, (0, 0))
        pygame.display.update()

    def homerun(self, screen):
        background = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/home.png')
        screen.blit(background, (0, 0))
        pygame.display.update()
