import pygame
import sys
from tiles import *
from fire1 import Fire, Cond
from smoke1 import Smoke, Smoke2
from player import Player
from settings import *

# mardy
pygame.mixer.init()


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shiftx = 0
        self.world_shifty = 0
        self.current_x = 0
        self.completed = False  # add
        self.font = pygame.font.Font(None, 22)

    def fire_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.fire.sprites():
            if sprite.rect.colliderect(player.rect):
                self.fire.remove(sprite)

                smoke = Smoke(sprite.rect.topleft)
                self.smoke.add(smoke)

        num_sprites1 = len(self.fire.sprites())

        if num_sprites1 == 0:
            return  # check if same

    def play_music(self):
        pygame.mixer.music.load(
            "C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/level1.wav")
        pygame.mixer.music.play(0)

    def cond_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.cond.sprites():
            if sprite.rect.colliderect(player.rect):
                self.cond.remove(sprite)

                smoke = Smoke2(sprite.rect.topleft)
                self.smoke.add(smoke)

        num_sprites2 = len(self.cond.sprites())

        if num_sprites2 == 0:
            return

    def get_num_sprites1(self):
        num_sprites1 = len(self.fire.sprites())
        return num_sprites1

    def get_num_sprites2(self):
        num_sprites2 = len(self.cond.sprites())
        return num_sprites2

    def show_text(self):
        text1 = self.font.render(
            'Reducing energy consumption results to reduced emissions, mitigating', False, 'White')
        text2 = self.font.render(
            'climate crisis, and greener and sustainable future.', False, 'White')
        self.display_surface.blit(text1, (5, 10))
        self.display_surface.blit(text2, (5, 25))

    def restart_level(self):
        self.setup_level(level_map)
        self.world_shiftx = 0
        self.world_shifty = 0
        self.current_x = 0
        self.run()

    def gameover(self):  # may iniba ako
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
                        # Restart the level
                        self.restart_level()
                    elif event.key == pygame.K_n:
                        self.completed = True
                        running = False
            screen.blit(image, (0, 0))
            pygame.display.update()

    def win(self):  # new
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
        self.smoke = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.fire = pygame.sprite.Group()
        self.cond = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'Q':
                    tile = Block1((x, y))
                    self.tiles.add(tile)
                if cell == 'W':
                    tile = Block2((x, y))
                    self.tiles.add(tile)
                if cell == 'E':
                    tile = Block3((x, y))
                    self.tiles.add(tile)
                if cell == 'R':
                    tile = Block4((x, y))
                    self.tiles.add(tile)
                if cell == 'T':
                    tile = Block5((x, y))
                    self.tiles.add(tile)
                if cell == 'X':
                    tile = Block6((x, y))
                    self.tiles.add(tile)
                if cell == 'Y':
                    tile = Block7((x, y))
                    self.tiles.add(tile)
                if cell == 'U':
                    tile = Block8((x, y))
                    self.tiles.add(tile)
                if cell == 'A':
                    tile = Block9((x, y))
                    self.tiles.add(tile)
                if cell == 'S':
                    tile = Block10((x, y))
                    self.tiles.add(tile)
                if cell == 'G':
                    tile = Block11((x, y))
                    self.tiles.add(tile)
                if cell == 'F':
                    tile = Block12((x, y))
                    self.tiles.add(tile)

                if cell == 'O':
                    fire = Fire((x, y))
                    self.fire.add(fire)
                if cell == 'L':
                    cond = Cond((x, y))
                    self.cond.add(cond)
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
        if self.completed == True:  # new
            return

        self.tiles.update(self.world_shiftx)
        self.tiles.update(self.world_shifty)
        self.fire_collision()
        self.cond_collision()

        self.smoke.update(self.world_shiftx)
        self.smoke.update(self.world_shifty)
        self.fire.update(self.world_shiftx)
        self.fire.update(self.world_shifty)
        self.cond.update(self.world_shiftx)
        self.cond.update(self.world_shifty)

        self.tiles.draw(self.display_surface)
        self.smoke.draw(self.display_surface)
        self.fire.draw(self.display_surface)
        self.cond.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        num_sprites1 = self.get_num_sprites1()  # new
        num_sprites2 = self.get_num_sprites2()  # new

        player = self.player.sprite

        if player.rect.y > 400:  # new
            self.gameover()

        if num_sprites1 == 0 and num_sprites2 == 0:  # new
            self.win()
            self.completed = True
            return

        self.show_text()
