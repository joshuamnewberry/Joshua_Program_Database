from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any
from enum import Enum
from random import randint
from coord import Coord

class CharacterDeath(Exception):
    """
    Custom Exception for Character Deaths

    """

    def __init__(self, msg:str, char:Character) -> None:
        """
        Initialize the object, store the message and set the character"s temp health back to zero

        Parameters:
        msg:str the message to be printed
        char:Character the character who died, their temp_health will be set to zero

        Return:
        None

        """

        # Store variables
        self.message = msg
        char.temp_health = 0
    
    def __str__(self) -> str:
        """
        Return the message

        Parameters:
        None

        Return:
        self.message:str The stored message

        """
        # Return message
        return self.message

class Player(Enum):
    """
    Enumerator class used to denote Player association

    """
    VILLAIN = 0
    HERO = 1

class Character(ABC):
    """
    Abstract Parent Class for all Creatures

    """
    def __init__(self, player:Player) -> None:
        """
        Initialize the object, check player is type Player and store initial variable values
        
        Parameters:
        player:Player Player type of the Character (Hero or Villain)

        Return:
        None

        """

        # Check Player Type
        if type(player) != Player:
            raise TypeError("Expected a Player Type")
        # Store Player
        self.__player = player
        # Store Default values
        self.__health = 5
        self.__temp_health = 5
        self.__attack = 3
        self.__defense = 3
        self.__move = 3
        self.__range = 1
    
    def __str__(self) -> str:
        """
        Return the Class name

        Parameters:
        None

        Return:
        self.__class__.__name__:str the class name of the object
        
        """
        # Return Class name
        return self.__class__.__name__
    
    def integerType(num:Any) -> None:
        """
        Raise a TypeError if num is not an Integer

        Parameters:
        num:Any 

        Return:
        None

        """

        # Raise Type Error if not an int
        if type(num) != int:
            raise TypeError(f"{num} is not an integer")
    
    @property
    def player(self) -> Player:
        """
        Get or Set player variable

        Parameters:
        player:Player if passed will be the new player type

        Return:
        self.__player if getting will return player type

        """

        # Return Player type
        return self.__player
    @player.setter
    def player(self, player:Player) -> None:
        # Raise Type Error if not an int
        if type(player) != Player:
            raise TypeError(f"Expected a Player Type")
        # Store player type
        self.__player = player
    
    @property
    def health(self) -> int:
        """
        Get or Set health variable, check int type and greater than 0

        Parameters:
        health:int if passed will be the new health

        Return:
        self.__health if getting will return health

        """

        # Return Health num
        return self.__health
    @health.setter
    def health(self, health:int) -> None:
        # Check int type and greater than zero
        Character.integerType(health)
        if health <= 0:
            raise ValueError("Expected a number greater than 0")
        # Store Health num
        self.__health = health
    
    @property
    def temp_health(self) -> int:
        """
        Get or Set temp_health variable, check int type, if less than zero raise CharacterDeath exception

        Parameters:
        temp_health:int if passed will be the new temp_health

        Return:
        self.__temp_health if getting will return temp_health

        """

        # Return Temp__Health num
        return self.__temp_health
    @temp_health.setter
    def temp_health(self, temp_health:int) -> None:
        # Check int type
        Character.integerType(temp_health)
        # Store Temp_Health num
        self.__temp_health = temp_health
        # If temp_health is less than 0 raise CharacterDeath
        if self.__temp_health < 0:
            raise CharacterDeath(f"{self} has died", self)
    
    @property
    def combat(self) -> list:
        """
        Get or Set attack and defense variables, check int type, length of 2, greater than or equal to 0

        Parameters:
        combat:list if passed will set the new attacka and defense values

        Return:
        [self.__attack, self.__defense] will return attack and defense variables in a list of length 2

        """
        # Return attack and defense as a list
        return [self.__attack, self.__defense]
    @combat.setter
    def combat(self, combat:list) -> None:
        # Check combat is list
        if type(combat) != list:
            raise TypeError("Expected a list")
        # Check length of 2
        if len(combat) != 2:
            raise ValueError("Expected a length 2 list")
        # Check integer type
        Character.integerType(combat[0])
        Character.integerType(combat[1])
        # Check greater than or equal to zero
        if combat[0] < 0:
            raise ValueError(f"{combat[0]} is not greater or equal to 0 ")
        if combat[1] < 0:
            raise ValueError(f"{combat[1]} is not greater or equal to 0 ")
        # Store values
        self.__attack = combat[0]
        self.__defense = combat[1]
    
    @property
    def move(self) -> int:
        """
        Get or Set move variable, check int type, greater than 0

        Parameters:
        move:int if passed will be the new move value

        Return:
        self.__move if getting will return move

        """

        # Return move num
        return self.__move
    @move.setter
    def move(self, move:int) -> None:
        # Check int type
        Character.integerType(move)
        # Check greater than zero
        if move <= 0:
            raise ValueError
        # Store move num
        self.__move = move
    
    @property
    def range(self) -> int:
        """
        Get or Set range variable, check int type, greater than 0

        Parameters:
        range:int if passed will be the new range value

        Return:
        self.__range if getting will return range

        """
        
        # Return range num
        return self.__range
    @range.setter
    def range(self, range:int) -> None:
        # Check int type
        Character.integerType(range)
        # Check greater than zero
        if range <= 0:
            raise ValueError
        # Store range num
        self.__range = range
    
    @abstractmethod
    def is_valid_move(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the move is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """

        # Check from_cood not equal to to_coord
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        # Store height and width variables
        height = len(board)-1
        width = len(board[0])-1
        # Check x and y less than zero
        if from_coord.x < 0 or to_coord.x < 0 or from_coord.y < 0 or to_coord.y < 0:
            return False
        # Check x and y greater than height and width
        if from_coord.x > height or to_coord.x > height or from_coord.y > width or to_coord.y > width:
            return False
        # Check from_coord equal to self
        if board[from_coord.x][from_coord.y] != self:
            return False
        # Check to_coord is empty
        if board[to_coord.x][to_coord.y] != None:
            return False
        # If arrive here return True
        return True
    
    @abstractmethod
    def is_valid_attack(self, from_coord:Coord, to_coord:Coord, board:List[List[None|Character]]) -> bool:
        """
        Return True if the attack is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the target
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False
        
        """
        # Check from_cood not equal to to_coord
        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:
            return False
        # Store height and width variables
        height = len(board)-1
        width = len(board[0])-1
        # Check x and y less than zero
        if from_coord.x < 0 or to_coord.x < 0 or from_coord.y < 0 or to_coord.y < 0:
            return False
        # Check x and y greater than height and width
        if from_coord.x > height or to_coord.x > height or from_coord.y > width or to_coord.y > width:
            return False
        # Check from_coord equal to self
        if board[from_coord.x][from_coord.y] != self:
            return False
        # Check to_coord contains Character
        if not isinstance(board[to_coord.x][to_coord.y], Character):
            return False
        # If arrive here return True
        return True
    
    @abstractmethod
    def calculate_dice(self, target:Character, attack:bool = True, lst:list = None, *args, **kwargs) -> int:
        """
        Return  the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num:int number of sucessful rolls
        
        """

        # Create sucess_num variable
        sucess_num = 0
        # Grab dice num based on attack bool
        dice_num = self.combat[int(not attack)]
        # Create compare = 3
        compare = 3
        # If attacking compare = 4
        if attack:
            compare = 4
        # If no list is passed create a list
        if lst is None:
            lst = []
            # Add values to the list up to the dice num
            for _ in range(0, dice_num):
                # Random values from 1 to 6
                lst.append(randint(1, 6))
        # Loop over values up to the dice_num
        for i in range(0, dice_num):
            # Compare the value to the compare variable
            if lst[i] > compare:
                # Add one to sucess_num
                sucess_num += 1
        # Return number of sucessfully rolled dice
        return sucess_num
    
    @abstractmethod
    def deal_damage(self, target:Character, damage:int, *args, **kwargs) -> None:
        """
        Subtract damage from target.temp_health and print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None
        
        """

        # Print damage dealt
        print(f"{target.__class__.__name__} was dealt {damage} damage")
        try:
            # Modify temp health
            target.temp_health -= damage
        except CharacterDeath as msg:
            # If character death occurs print the message
            print(msg)