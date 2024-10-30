class Coord:
    def __init__(self, x:int, y:int) -> None:
        if type(x) == int and type(y) == int:
            self.__x = x
            self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"