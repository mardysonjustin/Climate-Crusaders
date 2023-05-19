import pygame
from support import import_folder


class Orb(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.07
        self.image = self.animations['orb'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def import_character_assets(self):
        character_path = 'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/fire/'
        self.animations = {'orb': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations['orb']

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        self.image = image

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
