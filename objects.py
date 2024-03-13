import pygame as pg
from settings import *
from utils import *
from items import *
from sprites import *
from blocks import TreeStump


class Portal(Object):
  def __init__(self, level, goal, x, y, key):
    self.level = level
    self._layer = PLAYER_LAYER - 1
    self.groups = [self.level.sprites, self.level.objects]
    pg.sprite.Sprite.__init__(self, self.groups)

    self.goal_level = goal[0]
    self.player = level.player

    self.key = key

    self.width = TILESIZE * 2
    self.height = TILESIZE / 2
    self.x = x
    self.y = y

    self.goal_x = goal[1]
    self.goal_y = goal[2]

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    super().__init__()

  def use(self, item):
    print(item)
    if self.key:
      if isinstance(item.item, Key):
        if item.item.key == self.key:
          self.key = None
          return True
      self.level.game.tm.show_text('this key does not fit this door', 1500)
      print('wrong')
    self.level.game.tm.show_text('this door is not locked', 1500)
    print('unlocked')
    return False

  def activate(self):
    print(f'{self.goal_level} activated')
    if not self.key:
      self.level.game.sm.to_scene(self.level.game.levels[self.goal_level], self.goal_x, self.goal_y)
    else:
      self.level.game.tm.show_text('this door is locked', 1500)
      print('locked')


class Chest(Object):
  def __init__(self, level, x, y, key, contents):
    self.level = level
    self._layer = PLAYER_LAYER - 1
    self.groups = [self.level.sprites, self.level.objects]
    pg.sprite.Sprite.__init__(self, self.groups)
    
    self.player = level.player

    self.key = key
    self.contents = contents

    if self.contents:
      self.contents.kill()

    self.width = TILESIZE * 2
    self.height = TILESIZE * 1.5
    self.x = x
    self.y = y

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    self.cool_down = 0

    super().__init__()

  def use(self, item):
    print(item)
    if self.key:
      if isinstance(item.item, Key):
        if item.item.key == self.key:
          self.key = None
          return True
        self.level.game.tm.show_text('this key does not fit this chest', 1500)
      print('wrong')
      return False
    self.level.game.tm.show_text('this chest is not locked', 1500)
    print('unlocked')
    return False

  def activate(self):
    if self.cool_down < pg.time.get_ticks():
      if not self.key:
        if self.contents:
          self.contents.pick_up()
          self.contents = None
          self.cool_down = pg.time.get_ticks() + 1000
        else:
          print('empty')
          self.level.game.tm.show_text('this chest is empty', 1500)
      else:
        self.level.game.tm.show_text('this chest is locked', 1500)
        print('locked')


class Boat(Object):
  def __init__(self, level, x, y):
    self.level = level
    self._layer = PLAYER_LAYER - 1
    self.groups = [self.level.sprites, self.level.objects]
    pg.sprite.Sprite.__init__(self, self.groups)

    self.player = level.player

    self.width = 94*2
    self.height = 45*2
    self.x = x
    self.y = y

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(BOAT_IMG, (0, 0), (0, 17*2, self.width, self.height))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    super().__init__()

  def use(self, item):
    return False

  def activate(self):
    map = any(isinstance(item.item, Map) for item in self.level.game.inventory.contents)
    potion = any(isinstance(item.item, Potion) for item in self.level.game.inventory.contents)
    log = any(isinstance(item.item, Log) for item in self.level.game.inventory.contents)
    if map and potion and log:
      print('win')
      self.level.player.rect.center = (self.rect.center[0], self.rect.y+20)
      self.level.game.win()
    else:
      missing = []
      if not map:
        missing.append('map')
      if not potion:
        missing.append('potion')
      if not log:
        missing.append('log')
      print('not done yet')
      print(map, potion, log)
      self.level.game.tm.show_text(f'you are still missing: {", ".join(missing)}', 2000)

class Tree(Object):
  def __init__(self, level, x, y):
    self.level = level

    self.player = level.player

    self.width = TILESIZE * 2
    self.height = TILESIZE * 2
    self.x = x
    self.y = y

    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(TREE_IMG, (0, 0), (0, 0, self.width, self.height))

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    TreeStump(self.level, self.x+5/6, self.y+9/6)

    super().__init__(PLAYER_LAYER+2)

  def use(self, item):
    print(item)
    if isinstance(item.item, Axe):
      self.kill()
      planks = Log(self.level, self.x, self.y)
      planks.pick_up()
      return True
    print('wrong')
    return False