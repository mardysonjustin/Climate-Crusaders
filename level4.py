import pygame
import sys
from tiles4 import *
from terrain import *
from faucet_run import faucetRun
from faucet_close import faucetClose
from shower_run import showerRun
from shower_close import showerClose
from wash_run import washRun
from wash_close import washClose
from player import Player
from settings4 import *


class Level4:

    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.completed = False
        self.world_shiftx = 0
        self.world_shifty = 0
        self.current_x = 0
        self.font = pygame.font.Font(None, 22)

    def faucet_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.faucet_run.sprites():
            if sprite.rect.colliderect(player.rect):
                self.faucet_run.remove(sprite)

                faucet_close = faucetClose(sprite.rect.topleft)
                self.faucet_close.add(faucet_close)

        num_sprites1 = len(self.faucet_run.sprites())
        if num_sprites1 == 0:
            return

        for sprite in self.shower_run.sprites():
            if sprite.rect.colliderect(player.rect):
                self.shower_run.remove(sprite)

                shower_close = showerClose(sprite.rect.topleft)
                self.shower_close.add(shower_close)

        num_sprites2 = len(self.shower_run.sprites())
        if num_sprites2 == 0:
            return

        for sprite in self.wash_run.sprites():
            if sprite.rect.colliderect(player.rect):
                self.wash_run.remove(sprite)

                wash_close = washClose(sprite.rect.topleft)
                self.wash_close.add(wash_close)

        num_sprites3 = len(self.wash_run.sprites())
        if num_sprites3 == 0:
            return

    def show_text(self):
        text1 = self.font.render(
            'Putting out fires reduces CO2 emissions, combating', False, 'White')
        text2 = self.font.render(
            'climate change and preserving our ecosystems.', False, 'White')
        self.display_surface.blit(text1, (5, 10))
        self.display_surface.blit(text2, (5, 25))

    def restart_level(self):
        self.setup_level(level_map4)
        self.world_shiftx = 0
        self.world_shifty = 0
        self.current_x = 0
        self.run()

    def gameover(self):
        screen = pygame.display.set_mode((600, 330))
        image = pygame.image.load(
            "C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/GO.png")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        running = False
                        self.restart_level()
                    elif event.key == pygame.K_n:
                        self.completed = True
                        running = False
            screen.blit(image, (0, 0))
            pygame.display.update()

    def win(self):
        screen = pygame.display.set_mode((600, 330))
        image = pygame.image.load(
            "C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/win.png")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    running = False
            screen.blit(image, (0, 0))
            pygame.display.update()

    def setup_level(self, layout):

        self.tiles = pygame.sprite.Group()
        self.faucet_close = pygame.sprite.Group()
        self.faucet_run = pygame.sprite.Group()
        self.shower_close = pygame.sprite.Group()
        self.shower_run = pygame.sprite.Group()
        self.wash_close = pygame.sprite.Group()
        self.wash_run = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()

        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'Q':
                    tile = Block1((x, y))
                    self.tiles.add(tile)

                if cell == 'W':
                    wall = Wall((x, y))
                    self.wall.add(wall)
                if cell == 'E':
                    wall = Door((x, y))
                    self.wall.add(wall)
                if cell == 'R':
                    wall = Chain((x, y))
                    self.wall.add(wall)
                if cell == 'L':
                    wall = Chand((x, y))
                    self.wall.add(wall)
                if cell == 'T':
                    wall = Window1((x, y))
                    self.wall.add(wall)
                if cell == 'Y':
                    wall = Window2((x, y))
                    self.wall.add(wall)
                if cell == 'U':
                    wall = Water((x, y))
                    self.wall.add(wall)
                if cell == 'I':
                    wall = Water1((x, y))
                    self.wall.add(wall)

                if cell == 'O':
                    faucet_run = faucetRun((x, y))
                    self.faucet_run.add(faucet_run)
                if cell == 'M':
                    shower_run = showerRun((x, y))
                    self.shower_run.add(shower_run)
                if cell == 'N':
                    wash_run = washRun((x, y))
                    self.wash_run.add(wash_run)

                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width and direction_x < 0:
            self.world_shiftx = 2
            player.speed = 0

        elif player_x > screen_width - screen_width and direction_x > 0:
            self.world_shiftx = -2
            player.speed = 0
        else:
            self.world_shiftx = 0
            player.speed = 6

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < screen_height and direction_y < 0:
            self.world_shifty = 2
            player.jump_speed = 0

        elif player_y > screen_height - screen_height and direction_y > 0:
            self.world_shifty = -2
            player.jump_speed = 0

        else:
            self.world_shifty = 0
            player.jump_speed = -10

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
                    player.direction.x = 0

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 5
                    player.on_ceiling = True
                else:
                    player.direction.y = 0

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):
        # level tiles
        self.tiles.update(self.world_shiftx)
        self.tiles.update(self.world_shifty)
        self.wall.update(self.world_shiftx)
        self.wall.update(self.world_shifty)

        self.faucet_collision()

        self.faucet_close.update(self.world_shiftx)
        self.faucet_close.update(self.world_shifty)
        self.faucet_run.update(self.world_shiftx)
        self.faucet_run.update(self.world_shifty)

        self.shower_close.update(self.world_shiftx)
        self.shower_close.update(self.world_shifty)
        self.shower_run.update(self.world_shiftx)
        self.shower_run.update(self.world_shifty)

        self.wash_close.update(self.world_shiftx)
        self.wash_close.update(self.world_shifty)
        self.wash_run.update(self.world_shiftx)
        self.wash_run.update(self.world_shifty)

        self.tiles.draw(self.display_surface)
        self.wall.draw(self.display_surface)
        self.faucet_close.draw(self.display_surface)
        self.faucet_run.draw(self.display_surface)
        self.shower_close.draw(self.display_surface)
        self.shower_run.draw(self.display_surface)
        self.wash_close.draw(self.display_surface)
        self.wash_run.draw(self.display_surface)

        self.scroll_x()

        if self.completed == True:
            return
        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.player.draw(self.display_surface)

        num_sprites1 = len(self.faucet_run.sprites())
        num_sprites2 = len(self.shower_run.sprites())
        num_sprites3 = len(self.wash_run.sprites())
        player = self.player.sprite

        if (num_sprites1 == 0 and num_sprites2 == 0 and num_sprites3 == 0):
            self.win()
            self.completed = True
            return

        if player.rect.y > 400:
            self.gameover()

        self.show_text()
