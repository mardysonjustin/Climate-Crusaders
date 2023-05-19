import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block1.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block2.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block3(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block3.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block4(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block4.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block5(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block5.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block6(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block6.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block7(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block7.png')
        self.rect = self.image.get_rect(topleft=pos)


class Block8(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block8.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block9(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block9.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block10(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block10.png')
        self.rect = self.image.get_rect(topleft=pos)

    def flip_vertical(self):
        flipped_image = pygame.transform.flip(self.image, False, True)
        self.image = flipped_image

    def update(self, x_shift):
        self.rect.x += x_shift


class Block11(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block11.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block12(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/mblocks/block12.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
