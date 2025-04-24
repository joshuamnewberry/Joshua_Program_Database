import pygame

pygame.init()
dim_str = input()
dim_parts = dim_str.split(':')[1].strip().split('x')
width = int(dim_parts[0])
height = int(dim_parts[1])
print(f'Detected dimensions as {width}x{height}')
step_str = input()
num_steps = int(step_str.split()[3])
rule_str = input()
_ = input()

data = []

for i in range(num_steps):
  step_data = []
  for row in range(height):
    line_str = input()
    step_data.append(line_str.strip())
  _ = input()
  data.append(step_data)

screen_width = 800
screen_height = 800
cell_width = screen_width // width
cell_height = screen_height // height

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
fps_clock = pygame.time.Clock()
step_idx = 0
done = False
while not done:
  for evt in pygame.event.get():
    if evt.type == pygame.QUIT:
      done = True
    elif evt.type == pygame.KEYDOWN:
      if evt.key == pygame.K_q or evt.key == pygame.K_ESCAPE:
        done = True

  screen.fill((0,0,0))
  for row_idx in range(height):
    row_str = data[step_idx][row_idx]
    for col_idx in range(width):
      if row_str[col_idx] == '#':
        pygame.draw.rect(screen, (255,255,255), (cell_width * col_idx, cell_height * row_idx, cell_width, cell_height))
  

  pygame.display.flip()
  step_idx += 1
  if step_idx >= len(data):
    step_idx = 0
  fps_clock.tick(20)
