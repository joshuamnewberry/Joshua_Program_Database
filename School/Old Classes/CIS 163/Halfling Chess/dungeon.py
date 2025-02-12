from creatures import *
from coord import *
import random


class Dungeon:
    def boardLength(num) -> None:
        """
                Validate the board length.

                Parameters:
                num (int): The intended length of the board.

                Raises:
                TypeError: If `num` is not an integer.
                ValueError: If `num` is less than 4 or greater than 12.

                Returns:
                None
                """
        if not isinstance(num, int):
            raise TypeError(f'Board length must be an integer')
        if num < 4:
            raise ValueError(f"Board length must be at least 4")
        if num > 12:
            raise ValueError(f'Board length must be no more than 12')

    def __init__(self, height: int, width: int, villains: List[Villain] = []) -> None:
        """
               Initialize the Dungeon object with dimensions, heroes, and villains.

               Parameters:
               height (int): The height of the dungeon grid.
               width (int): The width of the dungeon grid.
               villains (List[Villain]): Optional; list of villain instances to place in the dungeon.

               Raises:
               TypeError: If `villains` is not a list or contains non-Villain instances.

               Returns:
               None
               """
        Dungeon.boardLength(height)
        Dungeon.boardLength(width)
        self.__height = height
        self.__width = width
        board = [[None for i in range(width)] for i in range(height)]
        if not isinstance(board, list) or not all(isinstance(row, list) for row in board):
            raise TypeError("Board must be a list of lists")
        self.__board = board
        self.__player = Player.HERO
        self.__heroes = [Warrior(), Mage(), Paladin(), Ranger()]
        if villains == []:
            self.__villains = self.generate_villains()
        else:
            if not isinstance(villains, list):
                raise TypeError("Villains must be a list")
            if not all(isinstance(villain, Villain) for villain in villains):
                raise TypeError("All elements in the villains list must be instances of Villain")
            self.__villains = villains

    @property
    def height(self) -> int:
        """
               Retrieve the dungeon height.

               Returns:
               int: The dungeon grid height.
               """
        return self.__height

    @property
    def width(self) -> int:
        """
                Retrieve the dungeon width.

                Returns:
                int: The dungeon grid width.
                """
        return self.__width

    @property
    def board(self) -> List[List[None | Character]]:
        """
               Retrieve the dungeon board.

               Returns:
               List[List[None | Character]]: The 2D list representing the dungeon layout.
               """
        return self.__board

    @board.setter
    def board(self, board):
        """
                Set a new dungeon board layout.

                Parameters:
                board (List[List[None | Character]]): The 2D list representing the new layout.

                Returns:
                None
                """
        self.__board = board

    @property
    def player(self) -> Player:
        """
              Retrieve the current player.

              Returns:
              Player: The current player, either HERO or VILLAIN.
              """
        return self.__player

    @property
    def heroes(self) -> List[Hero]:
        """
                Retrieve the list of hero characters.

                Returns:
                List[Hero]: List of heroes in the dungeon.
                """
        return self.__heroes

    @heroes.setter
    def heroes(self, heroes: List[Hero]) -> None:
        """
                Set a new list of heroes for the dungeon.

                Parameters:
                heroes (List[Hero]): The new list of hero characters.

                Raises:
                TypeError: If `heroes` is not a list of Hero instances.

                Returns:
                None
                """
        if not isinstance(heroes, list) or not all(isinstance(hero, Hero) for hero in heroes):
            raise TypeError("Expected a list of heroes")
        self.__heroes = heroes

    @property
    def villains(self) -> List[Hero]:
        """
        Retrieve the list of villains in the dungeon.

        Returns:
        List[Hero]: List of villains in the dungeon.
        """

        return self.__villains

    @villains.setter
    def villains(self, villains: List[Villain]) -> None:
        """
        Set a new list of villains for the dungeon.

        Parameters:
        villains (List[Villain]): The new list of villain characters.

        Returns:
        None
        """
        if not isinstance(villains, list):
            raise TypeError
        self.__villains = villains

    def is_valid_move(self, coords: List[Coord]) -> bool:
        """
        Check if a move is valid between two coordinates.

        Parameters:
        coords (List[Coord]): List containing the starting and destination coordinates.

        Raises:
        ValueError: If there is no character at the starting coordinate or if the destination is occupied.

        Returns:
        bool: True if the move is valid, otherwise False.
        """
        from_coord, to_coord = coords[0], coords[1]
        character = self.board[from_coord.x][from_coord.y]
        if character is None:
            raise ValueError(f"No character at {from_coord}")

        if self.board[to_coord.x][to_coord.y] is not None:
            raise ValueError(f"Cannot move to {to_coord} as it is already occupied by another character.")

        return character.is_valid_move(from_coord, to_coord, self.board)
    def is_valid_attack(self, coords: List[Coord]) -> bool:
        """
        Check if an attack is valid from a given coordinate.

        Parameters:
        coords (List[Coord]): The attacking character's coordinates.

        Raises:
        ValueError: If there is no character at the given coordinates.

        Returns:
        bool: True if the attack is valid, otherwise False.
        """
        from_coord, to_coord = coords[0], coords[1]
        character = self.board[from_coord.x][from_coord.y]
        if character is None:
            raise ValueError(f"No character at ({from_coord.x}, {from_coord.y}")
        return character.is_valid_attack(from_coord, to_coord, self.board)

    def character_at(self, x: int, y: int) -> Character:
        """
        Retrieve the character at a specific position on the board.

        Parameters:
        x (int): The row coordinate.
        y (int): The column coordinate.

        Raises:
        ValueError: If `x` or `y` are out of bounds.

        Returns:
        Character: The character at the given position.
        """
        # Check the coordinates
        if x < 0 or x >= self.__height:
            raise ValueError(f"x {x} is out of bounds.")
        if y < 0 or y >= self.__width:
            raise ValueError(f"y {y} is out of bounds.")

        # Get the character
        character = self.__board[x][y]

        # Return the character
        return character

    def set_character_at(self, target: Character, x: int, y: int) -> None:
        """
        Place a character at specific coordinates.

        Parameters:
        target (Character): The character to place.
        x (int): The row coordinate.
        y (int): The column coordinate.

        Raises:
        ValueError: If coordinates are out of bounds or if the position is occupied.

        Returns:
        None
        """
        # Check if in bounds
        if x < 0 or x >= self.__height:
            raise ValueError(f"x {x} is out of bounds.")
        if y < 0 or y >= self.__width:
            raise ValueError(f"y {y} is out of bounds.")

        # Check if the target position is already occupied
        if self.__board[x][y] is not None:
            raise ValueError(
                f"Cannot place character at ({x}, {y}) because it is already occupied by {self.__board[x][y]}.")

        # Place character at the specified coordinates
        self.__board[x][y] = target

    def move(self, from_coord: Coord, to_coord: Coord) -> None:
        """
        Move a character from one coordinate to another.

        Parameters:
        from_coord (Coord): The starting coordinates.
        to_coord (Coord): The destination coordinates.

        Returns:
        None
        """
        # Check if a character is at the from_coord
        character = self.__board[from_coord.x][from_coord.y]
        # Move the character
        self.__board[to_coord.x][to_coord.y] = character
        # Clear the original position
        self.__board[from_coord.x][from_coord.y] = None

    def attack(self, from_coord: Coord, to_coord: Coord) -> None:
        """
        Perform an attack between two coordinates.

        Parameters:
        from_coord (Coord): The attacker's coordinates.
        to_coord (Coord): The defender's coordinates.

        Raises:
        ValueError: If the attack is invalid or there is no attacker/defender at the specified coordinates.

        Returns:
        None
        """
        # Get the attacker and defender
        attacker = self.__board[from_coord.x][from_coord.y]
        defender = self.__board[to_coord.x][to_coord.y]

        # Check if there is a valid attacker and defender
        if not isinstance(attacker, Character):
            raise ValueError(f"No valid attacker at {from_coord}.")
        if not isinstance(defender, Character):
            raise ValueError(f"No valid defender at {to_coord}.")

        # Check if the attack is valid
        if not self.is_valid_attack([from_coord, to_coord]):
            raise ValueError(f"Invalid attack move from {from_coord} to {to_coord}.")

        # Calculate damage
        attack = attacker.calculate_dice(defender)
        defense = defender.calculate_dice(attacker, False)

        # Determine damage
        damage = attack - defense

        # Deal damage to the defender
        if damage >= 0:
            attacker.deal_damage(defender, damage)
        elif damage < 0:
            defender.deal_damage(attacker, damage)

        # Set the next player
        self.set_next_player()

    def set_next_player(self) -> None:
        """
        Switch to the next player.

        Returns:
        None
        """
        if self.__player == Player.HERO:
            self.__player = Player.VILLAIN
        else:
            self.__player = Player.HERO

    def print_board(self) -> None:
        """
        Print the current state of the board.

        Returns:
        None
        """
        st = ' \t'
        st += '_____' * len(self.board)
        st += '\n'
        for i in range(len(self.__board)):
            st += f'{i}\t'
            for j in range(len(self.__board[i])):
                if self.board[i][j] is None:
                    st += '|___|'
                else:
                    st += f'|{self.board[i][j].__class__.__name__[:3]}|'
            st += '\n'
        st += '\t'
        for i in range(len(self.board[0])):
            st += f'  {i}  '
        print(st)

    def is_dungeon_clear(self) -> bool:
        """
        Check if all villains have been defeated.

        Returns:
        bool: True if all villains are defeated (temp_health <= 0), otherwise False.
        """
        for i in range(len(self.__board)):
            for j in range(len(self.__board[0])):
                if isinstance(self.__board[i][j], Villain):
                    if self.__board[i][j].temp_health > 0:
                        return False
        return True


    def adventurer_defeat(self) -> bool:
        """
        Check if all heroes have been defeated.

        Returns:
        bool: True if all heroes are defeated, otherwise False.
        """
        for i in range(len(self.__board)):
            for j in range(len(self.__board[0])):
                if isinstance(self.__board[i][j], Hero):
                    if self.__board[i][j].temp_health > 0:
                        return False
        return True

    def generate_villains(self) -> None:
        """
        Generate a list of villains to place in the dungeon.

        Returns:
        None
        """
        high = max(self.height, self.width)
        num_villains = random.randint(1, high)
        self.__villains = []  # Reset the villains list
        necromancer_added = False  # necromancer tracker

        for i in range(num_villains):
            roll = random.randint(1, 10)
            if 1 <= roll <= 5:  # 50% chance for Goblin
                self.__villains.append(Goblin())
            elif 6 <= roll <= 8:  # 30% chance for Skeleton
                self.__villains.append(Skeleton())
            elif 9 <= roll <= 10:  # 20% chance for Necromancer
                if necromancer_added == False:
                    self.__villains.append(Necromancer())
                    necromancer_added = True # Show that a necromanser has been added
                else:
                    self.__villains.append(Skeleton())  # Add a Skeleton instead


    def place_heroes(self) -> None:
        """
        Position heroes on the board.

        Returns:
        None
        """
        mid = self.__width // 2  # Calculate middle

        if self.__width % 2 == 0:  #Even
            #Penultimate row
            self.__board[self.__height - 2][mid - 1] = self.__heroes[0]  #Warrior
            self.__board[self.__height - 2][mid] = self.__heroes[2]  #Paladin
            #Last row
            self.__board[self.__height - 1][mid - 1] = self.__heroes[1]  #Mage
            self.__board[self.__height - 1][mid] = self.__heroes[3]  #Ranger
        else:  #Odd
            #Penultimate row
            self.__board[self.__height - 2][mid] = self.__heroes[0]  #Warrior
            #Last row
            self.__board[self.__height - 1][mid - 1] = self.__heroes[1]  #Mage
            self.__board[self.__height - 1][mid] = self.__heroes[2]  #Paladin
            self.__board[self.__height - 1][mid + 1] = self.__heroes[3]  #Ranger

    def place_villains(self) -> None:
        """
        Position villains on the board.

        Returns:
        None
        """
        for villain in self.__villains:
            placed = False
            while not placed:
                # Randomize a row
                row = random.randint(0, self.__height - 3)
                # Randomize a column
                col = random.randint(0, self.__width - 1)

                # Check if empty
                if self.__board[row][col] is None:
                    # Place the villain
                    self.__board[row][col] = villain
                    placed = True

    def generate_new_board(self, height: int = -1, width: int = -1) -> None:
        """
        Create a new board with updated dimensions and positions for characters.

        Parameters:
        height (int): Optional; the new board height. Defaults to -1 (randomly chosen).
        width (int): Optional; the new board width. Defaults to -1 (randomly chosen).

        Returns:
        None
        """
        # Randomize height and width
        if height == -1 or width == -1:
            height = random.randint(4, 12)
            width = random.randint(4, 12)

        # Reset the board
        self.__board = [[None for i in range(self.__width)] for i in range(self.__height)]

        # Generate new villains
        self.generate_villains()

        # Place heroes
        self.place_heroes()

        # Place villains
        self.place_villains()

# d = Dungeon(5,7)
# d.generate_new_board()
# from_coord = Coord(3, 3)
# to_coord = Coord(0, 3)
# print(d.print_board())
# print(d.is_valid_move(from_coord, to_coord))
# d.move(from_coord, to_coord)
# print(d.is_dungeon_clear())
# print(d.adventurer_defeat())
# d.set_character_at(Skeleton(), 3, 2)
# print(d.print_board())
# print(d.character_at(3, 3))
# print(d.character_at(3, 2))
# print(d.character_at(2, 3))
# print(d.character_at(1, 2))