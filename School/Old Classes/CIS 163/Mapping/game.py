from llstack import *
from math import copysign

class InvalidCoordinateError(Exception):
    def __init__(self, msg:str = "") -> None:
        self.msg = str(msg)
    
    def __str__(self) -> str:
        return self.msg

class OutOfBoundaries (Exception):
    def __init__(self, msg:str = "") -> None:
        self.msg = str(msg)
    
    def __str__(self) -> str:
        return self.msg

class Map:
    
    def __init__(self, grid:List[List[str]], start_loc:tuple[int], end_loc:tuple[int]) -> None:
        """
        Initializes variables using properties and grid directly - check grid

        Parameters:
        grid:List[List[str]] the Map for which we will solve the path
        start_loc:tuple[int] the starting location
        end_loc:tuple[int]   the ending location

        Return:
        None
        
        """

        # If grid is not list
        if type(grid) != list:
            raise TypeError("Expected type List[List[str]]")
        # For all y in the grid
        for y in range(0, len(grid)):
            # If not a list
            if type(grid[y]) != list:
                raise TypeError("Expected type List[List[str]]")
            # For all x of this row of the grid
            for x in range(0, len(grid[y])):
                # If value is not a string
                if type(grid[y][x]) != str:
                    raise TypeError("Expected type List[List[str]]")
                # If value is not "grass" or "ocean"
                if grid[y][x] != "grass" and grid[y][x] != "ocean":
                    raise ValueError("Expected values \"grass\" or \"ocean\"")
        # Set values
        self.__grid = grid
        self.start_coords = start_loc
        self.end_coords = end_loc
    
    def coord_check(self, data:tuple[int]) -> None:
        """
        Check coord conditions and raise proper Errors

        Parameters:
        data:tuple[int] the coord to get checked

        Return:
        None
        
        """
        
        # Check grid bounds
        if data[0] >= len(self.grid) or data[1] >= len(self.grid[data[0]]):
            raise OutOfBoundaries(f"({data[0]},{data[1]}) not in bounds")
        # Check not starting in ocean
        if self.grid[data[0]][data[1]] == "ocean":
            raise InvalidCoordinateError("Cannot start in the Ocean")
    
    @property
    def start_coords(self) -> tuple[int]:
        """
        Get or Set self.__start, check tuple_conditions as well as specific coord conditions

        Parameters:
        data:tuple[int] the starting location

        Return:
        self.__start the starting location
        
        """

        return self.__start
    @start_coords.setter
    def start_coords(self, data:tuple[int]) -> None:
        # Check tuple conditions
        tuple_conditions(data)
        # Check coord conditions
        self.coord_check(data)
        self.__start = data
    
    @property
    def end_coords(self) -> tuple[int]:
        """
        Get or Set self.__end, check tuple_conditions as well as specific coord conditions

        Parameters:
        data:tuple[int] the ending location

        Return:
        self.__end the ending location
        
        """

        return self.__end
    @end_coords.setter
    def end_coords(self, data:tuple[int]) -> None:
        # Check tuple conditions
        tuple_conditions(data)
        # Check not ending at starting coords
        if data == self.start_coords:
            raise ValueError("Cannot end at starting location")
        # Check coord conditions
        self.coord_check(data)
        self.__end = data
    
    @property
    def grid(self) -> List[List[str]]:
        return self.__grid
    
    def solve(self, start:tuple[int], end:tuple[int], grid:List[List[str|None]], path:LLStack, explored:set) -> LLStack|None:
        """
        Solve for the path, return the first viable path found

        Parameters:
        start:tuple[int]  Starting location - or current location on the path
        end:tuple[int]  Ending location
        grid:List[List[str|None]]  Grid to be traversed, the grid we are finding a path for
        path:LLStack  The current Path
        explored:set  The explored Path at the current time

        Return:
        LLStack or None, the path that is found, or None if no path is found
        
        """

        # If at the ending coord
        if start == end:
            # Add current location
            path.push(start)
            # Return the current path
            return path
        # If not in grid bounds
        if start[0] < 0 or start[0] >= len(grid) or start[1] < 0 or start[1] >= len(grid[start[0]]):
            return
        # If in an ocean
        if grid[start[0]][start[1]] == "ocean":
            return
        # If start has already been explored
        if start in explored:
            return
        # Add current location to path and explored
        path.push(start)
        explored.add(start)
        # Create deltaX and deltaY variables
        deltaX = end[0] - start[0]
        deltaY = end[1] - start[1]
        # If further away in X than Y go towards it X first
        if abs(deltaX) > abs(deltaY):
            # Go towards by X
            a = self.solve((int(start[0] + copysign(1, deltaX)), start[1]), end, grid, path, explored)
            if a:
                return a
            # Go towards by Y
            a = self.solve((start[0], int(start[1] + copysign(1, deltaY))), end, grid, path, explored)
            if a:
                return a
            # Go away by Y
            a = self.solve((start[0], int(start[1] - copysign(1, deltaY))), end, grid, path, explored)
            if a:
                return a
            # Go away by X
            a = self.solve((int(start[0] - copysign(1, deltaX)), start[1]), end, grid, path, explored)
            if a:
                return a
        else:
            # Go toward by Y
            a = self.solve((start[0], int(start[1] + copysign(1, deltaY))), end, grid, path, explored)
            if a:
                return a
            # Go towards by X
            a = self.solve((int(start[0] + copysign(1, deltaX)), start[1]), end, grid, path, explored)
            if a:
                return a
            # Go away by X
            a = self.solve((int(start[0] - copysign(1, deltaX)), start[1]), end, grid, path, explored)
            if a:
                return a
            # Go away by Y
            a = self.solve((start[0], int(start[1] - copysign(1, deltaY))), end, grid, path, explored)
            if a:
                return a
        # If path doesn't work out then remove from explored
        explored.remove(path.pop())

    def find_path(self) -> LLStack|None:
        # Call solve method with proper inputs
        return self.solve(self.start_coords, self.end_coords, self.grid, LLStack(), set())
    
    def solve_shortest(self, start:tuple[int], end:tuple[int], grid:List[List[str|None]], curr_path:List[tuple[int]], best_path:LLStack = None) -> LLStack|None:
        """
        Solve for the path, return the shortest path

        Parameters:
        start:tuple[int]  Starting location - or current location on the path
        end:tuple[int]  Ending location
        grid:List[List[str|None]]  Grid to be traversed, the grid we are finding a path for
        curr_path:List[tuple[int]]  The current Path
        best_path:LLStack  The Best Path so far

        Return:
        LLStack or None, the shortest path, or None if no path is found
        
        """

        # If not in grid bounds
        if start[0] < 0 or start[0] >= len(grid) or start[1] < 0 or start[1] >= len(grid[start[0]]):
            return
        # If in an ocean
        if grid[start[0]][start[1]] == "ocean":
            return
        # If start in current path
        if start in curr_path:
            return
        # If best_path is not None and the length of the current path is longer than the best path
        if best_path and len(curr_path)+1 >= best_path.size:
            return
        # If at the ending coord
        if start == end:
            # Create a new best path LLStack
            best_path = LLStack()
            # Use shortest_helper to build the LLStack from the list
            self.solve_shortest_helper(curr_path, best_path)
            # Add the start coord as well
            best_path.push(start)
            # Return the best_path
            return best_path
        # Add the current start to the current path
        curr_path.append(start)
        # Create deltaX and deltaY variables
        deltaX = end[0] - start[0]
        deltaY = end[1] - start[1]
        # If further away in X than Y go towards it X first
        if abs(deltaX) > abs(deltaY):
            # Go towards by X
            a = self.solve_shortest((int(start[0] + copysign(1, deltaX)), start[1]), end, grid, curr_path, best_path)
            if a:
                best_path = a
            # Go towards by Y
            a = self.solve_shortest((start[0], int(start[1] + copysign(1, deltaY))), end, grid, curr_path, best_path)
            if a:
                best_path = a
            # Go towards by Y
            a = self.solve_shortest((start[0], int(start[1] - copysign(1, deltaY))), end, grid, curr_path, best_path)
            if a:
                best_path = a
            # Go towards by X
            a = self.solve_shortest((int(start[0] - copysign(1, deltaX)), start[1]), end, grid, curr_path, best_path)
            if a:
                best_path = a
        else:
            # Go towards by Y
            a = self.solve_shortest((start[0], int(start[1] + copysign(1, deltaY))), end, grid, curr_path, best_path)
            if a:
                best_path = a
            # Go towards by X
            a = self.solve_shortest((int(start[0] + copysign(1, deltaX)), start[1]), end, grid, curr_path, best_path)
            if a:
                best_path = a
            # Go towards by X
            a = self.solve_shortest((int(start[0] - copysign(1, deltaX)), start[1]), end, grid, curr_path, best_path)
            if a:
                best_path = a
            # Go towards by Y
            a = self.solve_shortest((start[0], int(start[1] - copysign(1, deltaY))), end, grid, curr_path, best_path)
            if a:
                best_path = a
        # If no paths from this start are fruitful then remove the start from the current path
        curr_path.remove(start)
        # After searching everything return the best path
        return best_path
    
    def solve_shortest_helper(self, curr_path:List[tuple[int]], best_path:LLStack) -> None:
        """
        Take curr_path as a list and create best_path as an LLStack

        Parameters:
        curr_path:List[tuple[int]]  The current Path
        best_path:LLStack  The Best Path so far

        Return:
        None, only manipulate the inputs using references
        
        """

        # If the length of the current path is 0
        if len(curr_path) <= 0:
            return
        # Add the 1st element of the current path to the best path
        best_path.push(curr_path[0])
        # Continue adding to the LLStack
        self.solve_shortest_helper(curr_path[1:], best_path)

    def find_shortest_path(self) -> LLStack|None:
        # Call solve_shortest method with proper inputs
        return self.solve_shortest(self.start_coords, self.end_coords, self.grid, [])