import pygame
from tiles2 import *
from orb import Orb
from player import Player
from settings3 import *
import sys


class Level2:

    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shiftx = 0
        self.world_shifty = 0
        self.current_x = 0
        self.completed = False
        self.font = pygame.font.Font(None, 22)

    def orb_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.orb.sprites():
            if sprite.rect.colliderect(player.rect):
                self.orb.remove(sprite)

                tree = Tree(sprite.rect.topleft)
                self.tree.add(tree)

        num_sprites = len(self.orb.sprites())

        if num_sprites == 0:
            return

    def get_num_sprites(self):  # new
        num_sprites = len(self.orb.sprites())
        return num_sprites

    def show_text(self):
        text1 = self.font.render(
            'Planting trees absorbs carbon dioxide, mitigates climate change,', False, 'White')
        text2 = self.font.render(
            'and enhances ecosystem resilience and biodiversity.', False, 'White')
        self.display_surface.blit(text1, (10, 10))
        self.display_surface.blit(text2, (10, 25))

    def restart_level(self):  # new
        self.setup_level(level_map3)
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

        self.tiles2 = pygame.sprite.Group()
        self.tree = pygame.sprite.Group()
        self.orb = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Block1((x, y))
                    self.tiles2.add(tile)
                if cell == 'W' or 'E':
                    tile = Block2((x, y))
                    if cell == 'W':
                        self.tiles2.add(tile)
                    elif cell == 'E':
                        tile.flip_horizontal()
                        self.tiles2.add(tile)
                if cell == 'H' or 'D' or 'F' or 'I':
                    tile = Block3((x, y))
                    if cell == 'H':
                        self.tiles2.add(tile)
                    elif cell == 'D':
                        tile.flip_horizontal()
                        self.tiles2.add(tile)
                    elif cell == 'F':
                        tile.flip_vertical()
                        self.tiles2.add(tile)
                    elif cell == 'I':
                        tile.flip_both()
                        self.tiles2.add(tile)

                if cell == 'M' or 'N':
                    tile = Block4((x, y))
                    if cell == 'M':
                        self.tiles2.add(tile)
                    elif cell == 'N':
                        tile.flip_vertical()
                        self.tiles2.add(tile)
                if cell == 'Z' or 'C' or 'V' or 'B':
                    tile = Block5((x, y))
                    if cell == 'Z':
                        self.tiles2.add(tile)
                    elif cell == 'C':
                        tile.flip_horizontal()
                        self.tiles2.add(tile)
                    elif cell == 'V':
                        tile.flip_vertical()
                        self.tiles2.add(tile)
                    elif cell == 'B':
                        tile.flip_both()
                        self.tiles2.add(tile)
                if cell == 'O':
                    orb = Orb((x, y))
                    self.orb.add(orb)

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

        for sprite in self.tiles2.sprites():
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

        for sprite in self.tiles2.sprites():
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
        self.tiles2.update(self.world_shiftx)
        self.tiles2.update(self.world_shifty)

        self.orb_collision()

        self.tree.update(self.world_shiftx)
        self.tree.update(self.world_shifty)
        self.orb.update(self.world_shiftx)
        self.orb.update(self.world_shifty)

        self.tiles2.draw(self.display_surface)
        self.tree.draw(self.display_surface)
        self.orb.draw(self.display_surface)

        self.scroll_x()

        if self.completed == True:  # new
            return
        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.player.draw(self.display_surface)

        num_sprites = self.get_num_sprites()  # new
        player = self.player.sprite

        if player.rect.y > 400:  # new
            self.gameover()

        if num_sprites == 0:  # new
            self.win()
            self.completed = True
            return

        self.show_text()
