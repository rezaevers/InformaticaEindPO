# import modules
import pygame as pg
from settings import *
from sprites import *
from levels import *
from blocks import *
from entities import *
from scenes import *

class TestItem(Item):
  def __init__(self, level, x, y):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.color = (255, 255, 0)

    self.image = pg.Surface(
        (self.width, self.height))  # image of sprite (or surface)
    self.image.fill(self.color)

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    super().__init__()


class Potion(Item):
  def __init__(self, level, x, y):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.color = (255, 255, 0)

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(POTION_IMG, (16, 16))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    super().__init__()


class Map(Item):
  def __init__(self, level, x, y):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.color = (255, 255, 0)

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(MAP_IMG, (16, 16))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    super().__init__()

class Key(Item):
  def __init__(self, level, x, y, key):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.key = key

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(KEY_IMG, (16, 16))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    super().__init__()


class Axe(Item):
  def __init__(self, level, x, y):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(AXE_IMG, (16, 16))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    super().__init__()


class Log(Item):
  def __init__(self, level, x, y):
    self.level = level

    self.x = x
    self.y = y

    self.width = TILESIZE
    self.height = TILESIZE

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(PLANKS_IMG, (16, 16), (16, 28, 32, 32))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    super().__init__()