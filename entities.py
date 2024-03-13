# import modules
import pygame as pg
from pygame.rect import Rect
from settings import *
from sprites import *
from levels import *
from blocks import *
from tiles import *


class Tilemap:

  def __init__(self, level, map):
    self.map = map
    self.tiles = []
    self.level = level
    self.create_map()

  def create_map(self):
    for i, row in enumerate(self.map):
      for j, tile in enumerate(row):
        if tile in TILES:
          self.tiles.append(Tile(self.level, j, i, TILES[tile]))


class Camera:

  def __init__(self, level, width, height):
    self.level = level
    self.width = width
    self.height = height
    self.x = self.level.player.x - self.width / 2 + self.level.player.width / 2 / TILESIZE
    self.y = self.level.player.y - self.height / 2 + self.level.player.height / 2 / TILESIZE
    print(self.width, self.height)
    print(self.x, self.y)

  def update(self):
    self.x = self.level.player.x - self.width / 2 + self.level.player.width / 2 / TILESIZE
    self.y = self.level.player.y - self.height / 2 + self.level.player.height / 2 / TILESIZE

  def draw(self, surface, lvl_surface):
    surface.fill(self.level.bg_color)
    rect = surface.get_rect()
    surface.blit(lvl_surface, (0, 0),
                 (self.x * TILESIZE, self.y * TILESIZE, self.width * TILESIZE,
                  self.height * TILESIZE))


class SceneManager:

  def __init__(self, game):
    self.game = game
    self.current_scene = None
    self.lvl_surface = pg.Surface((3000, 3000), pg.SRCALPHA)

  def enter_scene(self, scene, x, y):
    self.current_scene = scene
    self.current_scene.setup(x, y)

  def update(self):
    self.current_scene.update()

  def draw(self, surface):
    self.lvl_surface.fill((0, 0, 0, 0))
    self.current_scene.draw(self.lvl_surface)
    self.current_scene.camera.draw(surface, self.lvl_surface)

  def to_scene(self, scene, x, y):
    self.game.playing = False
    transition = FadeTransition(self.game)
    transition.fade_out()
    self.enter_scene(scene, x, y)
    self.update()
    self.draw(self.game.game_surface)
    transition.fade_in()
    self.game.playing = True


class FadeTransition:

  def __init__(self, game):
    self.fade_surface = pg.Surface((WIDTH, GAME_SURF_HEIGHT))
    self.fade_surface.fill(BLACK)
    self.game = game

  def fade_out(self):
    for i in range(0, 255, 5):
      self.game.sm.draw(self.game.game_surface)
      self.fade_surface.set_alpha(i)
      self.game.window.blit(
          pg.transform.scale(self.game.game_surface,
                             (WIDTH, GAME_SURF_HEIGHT)), (0, 0))
      self.game.window.blit(self.fade_surface, (0, 0))
      pg.display.flip()
      pg.time.delay(2)

  def fade_in(self):
    for i in range(0, 255, 5):
      self.game.sm.draw(self.game.game_surface)
      self.fade_surface.set_alpha(255 - i)
      self.game.window.blit(
          pg.transform.scale(self.game.game_surface,
                             (WIDTH, GAME_SURF_HEIGHT)), (0, 0))
      self.game.window.blit(self.fade_surface, (0, 0))
      pg.display.flip()
      pg.time.delay(2)


class Inventory:

  def __init__(self, game):
    self.game = game
    self.contents = pg.sprite.Group()
    self.border = 0.15 * INVENTORY_HEIGHT

  def add(self, item):
    inventory_item = InventoryItem(self, item)
    self.contents.add(inventory_item)
    self.reformat()

  def draw_back(self, surface):
    surface.fill((0, 0, 100))
    for index, item in enumerate(self.contents):
      pg.draw.rect(surface, (0, 0, 50),
                   (self.border + index * (INVENTORY_HEIGHT - self.border),
                    self.border, INVENTORY_HEIGHT - 2 * self.border,
                    INVENTORY_HEIGHT - 2 * self.border))

  def draw_items(self, surface):
    surface.fill((0, 0, 0, 0))
    self.contents.draw(surface)

  def update(self):
    self.contents.update()

  def reformat(self):
    for index, item in enumerate(self.contents):
      item.x = INVENTORY_HEIGHT / 2 + index * (INVENTORY_HEIGHT -
                                               self.border) - item.width / 2
      item.y = HEIGHT - INVENTORY_HEIGHT / 2 - item.height / 2
      (item.rect.x, item.rect.y) = (item.x, item.y)

  def drop(self, item):
    old_rect = item.rect
    screen_rect = Rect(
        item.rect.x / SCALE_FACTOR +
        self.game.sm.current_scene.camera.x * TILESIZE,
        item.rect.y / SCALE_FACTOR +
        self.game.sm.current_scene.camera.y * TILESIZE,
        item.width / SCALE_FACTOR, item.height / SCALE_FACTOR)
    print(screen_rect)
    for object in self.game.sm.current_scene.objects:
      print(object.rect)
    print(self.game.sm.current_scene.camera.x,
          self.game.sm.current_scene.camera.y)
    item.rect = screen_rect
    hits = pg.sprite.spritecollide(item, self.game.sm.current_scene.objects,
                                   False)
    if hits:
      print('used')
      if hits[0].use(item):
        self.contents.remove(item)
        self.reformat()
    item.rect = old_rect

class TextManager:
  def __init__(self, game):
    print(pg.font.get_fonts())
    self.game = game  
    self.text_surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
    self.game = game
    self.font = pg.font.Font('assets/fonts/PixelFont.ttf', 30)
    # self.text = self.font.render('Hello World', True, WHITE)
    # self.rect = self.text.get_rect()
    # self.rect.center = (WIDTH / 2, GAME_SURF_HEIGHT - 70)
    self.text = None
    self.timer = 0

  def show_text(self, text, time):
    self.timer = pg.time.get_ticks() + time
    self.text = self.font.render(text, True, WHITE)
    self.rect = self.text.get_rect()
    self.rect.center = (WIDTH / 2, GAME_SURF_HEIGHT - 70)

  def update(self):
    if pg.time.get_ticks() > self.timer:
      self.text = None
  
  def draw(self, surface):
    if self.text:
      text_surface = pg.Surface((self.rect.width+10, self.rect.height+10), pg.SRCALPHA)
      surface_rect = text_surface.get_rect()
      text_surface.fill((0, 0, 0, 150))
      text_rect = self.text.get_rect()
      text_rect.center = (surface_rect.width / 2, surface_rect.height / 2)
      text_surface.blit(self.text, text_rect)
      surface.blit(text_surface, self.rect)
