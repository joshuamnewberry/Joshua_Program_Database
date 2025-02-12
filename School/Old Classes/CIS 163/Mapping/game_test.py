import unittest
from game import *

class TestLLStack(unittest.TestCase):

    def test_head(self) -> None:
        a = (1, 2)
        b = LLStack()
        self.assertEqual(b._LLStack__head, None)
        b.push(a)
        self.assertEqual(b._LLStack__head.data, a)
        self.assertEqual(type(b._LLStack__head), Node)
    
    def test_push(self) -> None:
        a = LLStack()
        with self.assertRaises(TypeError):
            a.push(5)
        with self.assertRaises(TypeError):
            a.push("hi")
        with self.assertRaises(TypeError):
            a.push([1, 2])
        with self.assertRaises(ValueError):
            a.push((1, 2, 3))
        with self.assertRaises(ValueError):
            a.push((-1, 1))
        with self.assertRaises(ValueError):
            a.push((1, -1))
        a.push((0, 0))
        a.push((100, 100))
    
    def test_pop(self) -> None:
        a = LLStack()
        a.push((0,0))
        self.assertEqual(a.pop(), (0,0))
        a.push((1,1))
        a.push((2,2))
        self.assertEqual(a.pop(), (2,2))
        a.push((2,2))
        self.assertEqual(a.pop(), (2,2))
    
    def test_storing(self) -> None:
        a = LLStack()
        a.push((1,1))
        a.push((2,2))
        a.push((3,3))
        self.assertEqual(a._LLStack__head.next.next.next, None)
        self.assertEqual(a._LLStack__head.next.next.data, (1,1))
        self.assertEqual(a._LLStack__head.next.data, (2,2))
        self.assertEqual(a._LLStack__head.data, (3,3))
    
    def test_size(self) -> None:
        a = LLStack()
        self.assertEqual(a.size, 0)
        a.push((1,2))
        self.assertEqual(a.size, 1)
        a.push((0,0))
        self.assertEqual(a.size, 2)
        a.pop()
        self.assertEqual(a.size, 1)
        a.pop()
        self.assertEqual(a.size, 0)
    
    def test_str(self) -> None:
        a = LLStack()
        a.push((1,1))
        a.push((3,3))
        a.push((5,5))
        a.push((10,10))
        self.assertEqual("(1,1) -> (3,3) -> (5,5) -> (10,10)", str(a))
        a.pop()
        self.assertEqual("(1,1) -> (3,3) -> (5,5)", str(a))

class TestGame(unittest.TestCase):

    def test_InvalidCoordinateError_exception(self) -> None:
        with self.assertRaises(InvalidCoordinateError):
            raise InvalidCoordinateError
        with self.assertRaises(InvalidCoordinateError):
            raise InvalidCoordinateError("Hello")
    
    def test_OutOfBoundaries_exception(self) -> None:
        with self.assertRaises(OutOfBoundaries):
            raise OutOfBoundaries
        with self.assertRaises(OutOfBoundaries):
            raise OutOfBoundaries("Hello")
    
    def test_grid(self) -> None:
        with self.assertRaises(TypeError):
            Map(1, (1,1), (2,2))
        with self.assertRaises(TypeError):
            Map([1], (1,1), (2,2))
        with self.assertRaises(TypeError):
            Map([["ocean", 15], [(25, 25)]], (1,1), (2,2))
        with self.assertRaises(ValueError):
            Map([["Hello"], ["You suck", "Lol"]], (1,1), (2,2))
        with self.assertRaises(ValueError):
            Map([["ocean"], ["grass", "Lol"]], (1,1), (2,2))
        a = Map([["ocean"], ["grass", "grass"]], (1,0), (1,1))

    def test_start_coords(self) -> None:
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], 0, (1,1))
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], 10, (1,1))
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], (1.5, 10), (1,1))
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], (10, 1.5), (1,1))
        with self.assertRaises(ValueError):
            Map([["grass", "grass"], ["grass", "grass"]], (10, 10, 10), (1,1))
        with self.assertRaises(ValueError):
            Map([["grass", "grass"], ["grass", "grass"]], (-2, 5), (1,1))
        with self.assertRaises(ValueError):
            Map([["grass", "grass"], ["grass", "grass"]], (5, -2), (1,1))
        a = Map([["grass", "grass"], ["grass", "grass"]], (0, 0), (1,1))
        with self.assertRaises(TypeError):
            a.start_coords = 0
        with self.assertRaises(TypeError):
            a.start_coords = 10
        with self.assertRaises(TypeError):
            a.start_coords = (1.5, 10)
        with self.assertRaises(TypeError):
            a.start_coords = (10, 1.5)
        with self.assertRaises(ValueError):
            a.start_coords = (10, 10, 10)
        with self.assertRaises(ValueError):
            a.start_coords = (-2, 5)
        with self.assertRaises(ValueError):
            a.start_coords = (5, -2)
        a.start_coords = (0, 0)
    
    def test_end_coords(self) -> None:
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), 0)
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), 10)
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), (1.5, 10))
        with self.assertRaises(TypeError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), (10, 1.5))
        with self.assertRaises(ValueError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), (10, 10, 10))
        with self.assertRaises(ValueError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), (-2, 5))
        with self.assertRaises(ValueError):
            Map([["grass", "grass"], ["grass", "grass"]], (0,0), (5, -2))
        a = Map([["grass", "grass"], ["grass", "grass"]], (0,0), (1,1))
        with self.assertRaises(TypeError):
            a.end_coords = 0
        with self.assertRaises(TypeError):
            a.end_coords = 10
        with self.assertRaises(TypeError):
            a.end_coords = (1.5, 10)
        with self.assertRaises(TypeError):
            a.end_coords = (10, 1.5)
        with self.assertRaises(ValueError):
            a.end_coords = (10, 10, 10)
        with self.assertRaises(ValueError):
            a.end_coords = (-2, 5)
        with self.assertRaises(ValueError):
            a.end_coords = (5, -2)
        a.end_coords = (1, 1)

    def test_findPath(self) -> None:
        grid = [['ocean', 'grass', 'grass', 'grass'],
        ['grass', 'grass', 'grass', 'grass', 'grass'],
        ['grass', 'grass', 'grass', 'ocean', 'grass'],
        ['grass', 'ocean', 'grass', 'ocean', 'grass', 'grass'],
        ['ocean', 'grass', 'grass', 'grass', 'grass'],
        ['grass', 'grass', 'ocean', 'grass']]
        a = Map(grid, (1,1), (3,5))
        b = a.find_path()
        solutions = ["(1,1) -> (1,2) -> (1,3) -> (1,4) -> (2,4) -> (3,4) -> (3,5)",
                    "(1,1) -> (2,1) -> (2,2) -> (3,2) -> (4,2) -> (4,3) -> (4,4) -> (3,4) -> (3,5)",
                    "(1,1) -> (0,1) -> (0,2) -> (0,3) -> (1,3) -> (1,4) -> (2,4) -> (3,4) -> (3,5)",
                    "(1,1) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (1,2) -> (0,2) -> (0,3) -> (1,3) -> (1,4) -> (2,4) -> (3,4) -> (3,5)",
                    "(1,1) -> (0,1) -> (0,2) -> (0,3) -> (1,3) -> (1,2) -> (2,2) -> (3,2) -> (4,2) -> (4,3) -> (4,4) -> (3,4) -> (3,5)"]
        self.assertTrue(str(b) in solutions)

    def test_findShortestPath(self) -> None:
        grid = [['ocean', 'grass', 'grass', 'grass'],
        ['grass', 'grass', 'grass', 'grass', 'grass'],
        ['grass', 'grass', 'grass', 'ocean', 'grass'],
        ['grass', 'ocean', 'grass', 'ocean', 'grass', 'grass'],
        ['ocean', 'grass', 'grass', 'grass', 'grass'],
        ['grass', 'grass', 'ocean', 'grass']]
        a = Map(grid, (1,1), (3,5))
        b = a.find_path()
        self.assertEqual("(1,1) -> (1,2) -> (1,3) -> (1,4) -> (2,4) -> (3,4) -> (3,5)", str(b))

        grid = [['grass', 'grass', 'grass', 'ocean', 'grass', 'grass', 'grass', 'ocean', 'grass', 'grass', 'ocean'],
                ['grass', 'ocean', 'grass', 'grass', 'grass', 'ocean', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'ocean', 'grass', 'grass', 'grass'],
                ['grass', 'ocean', 'grass', 'grass', 'grass'],
                ['ocean', 'grass', 'grass', 'grass', 'ocean', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
                ['grass', 'grass', 'grass', 'ocean', 'ocean', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'ocean', 'ocean', 'ocean'],
                ['grass', 'grass', 'grass', 'grass', 'grass'],
                ['grass', 'ocean', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
                ['grass', 'grass', 'grass', 'grass', 'grass', 'ocean', 'grass', 'grass', 'ocean', 'grass', 'grass', 'grass', 'ocean'],
                ['grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass', 'grass'],
                ['grass', 'grass', 'grass', 'grass']]
        a = Map(grid, (8,14), (5,1))
        b = a.find_path()
        self.assertEqual("(8,14) -> (8,13) -> (8,12) -> (8,11) -> (8,10) -> (8,9) -> (8,8) -> (8,7) -> (8,6) -> (8,5) -> (8,4) -> (8,3) -> (7,3) -> (7,2) -> (6,2) -> (5,2) -> (5,1)", str(b))

if __name__ == "__main__":
    unittest.main()