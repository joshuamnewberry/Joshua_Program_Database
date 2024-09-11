# All of these classese are different forms of encryption with varying difficulty

# Salting adds a "salt" to the end of the cipher, possibly confusing some people
class Salting:
    
    def __init__(self, text:str, salt:str) -> None:
        """
        Initialize the object and store the key and encrypted cipher

        Parameters:
        text:str the text to get encrypted
        salt:str the salt getting added as encryption

        Return:
        None

        """
        # If either variable is not a string raise a TypeError
        if type(text) != str or type(salt) != str:
            raise TypeError
            
        # Store both variables
        self.cipher_text = text + salt
        self.salt = salt
    
    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the encrypted version or key

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Return the cipher excluding the salt at the end
        return self.cipher_text[0:len(self.cipher_text)-len(self.salt)]

# Reverse1 reverses the entire string making it slightly harder to read/understand
class ReverseCipher1:
    def __init__(self, text:str) -> None:
        """
        Initialize the object and store the encrypted cipher

        Parameters:
        text:str the text to get encrypted

        Return:
        None

        """
        # If the variable is not a string raise a TypeError
        if type(text) != str:
            raise TypeError
        # Store the unencrypted text temporarily
        self.cipher_text = text
        # Create an empty string
        reverse_str = ""
        # For every letter, add it to the beginning of the string
        for i in self.cipher_text:
            reverse_str = i + reverse_str
        # Store the reversed string
        self.cipher_text = reverse_str

    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the encrypted version

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Create an empty string
        reverse_str = ""
        # For every letter, add it to the beginning of the string
        for i in self.cipher_text:
            reverse_str = i + reverse_str
        # Return the unreversed string
        return reverse_str

# Reverse2 reverses individual words keeping the sentence in the same order
class ReverseCipher2:
    def __init__(self, text:str) -> None:
        """
        Initialize the object and store the encrypted cipher

        Parameters:
        text:str the text to get encrypted

        Return:
        None

        """
        # If the variable is not a string raise a TypeError
        if type(text) != str:
            raise TypeError
        # Store the unencrypted string temporarily
        self.cipher_text = text
        # Create an empty list of reversed words
        reverse_word_list = []
        # Split the unencrypted string into a list of words
        words_list = self.cipher_text.split()
        # For each word in the list reverse it and store in the reversed list
        for word in words_list:
            # Create an empty string
            reverse_str = ""
            # For every letter in the word add it to the beginning of the string
            for letter in word:
                reverse_str = letter + reverse_str
            # Add to the list of reversed words
            reverse_word_list.append(reverse_str)
        # Create an empty string
        reverse_cipher = ""
        # For every word in the reversed word list add it to the string with a space for the next word
        for word in reverse_word_list:
            reverse_cipher += " " + word
        # Strip any whitespace and store the encrypted string
        self.cipher_text = reverse_cipher.strip()
    
    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the encrypted version

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Create an empty list of reversed words
        reverse_word_list = []
        # Split the encrypted string into a list of words
        words_list = self.cipher_text.split()
        # For each word in the list reverse it and store in the reversed list
        for word in words_list:
            # Create an empty string
            reverse_str = ""
            # For every letter in the word add it to the beginning of the string
            for letter in word:
                reverse_str = letter + reverse_str
            # Add to the list of reversed words
            reverse_word_list.append(reverse_str)
        # Create an empty string
        reverse_cipher = ""
        # For every word in the reversed word list add it to the string with a space for the next word
        for word in reverse_word_list:
            reverse_cipher += " " + word
        # Strip any whitespace and return the unencrypted string
        return reverse_cipher.strip()

# XOR performs an XOR operation between the cipher and the key creating a completely unreadable
# string that is decrypted by performing the operation again with the same key
class XORCipher:
    def __init__(self, text:str, key:str) -> None:
        """
        Initialize the object and store the key and encrypted cipher

        Parameters:
        text:str the text to get encrypted
        key:str the key used to encrypt

        Return:
        None

        """
        # If either variable is not a string raise a TypeError
        if type(text) != str or type(key) != str:
            raise TypeError
        # Temporarily store the unencrypted string
        self.cipher_text = text
        # Store the key
        self.key = key
        # Create an empty string
        cipher_str = ""
        # Store the key length for later use
        key_length = len(self.key)
        # Loop over the cipher index's and perform the XOR operation, storing each 
        # new character in the new string
        for i in range(len(self.cipher_text)):
            # Create a key index variable
            key_index = i
            # Subtract the key length until it is within the bounds of the key length
            while key_index >= key_length:
                key_index -= key_length
            # Store the ASCII number of the cipher character
            cipher_num = ord(self.cipher_text[i])
            # Store the ASCII number of the key character
            key_num = ord(self.key[key_index])
            # Perform the XOR operation
            new_num = cipher_num ^ key_num
            # Add the new character to the new string
            cipher_str += chr(new_num)
        # Store the encrypted string
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the key or the encrypted version

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Create an empty string
        cipher_str = ""
        # Store the key length for later use
        key_length = len(self.key)
        # Loop over the cipher index's and perform the XOR operation, storing each 
        # new character in the new string
        for i in range(len(self.cipher_text)):
            # Create a key index variable
            key_index = i
            # Subtract the key length until it is within the bounds of the key length
            while key_index >= key_length:
                key_index -= key_length
            # Store the ASCII number of the cipher character
            cipher_num = ord(self.cipher_text[i])
            # Store the ASCII number of the key character
            key_num = ord(self.key[key_index])
            # Perform the XOR operation
            new_num = cipher_num ^ key_num
            # Add the new character to the new string
            cipher_str += chr(new_num)
        # Return the unencrypted string
        return cipher_str

# Caesar shifts the letters of the cipher by a set integer, looping from z back to a, preserving 
# uppercase and lowercase and keeping spaces and special characters the same
class CaesarCipher:
    def __init__(self, text:str, key:int) -> None:
        """
        Initialize the object and store the key and encrypted cipher

        Parameters:
        text:str the text to get encrypted
        key:int the key used to encrypt

        Return:
        None

        """
        # If either variable is not a string raise a TypeError
        if type(text) != str or type(key) != int:
            raise TypeError
        # Temporarily store the unencrypted text
        self.cipher_text = text
        # Store the key
        self.key = key
        # Create a new string
        cipher_str = ""
        # Loop over the cipher text shifting each individual letter and skipping special characters
        for i in self.cipher_text:
            # If the character is a letter
            if i.isalpha():
                # Store the ASCII number
                cipher_num = ord(i)
                # Add the shift int
                cipher_num += self.key
                # If the character is upper
                if i.isupper():
                    # Add or subtract 26 until between 65 and 90
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                # If the character is lower
                elif i.islower():
                    # Add or subtract 26 until between 97 and 122
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26
                # Convert back to character and add to the new string
                cipher_str += chr(cipher_num)
            # Else add the special character or space to the new string
            else:
                cipher_str += i
        # Store the encrypted string
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the key or the encrypted version

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Create a new string
        cipher_str = ""
        # Loop over the cipher text shifting each individual letter and skipping special characters
        for i in self.cipher_text:
            # If the character is a letter
            if i.isalpha():
                # Store the ASCII number
                cipher_num = ord(i)
                # Subtract the shift int
                cipher_num -= self.key
                # If the character is upper
                if i.isupper():
                    # Add or subtract 26 until between 65 and 90
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                # If the character is lower
                elif i.islower():
                    # Add or subtract 26 until between 97 and 122
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26 
                cipher_str += chr(cipher_num)
            # Else add the special character or space to the new string
            else:
                cipher_str += i
        # Return the unencrypted string
        return cipher_str

# Vigenere converts the text and key into nubmers: A:0, B:1, C:2... and adds them together, looping from z back to a, not altering
# special characters in the text and converting back to a string that is unreadable and harder to crack than Caesar
class VigenereCipher:
    def __init__(self, text:str, key:str) -> None:
        """
        Initialize the object and store the key and encrypted cipher

        Parameters:
        text:str the text to get encrypted
        key:str the key used to encrypt

        Return:
        None

        """
        # If either variable is not a string raise a TypeError
        if type(text) != str or type(key) != str:
            raise TypeError
        # Temporarily store the unencrypted text
        self.cipher_text = text
        # Store the key
        self.key = key
        # Create a new string
        cipher_str = ""
        # Store the key length for later use
        key_length = len(self.key)
        # Loop over the cipher index's "add" the key and text, storing each 
        # new character in the new string
        for i in range (0, len(self.cipher_text)):
            # If the character is a letter
            if self.cipher_text[i].isalpha():
                # Store the letter
                cipher_letter = self.cipher_text[i]
                # Store the key index
                key_index = i
                # Subtract the key length until within the bounds
                while key_index >= key_length:
                    key_index -= key_length
                # Initialize the key num variable
                key_num = 0
                # Try to store as an int
                try:
                    key_num = int(self.key[key_index])
                # If not an int then convert to ASCII number of the upper case letter (if applicable)
                # and subtract 65 to standardize (A = 65 in ASCII)
                except:
                    key_num = ord(self.key[key_index].upper()) - 65
                # Add the key number to the cipher lettter's ASCII number
                cipher_num = ord(cipher_letter) + key_num
                # If the character is upper
                if cipher_letter.isupper():
                    # Add or subtract 26 until between 65 and 90
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                # If the character is lower
                elif cipher_letter.islower():
                    # Add or subtract 26 until between 97 and 122
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26 
                # Convert back into a character and add to the new string
                cipher_str += chr(cipher_num)
            # Else add the special character or space to the new string
            else:
                cipher_str += self.cipher_text[i]
        # Store the encrypted cipher
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the key or the encrypted version

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Create an empty string
        cipher_str = ""
        # Store the key length for later use
        key_length = len(self.key)
        # Loop over the cipher index's "subtract" the key from the text, storing each 
        # new character in the new string
        for i in range (0, len(self.cipher_text)):
            # If the character is a letter
            if self.cipher_text[i].isalpha():
                # Store the letter
                cipher_letter = self.cipher_text[i]
                # Store the key index
                key_index = i
                # Subtract the key length until within the bounds
                while key_index >= key_length:
                    key_index -= key_length
                # Initialize the key num variable
                key_num = 0
                # Try to store as an int
                try:
                    key_num = int(self.key[key_index])
                # If not an int then convert to ASCII number of the upper case letter (if applicable)
                # and subtract 65 to standardize (A = 65 in ASCII)
                except:
                    key_num = ord(self.key[key_index].upper()) - 65
                # Subtract the key number to the cipher lettter's ASCII number
                cipher_num = ord(cipher_letter) - key_num
                # If the character is upper
                if cipher_letter.isupper():
                    # Add or subtract 26 until between 65 and 90
                    while cipher_num > 90:
                        cipher_num -= 26
                    while cipher_num < 65:
                        cipher_num += 26
                # If the character is lower
                elif cipher_letter.islower():
                    # Add or subtract 26 until between 97 and 122
                    while cipher_num > 122:
                        cipher_num -= 26
                    while cipher_num < 97:
                        cipher_num += 26 
                # Convert back into a character and add to the new string
                cipher_str += chr(cipher_num)
            # Else add the special character or space to the new string
            else:
                cipher_str += self.cipher_text[i]
        # Return the unencrypted string
        return cipher_str

# CustomMapping uses a custom made dictionary to translate the text into an unreadable cipher decoded using the dictionary
class CustomMappingCipher:
    # Dictionary key
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
        """
        Initialize the object and store the encrypted cipher

        Parameters:
        text:str the text to get encrypted

        Return:
        None

        """
        # If the variable is not a string raise a TypeError
        if type(text) != str:
            raise TypeError
        # Temporarily store the unencrypted string
        self.cipher_text = text
        # Create an empty string
        cipher_str = ""
        # For each character in the text pull the corresponding value from the dictionary and add to the string
        for i in self.cipher_text:
            cipher_str += CustomMappingCipher.character_map[i]
        # Store the encrypted string
        self.cipher_text = cipher_str
    
    def __str__(self) -> str:
        """
        Return the unencrypted cipher without modifying the encrypted version

        Parameters:
        None

        Return:
        text:str the unencrypted original text

        """
        # Create an empty string
        cipher_str = ""
        # Create a list of dictionary keys
        key_list = list(CustomMappingCipher.character_map.keys())
        # Create a list of dictionary values
        val_list = list(CustomMappingCipher.character_map.values())
        # For each character in the cipher pull the index from the value list, and input the index in the key list
        # Add the corresponding character to the string
        for i in self.cipher_text:
            cipher_str += key_list[val_list.index(i)]
        # Return the unencrypted cipher
        return cipher_str
