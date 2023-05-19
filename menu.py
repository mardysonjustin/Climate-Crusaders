import pygame
from sys import exit


class Menu:
    def run(self, screen):
        font = pygame.font.Font(None, 70)
        title = font.render('Simple Things', False, 'Blue')
        background = pygame.image.load(
            'C:/Users/Mardyson Justin/Documents/Pyg/Graphics/LoFwp.png')
        screen.blit(background, (0, 0))
        screen.blit(title, (300, 200))
        pygame.display.update()
