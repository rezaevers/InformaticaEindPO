# import modules
import pygame as pg
from settings import *
from sprites import *
from entities import *
import entities
from levels import *
from blocks import *
import blocks
from items import *	
from objects import *
from tiles import *

class Scene:
  def setup(self):
    pass

  def update(self):
    pass

  def draw(self):
    pass


class Level(Scene):

  def __init__(self, lvl_data, game):
    self.tiles_data = lvl_data['tiles']
    self.objects_data = lvl_data['objects']
    self.blocks_data = lvl_data['blocks']
    self.game = game

    if self.tiles_data[0][0] == '-1':
      self.bg_color = (99, 169, 168)
    else:
      self.bg_color = (23, 14, 4)

    # create sprite groups
    self.sprites = pg.sprite.LayeredUpdates()
    self.tiles = pg.sprite.LayeredUpdates()
    self.blocks = pg.sprite.LayeredUpdates()
    self.non_collide_blocks = pg.sprite.LayeredUpdates()
    self.objects = pg.sprite.LayeredUpdates()
    self.items = pg.sprite.LayeredUpdates()

    # creating player
    self.player = self.game.player

    # creating objects
    self.create_objects(self.objects_data)

    # create blocks
    self.create_blocks(self.blocks_data)

    # create tilemap
    self.tilemap = entities.Tilemap(self, self.tiles_data)

    # create camera
    self.camera = entities.Camera(self, CAMERA_WIDTH, CAMERA_HEIGHT)

  def setup(self, x, y):
    self.player.setup(self, x, y)

    # create camera
    self.camera = entities.Camera(self, CAMERA_WIDTH, CAMERA_HEIGHT)
    # test objects
    # self.portal0 = Portal(self, 'world', 3, 1, RED)
    # self.portal1 = Portal(self, 'level1', 3, 4, BLUE)
    # self.item0 = TestItem(self, 1, 1)

  def update(self):
    # self.player.update()
    # self.tiles.update()
    # self.items.update()
    # self.objects.update()
    # self.blocks.update()
    self.sprites.update()
    # print(block for block in self.blocks)
    # print()

  def draw(self, surface):
    self.sprites.draw(surface)

  def create_objects(self, data):
    for i, row in enumerate(data):
      for j, cell in enumerate(row):
        if cell == '1':
          Portal(self, ('yellow_house', 6.7, 7.5), j, i+0.5, None) # to house 1 (yellow)
        if cell == '2':
          Portal(self, ('blue_house', 4.7, 12.5), j, i+0.5, 'blue_door') # to house 2 (blue)
        if cell == '3':
          Portal(self, ('red_house', 4.7, 7.5), j, i+0.5, None) # to house 3 (red)
        if cell == '4':
          Portal(self, ('island', 10.7, 6), j, i+0.5, None) # from house 1 (yellow)
        if cell == '5':
          Portal(self, ('island', 18.7, 10), j, i+0.5, None) # from house 2 (blue)
        if cell == '6':
          Portal(self, ('island', 7.7, 13), j, i+0.5, None) # from house 3 (red)
        if cell == '7':
          Potion(self, j, i)
        if cell == '8':
          Chest(self, j, i, None, Key(self, j, i, 'chest'))
        if cell == '9':
          Key(self, j, i, 'blue_door')
        if cell == '10':
          Chest(self, j, i, 'chest', Map(self, j, i))
        if cell == '11':
          Chest(self, j, i, None, None)
        if cell == '12':
          Chest(self, j, i, None, Axe(self, j, i))
        if cell == '13':
          Boat(self, j, i+0.1)
        if cell == '14':
          Tree(self, j, i)

  def create_blocks(self, data):
    for i, row in enumerate(data):
      for j, cell in enumerate(row):
        if cell == '0':
          blocks.ImageBlock(self, j, i, (WALL_IMG, (0, 0, TILESIZE, TILESIZE)))
        if cell == '1':
          blocks.Boundary(self, j, i)
        if cell == '2':
          blocks.ImageBlock(self, j, i, (RIGHT_WALL, (TILESIZE, 0, TILESIZE, TILESIZE)))
        if cell == '3':
          blocks.ImageBlock(self, j, i, (LEFT_WALL, (0, 0, TILESIZE, TILESIZE)))
        if cell == '4':
          blocks.ImageBlock(self, j, i, (YELLOW_HOUSE, (0, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '5':
          blocks.ImageBlock(self, j, i, (YELLOW_HOUSE, (TILESIZE, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '6':
          blocks.ImageBlock(self, j, i, (YELLOW_HOUSE, (0, TILESIZE*2, TILESIZE, TILESIZE)), False)
        if cell == '7':
          blocks.ImageBlock(self, j, i, (YELLOW_HOUSE, (TILESIZE, TILESIZE*2, TILESIZE, TILESIZE)), False)
        if cell == '8':
          blocks.ImageBlock(self, j, i, (BLUE_HOUSE, (0, 0, TILESIZE, TILESIZE)), False, PLAYER_LAYER+1)
        if cell == '9':
          blocks.ImageBlock(self, j, i, (BLUE_HOUSE, (TILESIZE, 0, TILESIZE, TILESIZE)), False, PLAYER_LAYER+1)
        if cell == '10':
          blocks.ImageBlock(self, j, i, (BLUE_HOUSE, (0, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '11':
          blocks.ImageBlock(self, j, i, (BLUE_HOUSE, (TILESIZE, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '12':
          blocks.ImageBlock(self, j, i, (BLUE_HOUSE, (0, TILESIZE*2, TILESIZE, TILESIZE)), False)
        if cell == '13':
          blocks.ImageBlock(self, j, i, (BLUE_HOUSE, (TILESIZE, TILESIZE*2, TILESIZE, TILESIZE)), False)
        if cell == '14':
          blocks.ImageBlock(self, j, i, (RED_HOUSE, (0, 0, TILESIZE, TILESIZE)), False, PLAYER_LAYER+1)
        if cell == '15':
          blocks.ImageBlock(self, j, i, (RED_HOUSE, (TILESIZE, 0, TILESIZE, TILESIZE)), False, PLAYER_LAYER+1)
        if cell == '16':
          blocks.ImageBlock(self, j, i, (RED_HOUSE, (0, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '17':
          blocks.ImageBlock(self, j, i, (RED_HOUSE, (TILESIZE, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '18':
          blocks.ImageBlock(self, j, i, (RED_HOUSE, (0, TILESIZE*2, TILESIZE, TILESIZE)), False)
        if cell == '19':
          blocks.ImageBlock(self, j, i, (RED_HOUSE, (TILESIZE, TILESIZE*2, TILESIZE, TILESIZE)), False)
        if cell == '20':
          blocks.ImageBlock(self, j, i, (WALL_IMG, (0, 0, TILESIZE, TILESIZE)))
          blocks.ImageBlock(self, j, i, (RIGHT_WALL, (TILESIZE, 0, TILESIZE, TILESIZE)))
        if cell == '21':
          blocks.ImageBlock(self, j, i, (YELLOW_HOUSE, (0, 0, TILESIZE, TILESIZE)), False, PLAYER_LAYER+1)
        if cell == '22':
          blocks.ImageBlock(self, j, i, (YELLOW_HOUSE, (TILESIZE, 0, TILESIZE, TILESIZE)), False, PLAYER_LAYER+1)
        if cell == '23':
          blocks.ImageBlock(self, j, i, (CHEST_IMG, (0, 0, TILESIZE, TILESIZE)))
        if cell == '24':
          blocks.ImageBlock(self, j, i, (CHEST_IMG, (TILESIZE, 0, TILESIZE, TILESIZE)))
        if cell == '25':
          blocks.ImageBlock(self, j, i, (BED_IMG_LEFT, (0, 0, TILESIZE, TILESIZE)))
        if cell == '26':
          blocks.ImageBlock(self, j, i, (BED_IMG_LEFT, (TILESIZE, 0, TILESIZE, TILESIZE)))
        if cell == '27':
          blocks.ImageBlock(self, j, i, (BED_IMG_LEFT_MIRROR, (0, 28, TILESIZE, TILESIZE)))
        if cell == '28':
          blocks.ImageBlock(self, j, i, (BED_IMG_LEFT_MIRROR, (TILESIZE, 28, TILESIZE, TILESIZE)))
        if cell == '30':
          blocks.ImageBlock(self, j, i, (WALL_IMG, (0, 0, TILESIZE, TILESIZE)))
          blocks.ImageBlock(self, j, i, (LEFT_WALL, (0, 0, TILESIZE, TILESIZE)))
        if cell == '31':
          blocks.ImageBlock(self, j, i, (BED_IMG_TOP, (0, 0, TILESIZE, TILESIZE)))
        if cell == '32':
          blocks.ImageBlock(self, j, i, (BED_IMG_TOP_MIRROR, (28, 0, TILESIZE, TILESIZE)))
        if cell == '33':
          blocks.ImageBlock(self, j, i, (BED_IMG_TOP, (0, TILESIZE, TILESIZE, TILESIZE)))
        if cell == '34':
          blocks.ImageBlock(self, j, i, (BED_IMG_TOP_MIRROR, (28, TILESIZE, TILESIZE, TILESIZE)))

class IntroScene(Scene):
  pass