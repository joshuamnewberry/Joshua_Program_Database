from game import *
import unittest

# Used to combine the testing for Hero and Villain parent functions, putting both classes through the same tests
class CharacterPropertyTestingHelper:
    """
    Tests Character properties and default values

    """
    def __init__(self) -> None:
        return None
    
    # Player Testing
    def testPlayerRead(self, char:Character, player:Player) -> bool:
        return char.player == player
    
    def testPlayerWrite(self, char:Character, player:Player) -> bool:
        if player == Player.HERO:
            char.player = Player.VILLAIN
            return char.player == Player.VILLAIN
        else:
            char.player = Player.HERO
            return char.player == Player.HERO
    
    def testPlayerWriteInt(self, char:Character) -> None:
        char.player = 10
    
    # Health Testing
    def testHealthRead(self, char:Character) -> bool:
        return char.health == 5
    
    def testHealthWrite(self, char:Character) -> bool:
        char.health = 10
        return char.health == 10
    
    def testHealthWriteNegative(self, char:Character) -> None:
        char.health = -10
    
    def testHealthWriteZero(self, char:Character) -> None:
        char.health = 0
    
    def testHealthWriteDouble(self, char:Character) -> None:
        char.health = 2.5
    
    def testHealthWriteStr(self, char:Character) -> None:
        char.health = "Hello"
    
    # Temp Health Testing
    def testTempHealthRead(self, char:Character) -> bool:
        return char.temp_health == 5
    
    def testTempHealthWrite(self, char:Character) -> bool:
        char.temp_health = 10
        return char.temp_health == 10
    
    def testTempHealthWriteNegative(self, char:Character) -> None:
        char.temp_health = -10
    
    def testTempHealthWriteZero(self, char:Character) -> bool:
        char.temp_health = 0
        return char.temp_health == 0
    
    def testTempHealthWriteDouble(self, char:Character) -> None:
        char.temp_health = 2.5
    
    def testTempHealthWriteStr(self, char:Character) -> None:
        char.temp_health = "Hello"
    
    # Character Death Test
    def testCharacterDeathTempHealthReset(self, char:Character) -> bool:
        try:
            char.temp_health = -5
        except:
            return char.temp_health == 0
        return
    
    # Combat Testing
    def testAttackRead(self, char:Character) -> bool:
        return char.combat[0] == 3
    
    def testDefenseRead(self, char:Character) -> bool:
        return char.combat[1] == 3
    
    def testCombatLength(self, char:Character) -> bool:
        return len(char.combat)
    
    def testAttackWrite(self, char:Character) -> bool:
        char.combat = [5, 3]
        return char.combat[0] == 5
    
    def testDefenseWrite(self, char:Character) -> bool:
        char.combat = [3, 5]
        return char.combat[1] == 5
    
    def testAttackWriteNegative(self, char:Character) -> None:
        char.combat = [-1, 10]
    
    def testDefenseWriteNegative(self, char:Character) -> None:
        char.combat = [10, -1]
    
    def testAttackWriteZero(self, char:Character) -> None:
        char.combat = [0, 10]
    
    def testDefenseWriteZero(self, char:Character) -> None:
        char.combat = [10, 0]
    
    def testCombatWriteNonList(self, char:Character) -> None:
        char.combat = 10
    
    def testAttackWriteDouble(self, char:Character) -> None:
        char.combat = [2.5, 10]
    
    def testDefenseWriteDouble(self, char:Character) -> None:
        char.combat = [10, 2.5]
    
    def testAttackWriteStr(self, char:Character) -> None:
        char.combat = ["Hello", 10]
    
    def testDefenseWriteStr(self, char:Character) -> None:
        char.combat = [10, "Hello"]
    
    def testCombatLengthThree(self, char:Character) -> None:
        char.combat = [10, 10, 10]
    
    # Move Testing
    def testMoveRead(self, char:Character) -> bool:
        return char.move == 3
    
    def testMoveWrite(self, char:Character) -> bool:
        char.move = 5
        return char.move == 5
    
    def testMoveWriteDouble(self, char:Character) -> None:
        char.move = 2.5
    
    def testMoveWriteStr(self, char:Character) -> None:
        char.move = "Hello"
    
    def testMoveWriteZero(self, char:Character) -> None:
        char.move = 0
    
    def testMoveWriteNegative(self, char:Character) -> None:
        char.move = -5
    
    # Range Testing
    def testRangeRead(self, char:Character) -> bool:
        return char.range == 1
    
    def testRangeWrite(self, char:Character) -> bool:
        char.range = 5
        return char.range == 5
    
    def testRangeWriteDouble(self, char:Character) -> None:
        char.range = 2.5
    
    def testRangeWriteStr(self, char:Character) -> None:
        char.range = "Hello"
    
    def testRangeWriteZero(self, char:Character) -> None:
        char.range = 0
    
    def testRangeWriteNegative(self, char:Character) -> None:
        char.range = -5

class HeroTesting(unittest.TestCase):
    """
    Tests Hero Method implementations, properties, and Child Class method changes

    """

    # Player
    def testHeroPlayerProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testPlayerRead(Hero(), Player.HERO))
        self.assertTrue(c.testPlayerWrite(Hero(), Player.HERO))
        with self.assertRaises(TypeError):
            c.testPlayerWriteInt(Hero())
    
    # Health
    def testHeroHealthProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testHealthRead(Hero()))
        self.assertTrue(c.testHealthWrite(Hero()))
        with self.assertRaises(ValueError):
            c.testHealthWriteNegative(Hero())
        with self.assertRaises(ValueError):
            c.testHealthWriteZero(Hero())
        with self.assertRaises(TypeError):
            c.testHealthWriteDouble(Hero())
        with self.assertRaises(TypeError):
            c.testHealthWriteStr(Hero())
    
    # Temp Health
    def testTempHealthProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testTempHealthRead(Hero()))
        self.assertTrue(c.testTempHealthWrite(Hero()))
        with self.assertRaises(CharacterDeath):
            c.testTempHealthWriteNegative(Hero())
        self.assertTrue(c.testTempHealthWriteZero(Hero()))
        with self.assertRaises(TypeError):
            c.testTempHealthWriteDouble(Hero())
        with self.assertRaises(TypeError):
            c.testTempHealthWriteStr(Hero())
        self.assertTrue(c.testCharacterDeathTempHealthReset(Hero()))
    
    # Combat
    def testCombatProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testAttackRead(Hero()))
        self.assertTrue(c.testDefenseRead(Hero()))
        self.assertTrue(c.testCombatLength(Hero()))
        self.assertTrue(c.testAttackWrite(Hero()))
        self.assertTrue(c.testDefenseWrite(Hero()))
        with self.assertRaises(ValueError):
            c.testAttackWriteNegative(Hero())
        with self.assertRaises(ValueError):
            c.testDefenseWriteNegative(Hero())
        c.testAttackWriteZero(Hero())
        c.testDefenseWriteZero(Hero())
        with self.assertRaises(TypeError):
            c.testCombatWriteNonList(Hero())
        with self.assertRaises(TypeError):
            c.testAttackWriteDouble(Hero())
        with self.assertRaises(TypeError):
            c.testDefenseWriteDouble(Hero())
        with self.assertRaises(TypeError):
            c.testAttackWriteStr(Hero())
        with self.assertRaises(TypeError):
            c.testDefenseWriteStr(Hero())
        with self.assertRaises(ValueError):
            c.testCombatLengthThree(Hero())
    
    # Move
    def testMoveProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testMoveRead(Hero()))
        self.assertTrue(c.testMoveWrite(Hero()))
        with self.assertRaises(TypeError):
            c.testMoveWriteDouble(Hero())
        with self.assertRaises(TypeError):
            c.testMoveWriteStr(Hero())
        with self.assertRaises(ValueError):
            c.testMoveWriteZero(Hero())
        with self.assertRaises(ValueError):
            c.testMoveWriteNegative(Hero())
    
    # Range
    def testRangeProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testRangeRead(Hero()))
        self.assertTrue(c.testRangeWrite(Hero()))
        with self.assertRaises(TypeError):
            c.testRangeWriteDouble(Hero())
        with self.assertRaises(TypeError):
            c.testRangeWriteStr(Hero())
        with self.assertRaises(ValueError):
            c.testRangeWriteZero(Hero())
        with self.assertRaises(ValueError):
            c.testRangeWriteNegative(Hero())
    
    # Default Values
    def testDefaultValues(self) -> None:
        # Hero
        a = Hero()
        self.assertTrue([Player.HERO, 5, 5, 3, 3, [3, 3], 3, 1], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
        # Warrior
        a = Warrior()
        self.assertTrue([Player.HERO, 7, 7, 2, 4, [2, 4], 3, 1], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
        # Mage
        a = Mage()
        self.assertTrue([Player.HERO, 5, 5, 2, 2, [2, 2], 2, 3], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
        # Paladin
        a = Paladin()
        self.assertTrue([Player.HERO, 6, 6, 3, 3, [3, 3], 3, 1, True], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range, a.heal])
        # Ranger
        a = Ranger()
        self.assertTrue([Player.HERO, 5, 5, 3, 3, [3, 3], 3, 3], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
    
    # String function
    def testHeroStr(self) -> None:
        self.assertEqual(str(Hero()), "Hero")
        self.assertEqual(str(Warrior()), "Warrior")
        self.assertEqual(str(Mage()), "Mage")
        self.assertEqual(str(Paladin()), "Paladin")
        self.assertEqual(str(Ranger()), "Ranger")
    
    # Is Valid Move
    def testIsValidMove_Good(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertTrue(a.is_valid_move(Coord(0, 0), Coord(3, 3), board))
        board[0][0] = None
        board[3][3] = a
        self.assertTrue(a.is_valid_move(Coord(3, 3), Coord(0, 0), board))
    
    def testIsValidMove_Occupied(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, Warrior(), None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(2, 2), board))
    
    def testIsValidMove_NegativeCoords(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(-1, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_move(Coord(-0, -1), Coord(3, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(-1, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(3, -1), board))
    
    def testIsValidMove_OutOfBoundCoords(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(5, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 5), Coord(3, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(5, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(3, 5), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(-2, -2), board))
    
    def testIsValidMove_SameCoords(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(0, 0), board))
        board[0][0] = None
        board[4][4] = a
        self.assertFalse(a.is_valid_move(Coord(4, 4), Coord(4, 4), board))
    
    def testIsValidMove_NonStartingPosition(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(4, 4), Coord(2, 2), board))
    
    # Is Valid Attack
    def testIsValidAttack_Good(self) -> None:
        a = Paladin()
        b = Mage()
        c = Ranger()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, Goblin(), None, None, b],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, c]  ]
        self.assertTrue(a.is_valid_attack(Coord(0, 0), Coord(1, 1), board))
        self.assertTrue(b.is_valid_attack(Coord(1, 4), Coord(1, 1), board))
        self.assertTrue(c.is_valid_attack(Coord(4, 4), Coord(1, 1), board))
        board[0][0] = None
        board[2][2] = a
        self.assertTrue(a.is_valid_attack(Coord(2, 2), Coord(1, 1), board))
    
    def testIsValidAttack_NotOccupied(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(2, 2), board))
    
    def testIsValidAttack_NegativeCoords(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(-1, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(-0, -1), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(-1, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(3, -1), board))
    
    def testIsValidAttack_OutOfBoundCoords(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(5, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 5), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(5, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(3, 5), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(-2, -2), board))
    
    def testIsValidAttack_SameCoords(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(0, 0), board))
        board[0][0] = None
        board[4][4] = a
        self.assertFalse(a.is_valid_attack(Coord(4, 4), Coord(4, 4), board))
    
    def testIsValidAttack_NonStartingPosition(self) -> None:
        a = Paladin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, Paladin(), None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(2, 2), Coord(0, 0), board))

    def testCalculateDice(self) -> None:
        # Set Random Seed
        random.seed(50)

        # Hero
        self.assertEqual(Hero().calculate_dice(Villain(), True), 0)
        self.assertEqual(Hero().calculate_dice(Villain(), True, [4, 5, 4]), 1)
        self.assertEqual(Hero().calculate_dice(Villain(), False), 2)
        self.assertEqual(Hero().calculate_dice(Villain(), False, [4, 5, 4]), 3)

        # Warrior vs. Non Goblin
        self.assertEqual(Warrior().calculate_dice(Villain(), True), 0)
        self.assertEqual(Warrior().calculate_dice(Villain(), True, [4, 5]), 1)
        self.assertEqual(Warrior().calculate_dice(Villain(), False), 1)
        self.assertEqual(Warrior().calculate_dice(Villain(), False, [4, 5, 4, 5], [4, 5]), 4)

        # Warrior vs. Goblin
        self.assertEqual(Warrior().calculate_dice(Goblin(), True), 2)
        self.assertEqual(Warrior().calculate_dice(Goblin(), True, [4, 5], [4, 5]), 2)
        self.assertEqual(Warrior().calculate_dice(Goblin(), False), 0)
        self.assertEqual(Warrior().calculate_dice(Goblin(), False, [4, 5, 4, 5], [4, 5]), 4)

    # Deal Damage
    def testDealDamage_CheckFinalTempHealth(self) -> None:
        a = Paladin()
        b = Warrior()
        b.deal_damage(a, 3)
        self.assertEqual(a.temp_health, 3)
    
    def testDealDamage_DeadCheckTempZero(self) -> None:
        a = Paladin()
        b = Warrior()
        b.deal_damage(a, 10)
        self.assertEqual(a.temp_health, 0)
    
    def testMageDealDamage(self) -> None:
        a = Mage()
        b = Necromancer()
        a.deal_damage(b, 1)
        self.assertEqual(b.temp_health, 3)

    def testRangerDealDamage(self) -> None:
        a = Ranger()
        b = Skeleton()
        c = Necromancer()
        a.deal_damage(b, 2)
        a.deal_damage(c, 2)
        self.assertEqual(b.temp_health, 1)
        self.assertEqual(c.temp_health, 3)
    
    # Heal Property
    def testHealProperty(self) -> None:
        a = Paladin()
        self.assertEqual(a.heal, True)
    
    # Heal Method
    def testRevive(self) -> None:
        a = Paladin()
        b = Mage()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, b, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        a.revive(b, Coord(0, 0), Coord(1, 1), board)
        self.assertEqual(b.temp_health, int(b.health / 2))

        a = Paladin()
        b = Mage()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, b]  ]
        a.revive(b, Coord(0, 0), Coord(4, 4), board)
        self.assertEqual(b.temp_health, 0)

        a = Paladin()
        b = Goblin()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, b, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        a.revive(b, Coord(0, 0), Coord(1, 1), board)
        self.assertEqual(b.temp_health, 0)

class VillainTesting(unittest.TestCase):
    """
    Tests Villain Method implementations, properties, and Child Class method changes

    """

    # Player
    def testHeroPlayerProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testPlayerRead(Villain(), Player.VILLAIN))
        self.assertTrue(c.testPlayerWrite(Villain(), Player.VILLAIN))
        with self.assertRaises(TypeError):
            c.testPlayerWriteInt(Villain())
    
    # Health
    def testHeroHealthProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testHealthRead(Villain()))
        self.assertTrue(c.testHealthWrite(Villain()))
        with self.assertRaises(ValueError):
            c.testHealthWriteNegative(Villain())
        with self.assertRaises(ValueError):
            c.testHealthWriteZero(Villain())
        with self.assertRaises(TypeError):
            c.testHealthWriteDouble(Villain())
        with self.assertRaises(TypeError):
            c.testHealthWriteStr(Villain())
    
    # Temp Health
    def testTempHealthProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testTempHealthRead(Villain()))
        self.assertTrue(c.testTempHealthWrite(Villain()))
        with self.assertRaises(CharacterDeath):
            c.testTempHealthWriteNegative(Villain())
        self.assertTrue(c.testTempHealthWriteZero(Villain()))
        with self.assertRaises(TypeError):
            c.testTempHealthWriteDouble(Villain())
        with self.assertRaises(TypeError):
            c.testTempHealthWriteStr(Villain())
        self.assertTrue(c.testCharacterDeathTempHealthReset(Villain()))
    
    # Combat
    def testCombatProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testAttackRead(Villain()))
        self.assertTrue(c.testDefenseRead(Villain()))
        self.assertTrue(c.testCombatLength(Villain()))
        self.assertTrue(c.testAttackWrite(Villain()))
        self.assertTrue(c.testDefenseWrite(Villain()))
        with self.assertRaises(ValueError):
            c.testAttackWriteNegative(Villain())
        with self.assertRaises(ValueError):
            c.testDefenseWriteNegative(Villain())
        c.testAttackWriteZero(Villain())
        c.testDefenseWriteZero(Villain())
        with self.assertRaises(TypeError):
            c.testCombatWriteNonList(Villain())
        with self.assertRaises(TypeError):
            c.testAttackWriteDouble(Villain())
        with self.assertRaises(TypeError):
            c.testDefenseWriteDouble(Villain())
        with self.assertRaises(TypeError):
            c.testAttackWriteStr(Villain())
        with self.assertRaises(TypeError):
            c.testDefenseWriteStr(Villain())
        with self.assertRaises(ValueError):
            c.testCombatLengthThree(Villain())
    
    # Move
    def testMoveProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testMoveRead(Villain()))
        self.assertTrue(c.testMoveWrite(Villain()))
        with self.assertRaises(TypeError):
            c.testMoveWriteDouble(Villain())
        with self.assertRaises(TypeError):
            c.testMoveWriteStr(Villain())
        with self.assertRaises(ValueError):
            c.testMoveWriteZero(Villain())
        with self.assertRaises(ValueError):
            c.testMoveWriteNegative(Villain())
    
    # Range
    def testRangeProperty(self) -> None:
        c = CharacterPropertyTestingHelper()
        self.assertTrue(c.testRangeRead(Villain()))
        self.assertTrue(c.testRangeWrite(Villain()))
        with self.assertRaises(TypeError):
            c.testRangeWriteDouble(Villain())
        with self.assertRaises(TypeError):
            c.testRangeWriteStr(Villain())
        with self.assertRaises(ValueError):
            c.testRangeWriteZero(Villain())
        with self.assertRaises(ValueError):
            c.testRangeWriteNegative(Villain())
    
    # Default Values
    def testDefaultValues(self) -> None:
        # Villain
        a = Villain()
        self.assertTrue([Player.VILLAIN, 5, 5, 3, 3, [3, 3], 3, 1], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
        # Skeleton
        a = Skeleton()
        self.assertTrue([Player.VILLAIN, 2, 2, 2, 1, [2, 1], 2, 1], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
        # Goblin
        a = Goblin()
        self.assertTrue([Player.VILLAIN, 3, 3, 2, 2, [2, 2], 3, 1], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
        # Necromancer
        a = Necromancer()
        self.assertTrue([Player.VILLAIN, 5, 5, 1, 2, [1, 2], 3, 3], [a.player, a.health, a.temp_health, a._Character__attack, a._Character__defense, a.combat, a.move, a.range])
    
    # String function
    def testVillainStr(self) -> None:
        self.assertEqual(str(Villain()), "Villain")
        self.assertEqual(str(Goblin()), "Goblin")
        self.assertEqual(str(Skeleton()), "Skeleton")
        self.assertEqual(str(Necromancer()), "Necromancer")
    
    # Is Valid Move
    def testIsValidMove_Good(self) -> None:
        a = Skeleton()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertTrue(a.is_valid_move(Coord(0, 0), Coord(0, 2), board))
        board[0][0] = None
        board[2][2] = a
        self.assertTrue(a.is_valid_move(Coord(2, 2), Coord(0, 2), board))
    
    def testIsValidMove_Occupied(self) -> None:
        a = Skeleton()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [Warrior(), None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(2, 0), board))
    
    def testIsValidMove_NegativeCoords(self) -> None:
        a = Skeleton()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(-1, 0), Coord(2, 2), board))
        self.assertFalse(a.is_valid_move(Coord(-0, -1), Coord(2, 2), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(-1, 2), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(2, -1), board))
    
    def testIsValidMove_OutOfBoundCoords(self) -> None:
        a = Goblin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(5, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 5), Coord(3, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(5, 3), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(3, 5), board))
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(-2, -2), board))
    
    def testIsValidMove_SameCoords(self) -> None:
        a = Goblin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(0, 0), board))
        board[0][0] = None
        board[4][4] = a
        self.assertFalse(a.is_valid_move(Coord(4, 4), Coord(4, 4), board))
    
    def testIsValidMove_NonStartingPosition(self) -> None:
        a = Necromancer()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(4, 4), Coord(4, 2), board))
    
    def testIsValidMove_NonStraightLineVillain(self) -> None:
        a = Necromancer()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_move(Coord(0, 0), Coord(2, 2), board))
    
    # Is Valid Attack
    def testIsValidAttack_Good(self) -> None:
        a = Skeleton()
        b = Goblin()
        c = Necromancer()
        # Board used for testing purposes
        board = [   [None, None, None, None, None],
                    [a, Mage(), b, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, c, None, None, None]  ]
        self.assertTrue(a.is_valid_attack(Coord(1, 0), Coord(1, 1), board))
        self.assertTrue(b.is_valid_attack(Coord(1, 2), Coord(1, 1), board))
        self.assertTrue(c.is_valid_attack(Coord(4, 1), Coord(1, 1), board))
        board[0][0] = None
        board[2][2] = a
        self.assertTrue(a.is_valid_attack(Coord(2, 2), Coord(1, 1), board))
    
    def testIsValidAttack_NotOccupied(self) -> None:
        a = Necromancer()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(2, 2), board))
    
    def testIsValidAttack_NegativeCoords(self) -> None:
        a = Necromancer()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(-1, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(-0, -1), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(-1, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(3, -1), board))
    
    def testIsValidAttack_OutOfBoundCoords(self) -> None:
        a = Necromancer()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(5, 0), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 5), Coord(3, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(5, 3), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(3, 5), board))
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(-2, -2), board))
    
    def testIsValidAttack_SameCoords(self) -> None:
        a = Skeleton()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(0, 0), Coord(0, 0), board))
        board[0][0] = None
        board[4][4] = a
        self.assertFalse(a.is_valid_attack(Coord(4, 4), Coord(4, 4), board))
    
    def testIsValidAttack_NonStartingPosition(self) -> None:
        a = Goblin()
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, Paladin(), None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        self.assertFalse(a.is_valid_attack(Coord(2, 2), Coord(0, 0), board))

    def testCalculateDice(self) -> None:
        # Set random seed
        random.seed(50)

        self.assertEqual(Villain().calculate_dice(Hero(), True), 0)
        self.assertEqual(Villain().calculate_dice(Hero(), True, [4, 5, 4]), 1)
        self.assertEqual(Villain().calculate_dice(Hero(), False), 2)
        self.assertEqual(Villain().calculate_dice(Hero(), False, [4, 5, 4]), 3)

    # Deal Damage
    def testDealDamage_CheckFinalTempHealth(self) -> None:
        a = Skeleton()
        b = Paladin()
        b.deal_damage(a, 1)
        self.assertEqual(a.temp_health, 1)
    
    def testDealDamage_DeadCheckTempZero(self) -> None:
        a = Goblin()
        b = Skeleton()
        b.deal_damage(a, 10)
        self.assertEqual(a.temp_health, 0)
    
    # Raise Dead Method
    def testRaiseDead(self) -> None:
        a = Necromancer()
        b = Mage()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [b, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        a.raise_dead(b, Coord(0, 0), Coord(2, 0), board)
        self.assertEqual(b.temp_health, int(b.health / 2))

        a = Necromancer()
        b = Goblin()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [b, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        a.raise_dead(b, Coord(0, 0), Coord(2, 0), board)
        self.assertEqual(b.temp_health, int(b.health / 2))

        a = Necromancer()
        b = Goblin()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [b, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None]  ]
        a.raise_dead(b, Coord(0, 0), Coord(2, 0), board)
        self.assertEqual(b.player, Player.VILLAIN)

        a = Necromancer()
        b = Ranger()
        b.temp_health = 0
        # Board used for testing purposes
        board = [   [a, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, b]  ]
        a.raise_dead(b, Coord(0, 0), Coord(1, 1), board)
        self.assertEqual(b.temp_health, 0)

class DungeonTesting(unittest.TestCase):
    """
    Tests Dungeon class properties and methods, as well as how it interacts with the character and creature

    """

    def setUp(self):
        self.dungeon = Dungeon(6, 6)
        self.from_coord = Coord(0, 0)
        self.to_coord = Coord(1, 1)
    
    def test_board_length_valid(self):
        self.assertEqual(self.dungeon.height, 6)
        self.assertEqual(self.dungeon.width, 6)
    
    def test_board_length_invalid(self):
        with self.assertRaises(ValueError):
            Dungeon.boardLength(3)
        with self.assertRaises(ValueError):
            Dungeon.boardLength(13)
        with self.assertRaises(TypeError):
            Dungeon.boardLength("10")
        with self.assertRaises(TypeError):
            Dungeon.boardLength(5.1)
    
    def test_initial_villains_generation(self):
        dungeon_with_villains = Dungeon(6, 6)
        dungeon_with_villains.generate_new_board()
        self.assertTrue(len(dungeon_with_villains.villains) > 0)
        self.assertTrue(all(isinstance(v, Villain) for v in dungeon_with_villains.villains))
    
    def test_custom_villains(self):
        villains = [Goblin(), Skeleton()]
        dungeon = Dungeon(6, 6, villains=villains)
        self.assertEqual(len(dungeon.villains), len(villains))
        self.assertEqual(dungeon.villains, villains)
    
    def test_hero_initialization(self):
        self.assertEqual(len(self.dungeon.heroes), 4)
        self.assertTrue(all(isinstance(hero, Hero) for hero in self.dungeon.heroes))
    
    def test_set_character_at(self):
        hero = Warrior()
        self.dungeon.set_character_at(hero, 3, 3)
        self.assertEqual(self.dungeon.character_at(3, 3), hero)
    
    def test_set_character_at_out_of_bounds(self):
        hero = Warrior()
        with self.assertRaises(ValueError):
            self.dungeon.set_character_at(hero, -3, 0)
        with self.assertRaises(ValueError):
            self.dungeon.set_character_at(hero, 0, 12)
    
    def test_move_character(self):
        hero = Warrior()
        self.dungeon.set_character_at(hero, self.from_coord.x, self.from_coord.y)
        self.dungeon.move(self.from_coord, self.to_coord)
        self.assertIsNone(self.dungeon.character_at(self.from_coord.x, self.from_coord.y))
        self.assertEqual(self.dungeon.character_at(self.to_coord.x, self.to_coord.y), hero)
    
    def test_valid_attack(self):
        attacker = Warrior()
        defender = Goblin()
        self.dungeon.set_character_at(attacker, self.from_coord.x, self.from_coord.y)
        self.dungeon.set_character_at(defender, self.to_coord.x, self.to_coord.y)
        self.assertTrue(self.dungeon.is_valid_attack([self.from_coord, self.to_coord]))
    
    def test_invalid_attack(self):
        self.assertIsNone(self.dungeon.character_at(0, 0))
        with self.assertRaises(ValueError) as context:
            self.dungeon.is_valid_attack([Coord(0, 0), Coord(4, 4)])
        self.assertIn("No character at", str(context.exception))
    
    def test_dungeon_clear_false(self):
        self.dungeon.set_character_at(Goblin(), 0, 1)
        self.assertFalse(self.dungeon.is_dungeon_clear())
    
    def test_adventurer_defeat(self):
        self.dungeon.set_character_at(Warrior(), 0, 0)
        self.assertFalse(self.dungeon.adventurer_defeat())
    
    def test_switch_player(self):
        self.assertEqual(self.dungeon.player, Player.HERO)
        self.dungeon.set_next_player()
        self.assertEqual(self.dungeon.player, Player.VILLAIN)
    
    def test_generate_villains(self):
        self.dungeon.generate_villains()
        self.assertTrue(1 <= len(self.dungeon.villains) <= max(self.dungeon.height, self.dungeon.width))
    
    def test_generate_villains_random(self):
        random.seed(42)
        self.dungeon.generate_villains()
        expected_villains_types = [Goblin, Goblin, Goblin, Goblin, Goblin, Goblin]
        generated_villains_types = [type(villain) for villain in self.dungeon.villains]
        self.assertEqual(
            generated_villains_types,
            expected_villains_types,
            "The generated villains do not match the expected types."
        )

if __name__ == "__main__":
    unittest.main()