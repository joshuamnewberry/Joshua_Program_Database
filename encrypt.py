class Salting:
    def __init__(self, text:str, salt:str) -> None:
        if type(text) != str or type(salt) != str:
            raise TypeError
        self.cipher_text = str(text)
        self.salt = str(salt)
        self.cipher_text += self.salt
    
    def __str__(self) -> str:
        return self.cipher_text[0:len(self.cipher_text)-len(self.salt)]

class ReverseCipher1:
    def __init__(self, text:str) -> None:
        if type(text) != str:
            raise TypeError
        self.cipher_text = str(text)
        reverse_str = ""
        for i in self.cipher_text:
            reverse_str = i + reverse_str
        self.cipher_text = reverse_str
    
    def __str__(self) -> str:
        reverse_str = ""
        for i in self.cipher_text:
            reverse_str = i + reverse_str
        return reverse_str

class ReverseCipher2:
    def __init__(self, text:str) -> None:
        if type(text) != str:
            raise TypeError
        self.cipher_text = str(text)
        reverse_word_list = []
        words_list = self.cipher_text.split()
        for word in words_list:
            reverse_str = ""
            for letter in word:
                reverse_str = letter + reverse_str
            reverse_word_list.append(reverse_str)
        reverse_cipher = ""
        for word in reverse_word_list:
            reverse_cipher += " " + word
        self.cipher_text = reverse_cipher.strip()

    def __str__(self) -> str:
        reverse_word_list = []
        words_list = self.cipher_text.split()
        for word in words_list:
            reverse_str = ""
            for letter in word:
                reverse_str = letter + reverse_str
            reverse_word_list.append(reverse_str)
        reverse_cipher = ""
        for word in reverse_word_list:
            reverse_cipher += " " + word
        return reverse_cipher.strip()

class XORCipher:
    def __init__(self, text:str, key:str) -> None:
        if type(text) != str or type(key) != str:
            raise TypeError
        self.cipher_text = str(text)
        self.key = str(key)
        cipher_str = ""
        key_length = len(self.key)
        for i in range(len(self.cipher_text)):
            key_index = i
            while key_index >= key_length:
                key_index -= key_length
            cipher_num = ord(self.cipher_text[i])
            key_num = ord(self.key[key_index])
            new_num = cipher_num ^ key_num
            cipher_str += chr(new_num)
        self.cipher_text = cipher_str

    def __str__(self) -> str:
        cipher_str = ""
        key_length = len(self.key)
        for i in range(len(self.cipher_text)):
            key_index = i
            while key_index >= key_length:
                key_index -= key_length
            cipher_num = ord(self.cipher_text[i])
            key_num = ord(self.key[key_index])
            new_num = cipher_num ^ key_num
            cipher_str = cipher_str + chr(new_num)
        return cipher_str

class CaesarCipher:
    def __init__(self, text:str, key:int) -> None:
        if type(text) != str or type(key) != int:
            raise TypeError
        self.cipher_text = text
        self.key = key
        cipher_str = ""
        for i in self.cipher_text:
            if i.isalpha():
                cipher_num = ord(i)
                cipher_num += self.key
                if(i.isupper()):
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                else:
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26
                cipher_str += chr(cipher_num)
            else:
                cipher_str += i
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        cipher_str = ""
        for i in self.cipher_text:
            if i.isalpha():
                cipher_num = ord(i)
                cipher_num -= self.key
                if(i.isupper()):
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                else:
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26 
                cipher_str += chr(cipher_num)
            else:
                cipher_str += i
        return cipher_str

class VigenereCipher:
    def __init__(self, text:str, key:str) -> None:
        if type(text) != str or type(key) != str:
            raise TypeError
        self.cipher_text = text
        self.key = key
        cipher_str = ""
        key_length = len(self.key)
        for i in range (0, len(self.cipher_text)):
            if self.cipher_text[i].isalpha():
                cipher_letter = self.cipher_text[i]
                key_index = i
                while key_index >= key_length:
                    key_index -= key_length
                key_num = 0
                try:
                    key_num = int(self.key[key_index])
                except:
                    key_num = ord(self.key[key_index].upper()) - 65
                cipher_num = ord(cipher_letter) + key_num
                if cipher_letter.isupper():
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                elif cipher_letter.islower():
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26
                cipher_str += chr(cipher_num)
            else:
                cipher_str += self.cipher_text[i]
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        cipher_str = ""
        key_length = len(self.key)
        for i in range (0, len(self.cipher_text)):
            if self.cipher_text[i].isalpha():
                cipher_letter = self.cipher_text[i]
                key_index = i
                while key_index >= key_length:
                    key_index -= key_length
                key_num = 0
                try:
                    key_num = int(self.key[key_index])
                except:
                    key_num = ord(self.key[key_index].upper()) - 65
                cipher_num = ord(cipher_letter) - key_num
                if cipher_letter.isupper():
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                elif cipher_letter.islower():
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26
                cipher_str += chr(cipher_num)
            else:
                cipher_str += self.cipher_text[i]
        return cipher_str

class CustomMappingCipher:
    character_map = {
    'a': ',', 'b': 'c', 'c': '/', 'd': '&', 'e': 'k', 'f': '}', 'g': '4', 'h': 'w', 
    'i': '>', 'j': 'b', 'k': 'W', 'l': 'P', 'm': 'V', 'n': '$', 'o': '"', 'p': '`', 
    'q': 'U', 'r': 'x', 's': '~', 't': 'o', 'u': 'K', 'v': 'B', 'w': ']', 'x': 'e', 
    'y': '[', 'z': '7', 'A': 'H', 'B': 'i', 'C': 'G', 'D': 's', 'E': ';', 'F': 'A', 
    'G': 'y', 'H': 'g', 'I': 'r', 'J': '%', 'K': 'p', 'L': '^', 'M': 'C', 'N': '6', 
    'O': 'O', 'P': '8', 'Q': '3', 'R': '\\', 'S': '5', 'T': '0', 'U': 'Y', 'V': '1', 
    'W': '+', 'X': '{', 'Y': '2', 'Z': 'D', '0': '(', '1': '=', '2': '?', '3': 'q', 
    '4': '<', '5': 't', '6': 'f', '7': 'L', '8': '|', '9': 'l', '!': 'Q', '"': 'F', 
    '#': 'h', '$': ')', '%': 'X', '&': 'd', "'": 'j', '(': '.', ')': 'v', '*': 'E', 
    '+': "'", ',': '#', '-': '@', '.': '*', '/': 'z', ':': 'S', ';': ':', '<': 'N', 
    '=': 'Z', '>': ' ', '?': 'T', '@': '-', '[': 'R', '\\': 'u', ']': 'M', '^': '9', 
    '_': '_', '`': 'a', '{': 'n', '|': 'I', '}': 'J', '~': '!', ' ': 'm' }
    
    def __init__(self, text:str) -> None:
        if type(text) != str:
            raise TypeError
        self.cipher_text = str(text)
        cipher_str = ""
        for i in self.cipher_text:
            cipher_str += CustomMappingCipher.character_map[i]
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        cipher_str = ""
        key_list = list(CustomMappingCipher.character_map.keys())
        val_list = list(CustomMappingCipher.character_map.values())
        for i in self.cipher_text:
            cipher_str += key_list[val_list.index(i)]
        return cipher_str