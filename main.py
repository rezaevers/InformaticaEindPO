# import modules
import pygame as pg
from pygame.event import wait
from settings import *
from sprites import *
from entities import *
from scenes import *
import utils


# game
class Game:

  def __init__(self):
    # initiating pygame
    pg.init()
    # pg.mixer.init()

    # setting up the display window
    self.clock = pg.time.Clock()
    self.game_surface = pg.Surface((CAMERA_WIDTH * TILESIZE, CAMERA_HEIGHT * TILESIZE))
    self.inventory_surface = pg.Surface((WIDTH, INVENTORY_HEIGHT))
    self.inventory_overlay = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
    self.window = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    pg.display.set_caption("Scavenger")

    self.player = Player(self)

    self.inventory = Inventory(self)
    self.sm = SceneManager(self)
    self.tm = TextManager(self)

    self.lvl_names = os.listdir('levels')

    self.levels = dict()
    for level in self.lvl_names:
      self.levels[level] = Level(utils.load_data(level), self)

    self.running = True

  def setup(self):
    self.playing = True
    self.sm.enter_scene(self.levels['island'], 11, 7)

  def events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        self.playing = False
        self.running = False
        quit()

  def draw(self):
    self.window.fill(BLACK)
    self.sm.draw(self.game_surface)
    self.inventory.draw_back(self.inventory_surface)
    self.inventory.draw_items(self.inventory_overlay)
    self.window.blit(pg.transform.scale(self.game_surface, (WIDTH, GAME_SURF_HEIGHT)), (0, 0))
    self.window.blit(self.inventory_surface, (0, HEIGHT-INVENTORY_HEIGHT))
    self.window.blit(self.inventory_overlay, (0, 0))
    self.tm.draw(self.window)
    pg.display.flip()

  def update(self):
    self.sm.update()
    self.tm.update()
    self.inventory.update()

  def main(self):
    if self.playing:
      self.events()
      self.update()
      self.draw()
      self.clock.tick(FPS)

  def intro(self):
    lines = ["I'm stranded on this abandoned island", "I need to get back home", "But before I leave, I need to collect some tools", "I need to find a map, a potion, and a log", "They must be somewhere on this island", "Use the arrow keys to move", "and the space bar to pick up items", "and to open doors and chests", "Then leave by boat once all the items have been collected", "Good luck!"]
    self.current_line = None
    self.lines_timer = 0
    busy = True
    while busy:
      self.events()
      if self.current_line is None:
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN] or keys[pg.K_SPACE]:
          print('start')
          self.current_line = 0
          self.lines_timer = pg.time.get_ticks() + 400
      else:
        if self.cutscene_update(lines):
          busy = False
      self.draw()
      pg.event.pump()
      self.clock.tick(FPS)

  def cutscene_update(self, lines):
    cooldown = 400
    keys = pg.key.get_pressed()
    self.tm.show_text(lines[self.current_line], 100)
    if self.lines_timer < pg.time.get_ticks() and keys[pg.K_SPACE]:
      print('new line')
      print(self.lines_timer, pg.time.get_ticks())
      self.current_line += 1
      if self.current_line >= len(lines):
        print('done with lines')
        return True
      self.lines_timer = pg.time.get_ticks() + cooldown

  def win(self):
    # self.update()
    # self.draw()
    self.playing = False
    lines = ["All the items I need have been collected!", "Congratulations, you win!", "To play again, press enter. To quit, press Q"]
    self.current_line = 0
    self.lines_timer = pg.time.get_ticks() + 400
    busy = True
    while busy:
      self.events()
      keys = pg.key.get_pressed()
      if keys[pg.K_RETURN]:
        # self.__init__()
        # self.setup()
        # self.intro()
        # while self.running:
        #   self.main()
        pg.quit()
        start()
      if keys[pg.K_q]:
        pg.quit()
        self.running = False
        busy = False
        quit()
      if self.cutscene_update(lines):
        self.current_line = len(lines) - 1
      self.draw()
      pg.event.pump()
      self.clock.tick(FPS)

def start():
  g = Game()
  g.setup()
  g.intro()
  while g.running:
    g.main()

start()
