import math
import csv
import os

def read_csv(file):
  with open(file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = []
    for row in reader:
      data.append(list(row))
    return data

# background
# objects
# player
# portals

def load_data(folder):
  data = {'tiles': read_csv('levels/' + folder + '/' + folder + '_map.csv'), 
          'objects': read_csv('levels/' + folder + '/' + folder + '_objects.csv'),
          'blocks': read_csv('levels/' + folder + '/' + folder + '_blocks.csv')
         }
  return data
