from character import *

class Villain(Character):
    """
    Parent Class for all Villains

    """
    def __init__(self) -> None:
        """
        Initialize the object with Player type Player.VILLAIN

        Parameters:
        None

        Return :
        None

        """

        # Initialize the parent class with Player type Villain
        super().__init__(Player.VILLAIN)

    def __str__(self) -> str:
        # Return parent class string method
        return super().__str__()

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[None | Character]]) -> bool:
        """
        Return True if the move is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False

        """

        # If passes all Character valid move cases
        if super().is_valid_move(from_coord, to_coord, board):
            # And is moving less than or equal to self.move in x and y
            if abs(to_coord.x - from_coord.x) <= self.move and abs(to_coord.y - from_coord.y) <= self.move:
                # And is moving only in the y direction
                if from_coord.x == to_coord.x:
                    # And not colliding with anything on the way
                    for y in range(min(from_coord.y, to_coord.y) + 1, max(from_coord.y, to_coord.y)):
                        # If we collide with something return False
                        if board[from_coord.x][y] != None:
                            return False
                    # Then return True
                    return True
                # Or is moving only in the x direction
                elif from_coord.y == to_coord.y:
                    # And not colliding with anything on the way
                    for x in range(min(from_coord.x, to_coord.x) + 1, max(from_coord.x, to_coord.x)):
                        # If we collide with something return False
                        if board[x][from_coord.y] != None:
                            return False
                    # Then return True
                    return True
        # If we fail any condtitions return False
        return False

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[None | Character]]) -> bool:
        """
        Return True if the attack is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the target
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False

        """

        # If passes all Character valid attack cases
        if super().is_valid_attack(from_coord, to_coord, board):
            # And is attacking in one straight line direction
            if from_coord.x == to_coord.x or from_coord.y == from_coord.y:
                # And is attacking less than or equal to self.range in x and y
                if abs(to_coord.x - from_coord.x) <= self.range and abs(to_coord.y - from_coord.y) <= self.range:
                    # Then return True
                    return True
        # If we fail any condtitions return False
        return False

    def calculate_dice(self, target: Character, attack: bool = True, lst: list = None, *args, **kwargs) -> int:
        """
        Return  the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num:int number of sucessful rolls

        """

        # Return calculate dice of the parent class
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        """
        Subtract damage from target.temp_health and print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None

        """

        # Execute deal damage of the parent class
        super().deal_damage(target, damage)

class Goblin(Villain):
    def __init__(self) -> None:
        """
        Initialize the object as a Villain, set specific property values

        Parameters:
        None

        Return :
        None

        """

        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]

class Skeleton(Villain):
    def __init__(self) -> None:
        """
        Initialize the object as a Villain, set specific property values

        Parameters:
        None

        Return :
        None

        """

        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2

class Necromancer(Villain):
    def __init__(self) -> None:
        """
        Initialize the object as a Villain, set specific property values

        Parameters:
        None

        Return :
        None

        """
        
        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.combat = [1, 2]
        self.range = 3

    def raise_dead(self, target: Character, from_coord: Coord, to_coord: Coord,
                   board: List[List[None | Character]]) -> None:
        """
        Check prereqs, and set player type to Player.VILLAIN and temp.health to health/2 rounded down

        Parameters:
        target:Character the Character getting raised from the dead
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return :
        None

        """

        # If target health is not zero or is valid attack is false then return (do nothing)
        if target.temp_health != 0 or not self.is_valid_attack(from_coord, to_coord, board):
            return
        # Otherwise set playe type to Villain
        target.player = Player.VILLAIN
        # And temp health to half of total health
        target.temp_health = int(target.health / 2)

class Hero(Character):
    """
    Parent Class for all Heroes

    """
    def __init__(self) -> None:
        """
        Initialize the object with Player type Player.VILLAIN

        Parameters:
        None

        Return :
        None

        """

        # Initialize the parent class with Player type Hero
        super().__init__(Player.HERO)

    def __str__(self) -> str:
        # Return parent class string method
        return super().__str__()

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[None | Character]]) -> bool:
        """
        Return True if the move is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False

        """

        # If passes all Character valid move cases
        if super().is_valid_move(from_coord, to_coord, board):
            # And is moving less than or equal to self.move in x and y
            if abs(to_coord.x - from_coord.x) <= self.move and abs(to_coord.y - from_coord.y) <= self.move:
                # Then return True
                return True
        # If we fail any condtitions return False
        return False

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[None | Character]]) -> bool:
        """
        Return True if the attack is valid, False otherwise

        Parameters:
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the target
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return:
        True or False

        """
        
        # If passes all Character valid attack cases
        if super().is_valid_attack(from_coord, to_coord, board):
            # And is attacking less than or equal to self.range in x and y
            if abs(to_coord.x - from_coord.x) <= self.range and abs(to_coord.y - from_coord.y) <= self.range:
                # Then return True
                return True
        # If we fail any condtitions return False
        return False

    def calculate_dice(self, target: Character, attack: bool = True, lst: list = None, *args, **kwargs) -> int:
        """
        Return  the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num:int number of sucessful rolls

        """

        # Return calculate dice of the parent class
        return super().calculate_dice(target, attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        """
        Subtract damage from target.temp_health and print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None

        """

        # Execute deal damage of the parent class
        super().deal_damage(target, damage)

class Warrior(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return :
        None

        """
        
        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]

    def calculate_dice(self, target: Character, attack: bool = True, lst: list = None, gob: list = None) -> int:
        """
        Return  the number of successful rolls using lst:list or generating a list of random rolls from 1 to 6, also uses gob to roll 2 extra dice when
        attacking a goblin, or if empty generates 2 more rolls

        Parameters:
        target:Character the Character self is in combat with
        attack:bool true when self is attacking, false when defending
        lst:list a list used for testing, custom dice rolls

        Return:
        sucess_num: int number of sucessful rolls

        """

        # Set sucess_num to zero
        sucess_num = 0

        # If attacking a goblin
        if attack and target.__class__ == Goblin:
            # And the list is none
            if gob is None:
                gob = []
                # Add dice to the list
                for _ in range(0, 2):
                    gob.append(randint(1, 6))
            # Set compare to 4
            compare = 4
            for roll in gob:
                # Check all rolls in the list
                if roll > compare:
                    # Add 1 per sucessful roll
                    sucess_num += 1
        # Add sucessful rolls to the calculate dice of the parent class
        return super().calculate_dice(target, attack, lst) + sucess_num

class Mage(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return :
        None

        """

        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.combat = [2, 2]
        self.range = 3
        self.move = 2

    def deal_damage(self, target: Character, damage: int):
        """
        Subtract damage from target.temp_health and print message if there is a Character Death, add 1 to damage for Mage class

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None

        """

        # Execute deal damage of parent class with damage added to by one
        super().deal_damage(target, damage + 1)

class Paladin(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return :
        None

        """
        
        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.__heal = True
        self.health = 6
        self.temp_health = 6

    @property
    def heal(self) -> bool:
        """
        Get or Set heal variable, check bool type

        Parameters:
        heal:bool if passed will be the new heal value

        Return:
        self.__heal if getting will return heal value

        """

        # Return heal variable
        return self.__heal

    @heal.setter
    def heal(self, heal) -> None:
        # If heal is not bool raise TypeError
        if type(heal) != bool:
            raise TypeError
        # Set .__heal to heal
        self.__heal = heal

    def revive(self, target: Character, from_coord: Coord, to_coord: Coord,
               board: List[List[None | Character]]) -> None:
        """
        Check prereqs, set temp.health to health/2 rounded down and heal to false

        Parameters:
        target:Character the Character getting raised from the dead
        from_coord:Coord the coordinates of the current position of the character
        to_coord:Coord the coordinates of the final position of the character
        board:List[List[None|Character]] the 2D list of the current board containing either None or Character in each slot

        Return :
        None

        """

        # If heal is false or player is not a Hero or target health is not zero or it is not a valid attack return (do nothing)
        if not self.__heal or target.player != Player.HERO or target.temp_health != 0 or not self.is_valid_attack(
                from_coord, to_coord, board):
            return
        # Set temp_health to half of total health
        target.temp_health = int(target.health / 2)
        # Set heal to false
        self.heal = False

class Ranger(Hero):
    def __init__(self) -> None:
        """
        Initialize the object as a Hero, set specific property values

        Parameters:
        None

        Return :
        None

        """
        
        # Initialize the parent class
        super().__init__()
        # Set specific variable changes
        self.range = 3

    def deal_damage(self, target: Character, damage: int) -> None:
        """
        Subtract damage from target.temp_health, do one less damage to skeletons. Print message if there is a Character Death

        Parameters:
        target:Character the Character taking damage
        damage:int the amount of damage taken

        Return:
        None

        """

        # If target is a skeleton
        if target.__class__ == Skeleton:
            # Execute deal damage of parent class with damage subtracted by one
            super().deal_damage(target, damage - 1)
            return
        # Execute deal damage of parent class
        super().deal_damage(target, damage)