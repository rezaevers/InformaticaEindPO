# basic sprites for pygame project

import pygame as pg
from settings import *
from utils import *
from tiles import *
import random

pg.init()
# pg.mixer.init()


class Player(pg.sprite.Sprite):

  def __init__(self, game):
    self.game = game
    self._layer = PLAYER_LAYER

    self.x = 0
    self.y = 0

    self.width = 13
    self.height = 21
    # self.image = pg.Surface(
    #     (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    # self.image.fill((RED))
    self.image = pg.Surface(
        (self.width, self.height), pg.SRCALPHA)  # image of sprite (or surface)
    self.image.blit(PLAYER_IMG, (0, 0), (18, 22, self.width, self.height))
    self.image = pg.transform.scale_by(self.image, 55/21)

    self.rect = self.image.get_rect()  # rectangle around sprite
    self.width = self.rect.width
    self.height = self.rect.height

    self.direction = pg.math.Vector2()
    self.speed = pg.math.Vector2()
    self.max_speed = PLAYER_SPEED
    self.buffer = MOVEMENT_BUFFER

    self.facing = 'down'

  def setup(self, level, x, y):
    self.level = level
    self.groups = self.level.sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    
    self.x = x
    self.y = y

    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

  def update(self):
    self.input()

    self.x += self.speed.x
    self.y += self.speed.y

    self.rect.x = self.x * TILESIZE
    self.check_collisions('x')
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
    self.check_collisions('y')

    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

    self.level.camera.update()

    self.direction.x = 0
    self.direction.y = 0

  def input(self):
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
      self.direction.x = -1
      self.facing = 'left'
    if keys[pg.K_RIGHT]:
      self.direction.x = 1
      self.facing = 'right'
    if keys[pg.K_DOWN]:
      self.direction.y = 1
      self.facing = 'down'
    if keys[pg.K_UP]:
      self.direction.y = -1
      self.facing = 'up'

    # grid movement
    # if self.x % 1 == 0 and self.y % 1 == 0:
    #   if self.direction.length() != 0:
    #     self.speed = self.direction.normalize()
    #     self.speed.scale_to_length(self.max_speed)
    #   else:
    #     self.speed = pg.math.Vector2()
    # else:
    #   if self.x % 1 < self.buffer:
    #     self.speed.x = -(self.x%1)
    #   if 1 - self.x % 1 < self.buffer:
    #     self.speed.x = 1 - self.x % 1
    #   if self.y % 1 < self.buffer:
    #     self.speed.y = -(self.y%1)
    #   if 1 - self.y % 1 < self.buffer:
    #     self.speed.y = 1 - self.y % 1

    # free movement
    if self.direction.length() != 0:
      self.speed = self.direction.normalize()
      self.speed.scale_to_length(self.max_speed)
    else:
      self.speed = pg.math.Vector2()

    if keys[pg.K_i]:
      print(self.inventory.contents)

  def check_collisions(self, direction):
    hits = pg.sprite.spritecollide(self, self.level.blocks, False)
    if direction == 'x':
      if self.x < 0:
        self.x = 0
        
      if hits:
        # print(hits[0].groups)
        if self.speed.x > 0:
          self.x = hits[0].x - self.width / TILESIZE
        if self.speed.x < 0:
          self.x = hits[0].x + hits[0].width / TILESIZE

    if direction == 'y':
      if self.y < 0:
        self.y = 0

      if hits:
        # print(hits[0].groups)
        if self.speed.y > 0:
          self.y = hits[0].y - self.height  / TILESIZE
        if self.speed.y < 0:
          self.y = hits[0].y + hits[0].height / TILESIZE

class Tile(pg.sprite.Sprite):

  def __init__(self, game, x, y, image):
    self.game = game
    self._layer = TILE_LAYER
    self.groups = [self.game.sprites, self.game.tiles]
    pg.sprite.Sprite.__init__(self, self.groups)

    self.x = x
    self.y = y
    self.width = TILESIZE
    self.height = TILESIZE

    self.image = pg.Surface((image[1][2], image[1][3]), pg.SRCALPHA)
    self.image.blit(image[0], (0, 0), image[1])

    self.rect = self.image.get_rect()
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

  def update(self):
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE
  # class Portal(pg.sprite.Sprite):
  #   def __init__(self, level, goal, x, y, locked):
  #     self.level = level
  #     self._layer = PLAYER_LAYER - 1
  #     self.groups = [self.level.sprites, self.level.objects]
  #     pg.sprite.Sprite.__init__(self, self.groups)

  #     self.goal_level = goal[0]
  #     self.player = level.player

  #     self.locked = locked

  #     self.width = TILESIZE
  #     self.height = TILESIZE
  #     self.x = x
  #     self.y = y

  #     self.goal_x = goal[1]
  #     self.goal_y = goal[2]

  #     self.color = (0, 0, 255)
  #     self.image = pg.Surface(
  #         (self.width, self.height))  # image of sprite (or surface)
  #     self.image.fill(self.color)

  #     self.rect = self.image.get_rect()  # rectangle around sprite
  #     self.rect.x = self.x * TILESIZE
  #     self.rect.y = self.y * TILESIZE

  #   def update(self):
  #     keys = pg.key.get_pressed()
  #     self.rect.x = self.x * TILESIZE
  #     self.rect.y = self.y * TILESIZE

  #     activated = self.rect.colliderect(self.player.rect) and keys[pg.K_SPACE] and not self.locked
  #     if activated:
  #       print(f'activated {self.goal_level}')
  #       self.level.game.sm.to_scene(self.level.game.levels[self.goal_level], self.goal_x, self.goal_y)

  #   def use(self, item):
  #     if item == TestItem():
  #       self.locked = False
  #       return True
  #     print('wrong')
  #     return False

class Object(pg.sprite.Sprite):
  def __init__(self, layer=PLAYER_LAYER-3):
    self._layer = layer
    self.groups = [self.level.sprites, self.level.objects]
    pg.sprite.Sprite.__init__(self, self.groups)

    self.game = self.level.game
    self.player = self.game.player

  def update(self):
    self.input()
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

  def input(self):
    keys = pg.key.get_pressed()
    activated = keys[pg.K_SPACE] and self.rect.colliderect(self.player.rect)
    # print(self.rect, self.player.rect)
    if activated:
      self.activate()

  def activate(self):
    pass
  
  def use(self):
    pass
  

class Item(pg.sprite.Sprite):
  def __init__(self):
    self._layer = PLAYER_LAYER - 2
    self.groups = [self.level.sprites, self.level.items]
    pg.sprite.Sprite.__init__(self, self.groups)

    self.game = self.level.game
    self.player = self.game.player

  def update(self):
    self.input()
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE

  def input(self):
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE] and self.rect.colliderect(self.player.rect):
      self.pick_up()

  def pick_up(self):
    self.kill()
    new_img = pg.Surface(
        (TILESIZE/2, TILESIZE/2), pg.SRCALPHA)
    new_img.blit(self.image, (0, 0), (16, 16, 32, 32))
    border = self.level.game.inventory.border
    pg.transform.scale(new_img, (INVENTORY_HEIGHT - 2 * border, INVENTORY_HEIGHT - 2 * border))
    self.image = new_img
    self.game.inventory.add(self)
    
class InventoryItem(pg.sprite.Sprite):
  def __init__(self, inventory, item):
    self.inventory = inventory
    self.item = item
    self.x = 0
    self.y = 0
    self.width = self.item.width
    self.height = self.item.height
    self.groups = [inventory.contents]
    pg.sprite.Sprite.__init__(self, self.groups)
    self.image = pg.transform.scale_by(self.item.image, SCALE_FACTOR * 2)
    self.rect = self.image.get_rect()
    self.grabbed = False

  def update(self):
    if not self.grabbed:
      self.grabbed = self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]
    else:
      self.grabbed = pg.mouse.get_pressed()[0]
      if not self.grabbed:
        self.inventory.drop(self)
    
    if self.grabbed:
      self.rect.x, self.rect.y = pg.mouse.get_pos()
      self.rect.x -= self.width / 2
      self.rect.y -= self.height / 2
    else:
      self.rect.x, self.rect.y = self.x, self.y

class Block(pg.sprite.Sprite):
  def __init__(self, collide=True, layer=PLAYER_LAYER-2):
    self._layer = layer
    if collide:
      self.groups = [self.level.sprites, self.level.blocks]
    else:
      self.groups = [self.level.sprites, self.level.non_collide_blocks]
    pg.sprite.Sprite.__init__(self, self.groups)

    self.player = self.level.player

  def update(self):
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE