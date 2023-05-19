import pygame
import sys
from settings import *
from settings2 import *
from settings3 import *
from settings4 import *
from level import Level
from level2 import Level2
from level3 import Level3
from level4 import Level4
from tryoverworld import *


class GameState:
    def __init__(self, screen):
        self.home = True
        self.menu = True
        self.play = True
        self.level = None
        self.screen = screen
        self.level_select = LevelSelect()
        self.end = False
        self.music_playing = False

    def play_music(self):
        if not self.music_playing:
            pygame.mixer.music.load(
                "C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/menubg.wav")
            pygame.mixer.music.play(-1)
            self.music_playing = True

    def stop_music(self):
        if self.music_playing:
            pygame.mixer.music.stop()
            self.music_playing = False

    def set_level(self, level_num):
        if level_num == 1:
            self.level = Level(level_map, self.screen)
            self.background = pygame.image.load(
                'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/bg1.png').convert()
        elif level_num == 2:
            self.level = Level2(level_map3, self.screen)
            self.background = pygame.image.load(
                'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/bg2.png').convert()
        elif level_num == 3:
            self.level = Level3(level_map2, self.screen)
            self.background = pygame.image.load(
                'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/bg3.png').convert()
        elif level_num == 4:
            self.level = Level4(level_map4, self.screen)
            self.background = pygame.image.load(
                'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/bg4.png').convert()
        self.home, self.menu = False, False
        self.play = True


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60
level1 = Level(level_map, screen)
level2 = Level2(level_map2, screen)
level3 = Level3(level_map3, screen)
level3 = Level3(level_map3, screen)
level = None


game_state = GameState(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_state.home:
                game_state.home = False
                game_state.menu = True
            elif game_state.menu:
                if event.key == pygame.K_1:
                    game_state.set_level(1)
                elif event.key == pygame.K_2:
                    game_state.set_level(2)
                elif event.key == pygame.K_3:
                    game_state.set_level(3)
                elif event.key == pygame.K_4:
                    game_state.set_level(4)
            else:
                if event.key == pygame.K_ESCAPE:
                    game_state.home = True

    if game_state.home:
        game_state.level_select.homerun(screen)
        game_state.play_music()
    elif game_state.menu:
        game_state.level_select.run(screen)
    elif game_state.play:
        if game_state.level:
            screen.blit(game_state.background, (0, 0))
            game_state.level.run()
            if game_state.level.completed == True:
                game_state.home = True
            pygame.display.update()
            clock.tick(FPS)
