# import modules
import pygame as pg
from settings import *
from sprites import *
from levels import *
from entities import *
# from scenes import *

class Boundary(Block):
  def __init__(self, level, x, y):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    # self.image.fill(GREEN)  # fill surface with color

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    super().__init__()

# class HouseBlock(Block):
#   def __init__(self, level, x, y, image):
#     self.level = level

#     self.x = x
#     self.y = y

#     self.width = TILESIZE
#     self.height = TILESIZE

#     self.image = pg.Surface(
#         (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
  

#     self.rect = self.image.get_rect()  # rectangle around sprite
#     self.rect.x = self.x * TILESIZE
#     self.rect.y = self.y * TILESIZE

#     super().__init__()

class ImageBlock(Block):
  def __init__(self, level, x, y, image, collide=True, layer=PLAYER_LAYER - 2):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.image = pg.Surface((image[1][2], image[1][3]), pg.SRCALPHA)
    self.image.blit(image[0], (0, 0), image[1])

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    super().__init__(collide, layer)

class TreeStump(Block):
  def __init__(self, level, x, y):
    self.level = level

    # self.x = x + 1/3 * TILESIZE
    # self.y = y + 1/3 * TILESIZE

    # self.width = 1/3 * TILESIZE
    # self.height = 1/3 * TILESIZE

    # self.image = pg.Surface(
    #     (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    # # self.image.blit(TREE_IMG, (0, 0), (80*2/3, 525*2/3, self.width, self.height))
    # self.image.blit(TREE_IMG, (0, 0), (10, 10, TILESIZE, TILESIZE))

    # self.rect = self.image.get_rect()  # rectangle around sprite
    # self.rect.x = self.x * TILESIZE
    # self.rect.y = self.y * TILESIZE

    self.x = x
    self.y = y

    self.width = 32*2/3
    self.height = 32*2/3

    self.image = pg.Surface((self.width, self.height), pg.SRCALPHA)
    self.image.blit(TREE_IMG, (0, 0), (82*2/3, 525*2/3, self.width, self.height))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    super().__init__()