from typing import List

def checkSpot(x:int, y:int, board:List[List[bool]]):
    # Check along x axis
    for checkX in range(0, len(board[y])):
        if checkX != x:
            if board[y][checkX]:
                return False
    # Check along y axis
    for checkY in range(0, len(board)):
        if checkY != y:
            if board[checkY][x]:
                return False
    # Check top left diagonal
    checkX = x-1
    checkY = y-1
    while checkX >= 0 and checkY >= 0:
        if board[checkY][x]:
            return False
        checkX -= 1
        checkY -= 1
    # Check top right diagonal
    checkX = x+1
    checkY = y-1
    while checkY >= 0 and checkX < len(board[y]):
        if board[checkY][x]:
            return False
        checkX += 1
        checkY -= 1
    # Check bottom left diagonal
    checkX = x-1
    checkY = y+1
    while checkX >= 0 and checkY < len(board):
        if board[checkY][x]:
            return False
        checkX -= 1
        checkY += 1
    # Check bottom right diagonal
    checkX = x+1
    checkY = y+1
    while checkY < len(board) and checkX < len(board[y]):
        if board[checkY][x]:
            return False
        checkX += 1
        checkY += 1
    return True

def checkBoard(board:List[List[bool]]) -> bool:
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]:
                if not checkSpot(x, y, board):
                    return False
    return True