import pygame

# zyrach


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
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block1.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block2.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block3(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block3.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block4(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block4.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block5(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block5.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block6(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block6.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block7(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block7.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block8(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block8.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block9(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block1.png')
        self.rect = self.image.get_rect(topleft=pos)

    def flip_vertical(self):
        flipped_image = pygame.transform.flip(self.image, False, True)
        self.image = flipped_image

    def update(self, x_shift):
        self.rect.x += x_shift


class Block10(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block9.png')
        self.rect = self.image.get_rect(topleft=pos)

    def flip_vertical(self):
        flipped_image = pygame.transform.flip(self.image, False, True)
        self.image = flipped_image

    def flip_horizontal(self):
        flipped_image = pygame.transform.flip(self.image, True, False)
        self.image = flipped_image

    def flip_both(self):
        flipped_image = pygame.transform.flip(self.image, True, True)
        self.image = flipped_image

    def update(self, x_shift):
        self.rect.x += x_shift


class Block11(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block10.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
