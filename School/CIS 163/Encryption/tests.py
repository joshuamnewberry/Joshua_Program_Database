import unittest
from encrypt import*

class TestSaltingEncrypting(unittest.TestCase):

    #Salting Non String Text Input
    def test_SaltingTextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = Salting(100, "Key")
    
    #Salting Non String Key Input
    def test_SaltingKeyNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = Salting("Cipher", 100)
    
    #Salting Key Value
    def test_SaltingKeyValue(self) -> None:
        a = Salting("Cipher", "GVSU")
        self.assertEqual(a.salt, "GVSU")
    
    #Salting Key Value Not Changed
    def test_SaltingKeyValueNoChange(self) -> None:
        a = Salting("Cipher", "GVSU")
        string = str(a)
        self.assertEqual(a.salt, "GVSU")
    
    #Salting Encrypted Value
    def test_SaltingEncrypted(self) -> None:
        a = Salting("Cipher", "GVSU")
        self.assertEqual(a.cipher_text, "CipherGVSU")
    
    #Salting Decrypted Value
    def test_SaltingDecrypted(self) -> None:
        a = Salting("Cipher", "GVSU")
        self.assertEqual(str(a), "Cipher")
    
    #Salting Blank Salt Input Encrypted
    def test_SaltingBlankTextEncrypt(self) -> None:
        a = Salting("", "Key")
        self.assertEqual(a.cipher_text, "Key")
    
    #Salting Blank Salt Input Decrypted
    def test_SaltingBlankTextDecrypt(self) -> None:
        a = Salting("", "Key")
        self.assertEqual(str(a), "")
    
class TestReverese1Encrypting(unittest.TestCase):
    
    #ReverseCipher1 Non String Text Input
    def test_Reverse1TextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = ReverseCipher1(100)
    
    #ReverseCipher1 Encrypted Value
    def test_Reverse1Encrypted(self) -> None:
        a = ReverseCipher1("Cipher In Reverse")
        self.assertEqual(a.cipher_text, "esreveR nI rehpiC")
    
    #ReverseCipher1 Decrypted Value
    def test_Reverse1Decrypted(self) -> None:
        a = ReverseCipher1("Cipher In Reverse")
        self.assertEqual(str(a), "Cipher In Reverse")

class TestReverse2Encrypting(unittest.TestCase):
    
    #ReverseCipher2 Non String Text Input
    def test_Reverse2TextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = ReverseCipher2(100)
    
    #ReverseCipher2 Encrypted Value
    def test_Reverse2Encrypted(self) -> None:
        a = ReverseCipher2("Cipher In Reverse")
        self.assertEqual(a.cipher_text, "rehpiC nI esreveR")
    
    #ReverseCipher2 Decrypted Value
    def test_Reverse2Decrypted(self) -> None:
        a = ReverseCipher1("Cipher In Reverse")
        self.assertEqual(str(a), "Cipher In Reverse")

class TestXOREncrypting(unittest.TestCase):
    
    #XORCipher Non String Text Input
    def test_XORTextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = XORCipher(100, "Key")
    
    #XORCipher Non String Key Input
    def test_XORKeyNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = XORCipher("Cipher", 100)
    
    #XORCipher Key Value
    def test_XORKeyValue(self) -> None:
        a = XORCipher("Cipher", "hidden")
        self.assertEqual(a.key, "hidden")
    
    #XORCipher Key Value Not Changed
    def test_XORKeyValueNoChange(self) -> None:
        a = XORCipher("Cipher", "hidden")
        string = str(a)
        self.assertEqual(a.key, "hidden")
    
    #XORCipher Encrypted Value
    def text_XOREncrypted(self) -> None:
        a = XORCipher("Cipher", "hidden")
        self.assertEqual(a.cipher_text, "+¶∟")
    
    #XORCipher Decrypted Value
    def text_XORDecrypted(self) -> None:
        a = XORCipher("Cipher", "hidden")
        self.assertEqual(str(a), "Cipher")

class TestCaesarEncrypting(unittest.TestCase):
    
    #CaesarCipher Non String Text Input
    def test_CaesarTextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = CaesarCipher(100, 10)
    
    #CaesarCipher Non Int Key Input
    def test_CaesarKeyNoInt(self) -> None:
        with self.assertRaises(TypeError):
            a = CaesarCipher("Cipher", "Key")
    
    #CaesarCipher Key Value
    def test_CaesarKeyValue(self) -> None:
        a = CaesarCipher("Cipher", 5)
        self.assertEqual(a.key, 5)
    
    #CaesarCipher Key Value Not Changed
    def test_CaesarKeyValueNoChange(self) -> None:
        a = CaesarCipher("Cipher", 5)
        string = str(a)
        self.assertEqual(a.key, 5)
    
    #CaesarCipher Positive Key Encrypted Value
    def test_CaesarEncryptedPos(self) -> None:
        a = CaesarCipher("Cipher", 5)
        self.assertEqual(a.cipher_text, "Hnumjw")
    
    #CaesarCipher Positive Key Decrypted Value
    def test_CaesarDecryptedPos(self) -> None:
        a = CaesarCipher("Cipher", 5)
        self.assertEqual(str(a), "Cipher")
    
    #CaesarCipher Big Positive Key Encrypted Value
    def test_CaesarEncryptedBigPos(self) -> None:
        a = CaesarCipher("Cipher", 100)
        self.assertEqual(a.cipher_text, "Yeldan")
    
    #CaesarCipher Big Positive Key Decrypted Value
    def test_CaesarDecryptedBigPos(self) -> None:
        a = CaesarCipher("Cipher", 100)
        self.assertEqual(str(a), "Cipher")
    
    #CaesarCipher Negative Key Encrypted Value
    def test_CaesarEncryptedNeg(self) -> None:
        a = CaesarCipher("Cipher", -5)
        self.assertEqual(a.cipher_text, "Xdkczm")
    
    #CaesarCipher Negative Key Decrypted Value
    def test_CaesarDecryptedNeg(self) -> None:
        a = CaesarCipher("Cipher", -5)
        self.assertEqual(str(a), "Cipher")
    
    #CaesarCipher Big Negative Key Encrypted Value
    def test_CaesarEncryptedNeg(self) -> None:
        a = CaesarCipher("Cipher", -100)
        self.assertEqual(a.cipher_text, "Gmtliv")
    
    #CaesarCipher Big Negative Key Decrypted Value
    def test_CaesarDecryptedNeg(self) -> None:
        a = CaesarCipher("Cipher", -100)
        self.assertEqual(str(a), "Cipher")

class TestVigenereEncrypting(unittest.TestCase):
    
    #VigenereCipher Non String Text Input
    def test_VigenereTextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = VigenereCipher(100, "Key")
    
    #VigenereCipher Non String Key Input
    def test_VigenereKeyNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = VigenereCipher("Cipher", 100)
    
    #VigenereCipher Key Value
    def test_VigenereKeyValue(self) -> None:
        a = VigenereCipher("Cipher", "Key")
        self.assertEqual(a.key, "Key")
    
    #VigenereCipher Key Value Not Changed
    def test_VigenereKeyValueNoChange(self) -> None:
        a = VigenereCipher("Cipher", "Key")
        string = str(a)
        self.assertEqual(a.key, "Key")
    
    #VigenereCipher Int Key Value
    def test_VigenereIntKeyValue(self) -> None:
        a = VigenereCipher("Cipher", "123")
        self.assertEqual(a.key, "123")
    
    #VigenereCipher Int Key Value Not Changed
    def test_VigenereIntKeyValueNoChange(self) -> None:
        a = VigenereCipher("Cipher", "123")
        string = str(a)
        self.assertEqual(a.key, "123")
    
    #VigenereCipher Normal Key Encrypted
    def test_VigenereEncryptedNormal(self) -> None:
        a = VigenereCipher("Cipher", "Key")
        self.assertEqual(a.cipher_text, "Mmnrip")
    
    #VigenereCipher Normal Key Decrypted
    def test_VigenereDecryptedNormal(self) -> None:
        a = VigenereCipher("Cipher", "Key")
        self.assertEqual(str(a), "Cipher")
    
    #VigenereCipher Specials Key Encrypted
    def test_VigenereEncryptedSpecials(self) -> None:
        a = VigenereCipher("CipherCipher", "!@#$%^&*()")
        self.assertEqual(a.cipher_text, "WhlecuBlqjyq")
    
    #VigenereCipher Specials Key Decrypted
    def test_VigenereDecryptedSpecials(self) -> None:
        a = VigenereCipher("CipherCipher", "!@#$%^&*()")
        self.assertEqual(str(a), "CipherCipher")
    
    #VigenereCipher Int Key Encrypted
    def test_VigenereEncryptedInt(self) -> None:
        a = VigenereCipher("CipherCipher", "1234567890")
        self.assertEqual(a.cipher_text, "DksljxJqyhft")
    
    #VigenereCipher Int Key Decrypted
    def test_VigenereDecryptedInt(self) -> None:
        a = VigenereCipher("CipherCipher", "1234567890")
        self.assertEqual(str(a), "CipherCipher")

class TestCustomMappingEncrypting(unittest.TestCase):
    
    #CustomMappingCipher Non String Text Input
    def test_CustomMappingTextNoStr(self) -> None:
        with self.assertRaises(TypeError):
            a = CustomMappingCipher(100)
    
    #CustomMappingCipher Encrypted
    def test_CustomMappingEncrypted(self) -> None:
        a = CustomMappingCipher("Cipher")
        self.assertEqual(a.cipher_text, "G>`wkx")
    
    #CustomMappingCipher Decrypted
    def test_CustomMappingDecrypted(self) -> None:
        a = CustomMappingCipher("Cipher")
        self.assertEqual(str(a), "Cipher")
    
    #CustomMappingCipher Special Characters Encrypted
    def test_CustoMappingSpecialEncrypted(self) -> None:
        a  = CustomMappingCipher("Hello!@#$%^&*()")
        self.assertEqual(a.cipher_text, 'gkPP"Q-h)X9dE.v')
    
    #CustomMappingCipher Special Characters Decrypted
    def test_CustoMappingSpecialEncrypted(self) -> None:
        a  = CustomMappingCipher("Hello!@#$%^&*()")
        self.assertEqual(str(a), "Hello!@#$%^&*()")

if __name__ == "__main__":
    unittest.main()