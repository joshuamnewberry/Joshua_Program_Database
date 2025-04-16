import random
import copy
import sys

viz = False
random_seed = -1
#print('Received', len(sys.argv) - 1, 'command line argument(s)')
for arg in sys.argv[1:]:
  if arg == '--viz':
    viz = True
  else:
    if random_seed == -1:
      #print('Attempting to use this random seed:', arg)
      random_seed = int(arg)
      random.seed(random_seed)
    else:
      print('Error! Unknown argument (or too many random seeds):', arg)
      print('Exiting')
      quit(1)

if viz:
  print('')
  print('Attempting to run the visualizer!')
  print('If you run into an error about not having pygame, try this:')
  print('python3 -m pip install pygame')
  print('Note you might have to use admin privileges:')
  print('sudo python3 -m pip install pygame')
  print('')
  import pygame


class Pokemon:
  def __init__(self, num, name, type_1, type_2, bst):
    self.num = int(num)
    self.name = name
    self.type_1 = type_1
    self.type_2 = type_2
    self.bst = int(bst)

  def __str__(self):
    return self.name + '(' + str(self.bst) + ')'

  def get_attack_score(self, other, type_chart):
    type_sum = 1
    type_sum *= type_chart[self.type_1][other.type_1]
    if other.type_2 != '':
      type_sum *= type_chart[self.type_1][other.type_2]
    if self.type_2 != '':
      type_sum *= type_chart[self.type_2][other.type_1]
      if other.type_2 != '':
        type_sum *= type_chart[self.type_2][other.type_2]
    return type_sum


  def compare(self, other, type_chart):
    type_sum = self.get_attack_score(other, type_chart)
    type_sum -= other.get_attack_score(self, type_chart)
    if type_sum != 0:
      return type_sum > 0
    return self.bst > other.bst


def read_pokemon_list(filename):
  L = []
  with open(filename, 'r') as fp:
    for line in fp:
      line = line.strip()
      if line == '':
        continue
      line_parts = line.split(',')
      L.append(Pokemon(*line_parts[0:5]))
    return L

def load_type_chart(filename):
  D = {}
  with open(filename, 'r') as fp:
    header = fp.readline().strip()
    type_order = header.split(',')[1:]
    for line in fp:
      line = line.strip()
      if line == '':
        continue
      line_parts = line.split(',')
      attacking_type = line_parts[0]
      D[attacking_type] = {}
      for type_idx in range(len(type_order)):
        defending_type = type_order[type_idx]
        D[attacking_type][defending_type] = float(line_parts[type_idx + 1])
  return D

def verify_collapsed(pop):
  num = pop[0]
  for p in pop:
    if p != num:
      return False
  return True

def get_new_gen(pop, pokemon_list, type_chart, w, h):
  order = list(range(len(pop)))
  random.shuffle(order)
  new_pop = copy.deepcopy(pop)
  for idx in order:
    x = idx % w
    y = idx // w
    target = random.randint(0, 7)
    target_x = x
    target_y = y
    # Up
    if target == 0 or target == 1 or target == 2:
      target_y -= 1
      if target_y < 0:
        target_y = h - 1
    # Down
    elif target == 5 or target == 6 or target == 7:
      target_y += 1
      if target_y >= h:
        target_y = 0
    # Left
    if target == 0 or target == 3 or target == 5:
      target_x -= 1
      if target_x < 0:
        target_x = w - 1
    # Right
    if target == 2 or target == 4 or target == 7:
      target_x += 1
      if target_x >= w:
        target_x = 0
    target_idx = target_x + target_y * w
    cur_mon = pokemon_list[pop[idx]]
    target_mon = pokemon_list[pop[target_idx]]
    if cur_mon.compare(target_mon, type_chart):
      new_pop[target_idx] = pop[idx]
  return new_pop

def get_color(pokemon, type_id):
  type_name = pokemon.type_1
  if type_id == 2:
    type_name = pokemon.type_2
  color_map = {
      'Normal': (200, 200, 200), 
      'Fire': (200, 100, 20),
      'Water': (20, 100, 200), 
      'Electric': (200, 200, 0), 
      'Grass': (0, 200, 50), 
      'Ice': (0, 150, 200), 
      'Fighting': (150, 100, 0), 
      'Poison': (100, 0, 100), 
      'Ground': (200, 150, 0), 
      'Flying': (0, 200, 200), 
      'Psychic': (200, 0, 150),
      'Bug': (150, 200, 0),
      'Rock': (100, 100, 100), 
      'Ghost': (50, 50, 100), 
      'Dragon': (200, 150, 0),
      'Dark': (0, 0, 0), 
      'Steel': (225, 225, 225), 
      'Fairy': (200, 0, 200)
      }
  return color_map[type_name]

def print_leader(pop, cur_gen, pokemon_list):
  D = {}
  highest_count = 0
  leader_id = 0
  for id in pop:
    if id not in D:
      D[id] = 0
    D[id] += 1
    if D[id] > highest_count:
      highest_count = D[id]
      leader_id = id
  leader_mon = pokemon_list[leader_id]
  print(str(cur_gen) + ',' + \
      str(highest_count) +  ',' + \
      str(leader_mon.name) +  ',' + \
      str(leader_mon.num) +  ',' + \
      str(leader_mon.type_1) + ',' +  \
      str(leader_mon.type_2) + ',' + \
      str(leader_mon.bst))

def print_header():
  print('update,count,name,num,type_1,type_2,bst')



if __name__ == '__main__':

  pokemon_list = read_pokemon_list('pokemon_filtered.csv')
  type_map = load_type_chart('type_chart.csv')
  random.shuffle(pokemon_list)
  grid_width = 12
  grid_height = 12
  
  pop = list(range(144))
  random.shuffle(pop)
  print_header()

  if not viz:
    cur_gen = 0
    while not verify_collapsed(pop) and cur_gen < 1000:
      pop = get_new_gen(pop, pokemon_list, type_map, grid_width, grid_height)
      print_leader(pop, cur_gen, pokemon_list)
      cur_gen += 1
  
  if viz:
    pygame.init()
    tile_size = 70
    screen_size = grid_width * tile_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('arial', 12)
    is_running = True
    auto_play = False
    timer_max = 0.2
    frame_timer = timer_max
    cur_gen = 0
    while is_running and cur_gen < 1000:
      for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
          is_running = False
        if evt.type == pygame.KEYDOWN:
          if evt.key == pygame.K_q or evt.key == pygame.K_ESCAPE:
            is_running = False
          elif evt.key == pygame.K_SPACE:
            pop = get_new_gen(pop, pokemon_list, type_map, grid_width, grid_height)
            print_leader(pop, cur_gen, pokemon_list)
            cur_gen += 1
          elif evt.key == pygame.K_p:
            auto_play = not auto_play
            frame_timer = timer_max
      screen.fill((0,0,0))
      for idx in range(len(pop)):
        x = idx % grid_width
        y = idx // grid_height
        pokemon = pokemon_list[pop[idx]]
        color = get_color(pokemon, 1)
        pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))
        text_surf = font.render(pokemon.name, True, (0,0,0), (255,255,255))
        text_rect = text_surf.get_rect()
        text_rect.center = (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2)
        screen.blit(text_surf, text_rect)
      pygame.display.flip()
      if auto_play:
        delta_time = clock.tick(60) / 1000
        frame_timer -= delta_time
        if frame_timer < 0:
          frame_timer = timer_max
          pop = get_new_gen(pop, pokemon_list, type_map, grid_width, grid_height)
          print_leader(pop, cur_gen, pokemon_list)
          cur_gen += 1

