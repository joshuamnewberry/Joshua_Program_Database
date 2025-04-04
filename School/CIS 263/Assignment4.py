import array

class Hash:

    def __init__(self, table:array = None, size:int = 11) -> None:
        if table is None:
            table = [None] * size
        self.__table = table
        self.__size = size
    
    def  __str__(self) -> str:
        res = ""
        for element in self.__table:
            if element is not None:
                res += str(element) + " "
        return res.strip()
    
    def hash(self, x:int) -> int:
        return x % self.__size
    
    def hash2(self, x:int) -> int:
        return 7 - (x % 7)

    def linearProbe(self, x:int) -> None:
        index = self.hash(x)
        i = 1
        while self.__table[index] is not None:
            index = self.hash(x+i)
            i += 1
        self.__table[index] = x
    
    def quadraticProbe(self, x:int) -> None:
        index = self.hash(x)
        i = 1
        while self.__table[index] is not None:
            index = self.hash(x+pow(i,2))
            i += 1
        self.__table[index] = x
    
    def doubleHashProbe(self, x:int) -> None:
        index = self.hash(x)
        i = 1
        while self.__table[index] is not None:
            index = self.hash(x+(i*self.hash2(x)))
            i += 1
        self.__table[index] = x

hash1 = Hash()
lst = [14, 7, 22, 0, 13, 2, 9, 5]
for element in lst:
    hash1.linearProbe(element)
print(f"Linear Probing: {hash1}")
hash2 = Hash()
for element in lst:
    hash2.quadraticProbe(element)
print(f"Quadratic Probing: {hash2}")
hash3 = Hash()
for element in lst:
    hash3.doubleHashProbe(element)
print(f"Double Hashing: {hash3}")