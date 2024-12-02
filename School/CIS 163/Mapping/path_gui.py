# get the png files and paste in images folder
import pygame as pg
from game import *
import copy
import time
import random

IMAGE_SIZE = 52  # small format - images 52 X 52
IMAGES = {}

# Define custom event types
VARIABLE_CHANGE = pg.USEREVENT + 1

class GUI:
    def __init__(self):
        # Initializing the pygame
        pg.init()
        board = []
        self.max_width = 0
        self.max_height = 0
        # initializes the map
        for i in range(random.randint(10, 16)):
            row = []
            # having random rows for uneven board structure
            cols = random.randint(4, 20)
            if self.max_width < cols:
                self.max_width = cols
            for j in range(cols):
                # selecting random choice of ocean and grass
                # grass repesents land and ocean represents the block
                row.append(random.choices(['grass', 'ocean'], [5, 1], k = 1)[0])
            board.append(row)
        self.actual_board = copy.deepcopy(board)
        self.get_start_point()
        self.get_end_point()
        self.max_height = len(self.actual_board)
        self._gs = Map(board, self._start_point, self._end_point)

        # Initalizes thhe screen with given width and height
        self._screen = pg.display.set_mode((self.max_width * IMAGE_SIZE + IMAGE_SIZE * 2 , self.max_height * IMAGE_SIZE + IMAGE_SIZE * 2))
        # # Sets the heading
        pg.display.set_caption("Laker finding path")
        self._screen.fill("black")

    # will get the start point by randomly picking a location on the grid
    def get_start_point(self):
        height = len(self.actual_board)
        start_row = random.randint(0, height - 1)
        # setting the starting point
        self._start_point = (start_row, random.randint(0, len(self.actual_board[start_row]) - 1))
        # randomly selecting from the rows
        while self.actual_board[self._start_point[0]][self._start_point[1]] == 'ocean':
            start_row = random.randint(0, height - 1)
            # setting the starting point
            self._start_point = (start_row, random.randint(0, len(self.actual_board[start_row]) - 1))

    # will get the end point ensuring it is not start point by randomly picking a location
    def get_end_point(self):
        width = 0
        height = len(self.actual_board)
        for i in self.actual_board:
            if len(i) > width:
                width = len(i)
        end_row = random.randint(0, height - 1)
        self._end_point = (end_row, random.randint(0, len(self.actual_board[end_row]) - 1))
        while self._start_point == self._end_point or self.actual_board[self._end_point[0]][self._end_point[1]] == 'ocean':
            end_row = random.randint(0, height - 1)
            self._end_point = (end_row, random.randint(0, len(self.actual_board[end_row]) - 1))

    # will load images in the global dictionary
    # should be called only once as this operation is expensive
    @classmethod
    def load_images(self):
        IMAGES['grass'] = pg.transform.scale(pg.image.load('c:/Users/joshu/Coding Projects/School/CIS 163/Mapping/images/grass.png'), (IMAGE_SIZE, IMAGE_SIZE))
        IMAGES['ocean'] = pg.transform.scale(pg.image.load('c:/Users/joshu/Coding Projects/School/CIS 163/Mapping/images/ocean.png'), (IMAGE_SIZE, IMAGE_SIZE))
        IMAGES['start'] = pg.transform.scale(pg.image.load('c:/Users/joshu/Coding Projects/School/CIS 163/Mapping/images/start.png'), (IMAGE_SIZE, IMAGE_SIZE))
        IMAGES['end'] = pg.transform.scale(pg.image.load('c:/Users/joshu/Coding Projects/School/CIS 163/Mapping/images/end.png'), (IMAGE_SIZE, IMAGE_SIZE))
        IMAGES['human'] = pg.transform.scale(pg.image.load('c:/Users/joshu/Coding Projects/School/CIS 163/Mapping/images/human.jpg'), (IMAGE_SIZE, IMAGE_SIZE))
        # IMAGES['sand'] = pg.transform.scale(pg.image.load('./images/sand.jpg'), (IMAGE_SIZE, IMAGE_SIZE))

    def __draw_board__(self, gameState, screen):
        # to draw squares on the board(can be different function)
        #colors = [(119,171,89), (125,202,249)]
        for i in range(len(self._gs.grid)):
            for j in range(len(self._gs.grid[i])):
                piece = IMAGES[self._gs.grid[i][j]]
                if (i, j) == self._gs.start_coords:
                    piece = IMAGES['start']
                elif (i, j) == self._gs.end_coords:
                    piece = IMAGES['end']
                screen.blit(piece, pg.Rect(j * IMAGE_SIZE, i * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE))

    def run_game_on_board(self):
        # Draw initial board
        self.__draw_board__(self._gs, self._screen)
        pg.display.flip()

        time.sleep(2)

        # Uncomment the following code once you have your find_path function returning path
        path = self._gs.find_shortest_path()
        print(self.actual_board)
        print(path)
        
        # If no path is found, display "No Path Found" message
        if path is None:
            font = pg.font.SysFont("Arial", 36)
            txtsurf = font.render("No Path Found", True, 'white')
            self._screen.blit(txtsurf, (self._screen.get_width() // 2 - txtsurf.get_width() // 2,
                                        self._screen.get_height() - 2 * txtsurf.get_height()))
            pg.display.flip()
            time.sleep(2)  # Keep message on screen for 3 seconds
            return
        curr = path._LLStack__head
        lst_path = []
        # print(curr._Node__data, curr._Node__next)
        while curr != None:
            # print(curr.data)
            lst_path.append(curr.data)
            curr = curr.next
        lst_path = lst_path[::-1]
        lst_path = lst_path[1:]
        prev = []
        # Animate the human movement along the found path
        for pos in lst_path:
            i, j = pos

            # Clear the screen and redraw the board
            #
            if len(prev) != 0:
                self._screen.blit(IMAGES[prev[2]], pg.Rect(prev[1] * IMAGE_SIZE, prev[0] * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE))
                pg.display.flip()
                # self._gs.board[prev[0]][prev[1]] = prev[2]

            prev = [i, j, self.actual_board[i][j]]
            # # Draw the human at the current position
            self._screen.blit(IMAGES['human'], pg.Rect(j * IMAGE_SIZE, i * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE))

            # Update the display
            pg.display.flip()

            # Delay to create animation effect
            time.sleep(0.5)  # Adjust the time to control the speed of animation

        # Display "Path Found" message after reaching the end
        font = pg.font.SysFont("Arial", 36)
        txtsurf = font.render("Path Completed!", True, 'white')
        self._screen.blit(txtsurf, (self._screen.get_width() // 2 - txtsurf.get_width() // 2,
                                    self._screen.get_height() - 2 * txtsurf.get_height()))
        pg.display.flip()
        time.sleep(2)  # Keep message on screen for 2 seconds

def main():
    g = GUI()
    g.load_images()
    g.run_game_on_board()


#proper notation
if __name__ == '__main__':
    main()
