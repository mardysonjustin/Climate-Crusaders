import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/WALL.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/DOOR.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Chain(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/CHAIN.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Chand(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/CHAND.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Window1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/WINDOW_1.png')
        self.rect = self.image.get_rect(bottomleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Window2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/WINDOW_2.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Water(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/WATER.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Water1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks4/WATER1.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
