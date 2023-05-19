import pygame


class Block1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block2.4.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Block2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block2.2.png')
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


class Block3(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block2.1.png')
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


class Block4(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block2.3.png')
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


class Block5(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/block2.5.png')
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


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/blocks/tree.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
