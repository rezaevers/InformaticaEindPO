import pygame as pg
from settings import *

# player image
PLAYER_IMG = pg.image.load('assets/Characters/player.png')

# outside tilemap
TILES_IMG = pg.image.load('assets/Island/Tilemap_Flat.png')

# interior images
INSIDE_TILES_IMG = pg.transform.scale_by(pg.image.load('assets/House/more int.png'), 2)
WALL_IMG = pg.transform.scale_by(pg.image.load('assets/House/WALL 1.png'), 2)
RIGHT_WALL = pg.transform.scale_by(pg.image.load('assets/House/wallsa3.png'), 2)
LEFT_WALL = pg.transform.flip(RIGHT_WALL, True, False)
BED_IMG_RIGHT = pg.transform.scale_by(pg.image.load('assets/House/bed 23.png'), 2)
BED_IMG_RIGHT_MIRROR = pg.transform.flip(BED_IMG_RIGHT, False, True)
BED_IMG_LEFT = pg.transform.flip(BED_IMG_RIGHT, True, False)
BED_IMG_LEFT_MIRROR = pg.transform.flip(BED_IMG_LEFT, False, True)
BED_IMG_TOP = pg.transform.rotate(BED_IMG_RIGHT, 90)
BED_IMG_TOP_MIRROR = pg.transform.flip(BED_IMG_TOP, True, False)

# house images
YELLOW_HOUSE = pg.image.load('assets/Island/House_Yellow.png')
BLUE_HOUSE = pg.image.load('assets/Island/House_Blue.png')
RED_HOUSE = pg.image.load('assets/Island/House_Red.png')

# object images
CHEST_IMG = pg.transform.scale_by(pg.image.load('assets/House/BOX.png'), 2)
BOAT_IMG = pg.transform.scale_by(pg.image.load('assets/Items/rowboat.png'), 2)
TREE_IMG = pg.transform.scale_by(pg.image.load('assets/Island/Tree.png'), 2/3)

# item images
POTION_IMG = pg.transform.scale_by(pg.image.load('assets/Items/Potion.png'), 2)
MAP_IMG = pg.transform.scale_by(pg.image.load('assets/Items/Map.png'), 2)
KEY_IMG = pg.transform.scale_by(pg.image.load('assets/Items/keys_2_1.png'), 2)
AXE_IMG = pg.transform.scale_by(pg.image.load('assets/Items/Bijl.png'), 2)
PLANKS_IMG = pg.transform.scale_by(pg.image.load('assets/Items/Hout.png'), 0.5)


TILES = {
  '0': (TILES_IMG, (0, 0, TILESIZE, TILESIZE)),
  '1': (TILES_IMG, (TILESIZE, 0, TILESIZE, TILESIZE)),
  '2': (INSIDE_TILES_IMG, (TILESIZE*2, 0, TILESIZE, TILESIZE)),
  '3': (INSIDE_TILES_IMG, (TILESIZE*2, TILESIZE, TILESIZE, TILESIZE)),
  '4': (INSIDE_TILES_IMG, (TILESIZE, TILESIZE, TILESIZE, TILESIZE)),
  '5': (TILES_IMG, (TILESIZE*5, 0, TILESIZE, TILESIZE)),
  '6': (TILES_IMG, (TILESIZE*6, 0, TILESIZE, TILESIZE)),
  '7': (TILES_IMG, (TILESIZE*7, 0, TILESIZE, TILESIZE)),
  '8': (INSIDE_TILES_IMG, (0, TILESIZE, TILESIZE, TILESIZE)),
  '10': (TILES_IMG, (0, TILESIZE, TILESIZE, TILESIZE)),
  '11': (TILES_IMG, (TILESIZE, TILESIZE, TILESIZE, TILESIZE)),
  '12': (TILES_IMG, (TILESIZE*2, TILESIZE, TILESIZE, TILESIZE)),
  '15': (TILES_IMG, (TILESIZE*5, TILESIZE, TILESIZE, TILESIZE)),
  '16': (TILES_IMG, (TILESIZE*6, TILESIZE, TILESIZE, TILESIZE)),
  '17': (TILES_IMG, (TILESIZE*7, TILESIZE, TILESIZE, TILESIZE)),
  '20': (TILES_IMG, (0, TILESIZE*2, TILESIZE, TILESIZE)),
  '21': (TILES_IMG, (TILESIZE, TILESIZE*2, TILESIZE, TILESIZE)),
  '22': (TILES_IMG, (TILESIZE*2, TILESIZE*2, TILESIZE, TILESIZE)),
  '25': (TILES_IMG, (TILESIZE*5, TILESIZE*2, TILESIZE, TILESIZE)),
  '26': (TILES_IMG, (TILESIZE*6, TILESIZE*2, TILESIZE, TILESIZE)),
  '27': (TILES_IMG, (TILESIZE*7, TILESIZE*2, TILESIZE, TILESIZE)),
        }
