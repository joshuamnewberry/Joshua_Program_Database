import unittest
from BankClass import Bank, LowBalanceError, NonPositiveError

class TestBankClass(unittest.TestCase):

    def testCustomerName(self) -> None:
        a = Bank("Joe", 500)
        self.assertEqual(a.name, "Joe")

    def testCustomerBalance(self) -> None:
        a = Bank("Joe", 500)
        self.assertEqual(a.balance, 500)
    
    def testCustomerBalanceStr(self) -> None:
        with self.assertRaises(TypeError):
            a = Bank("Joe", "abc")
    
    def testDepositStr(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(TypeError):
            a.deposit("abc")
    
    def testDepositFloat(self) -> None:
        a = Bank("Joe", 500)
        a.deposit(2.5)
        self.assertEqual(a.balance, 502.5)
    
    def testDepositInt(self) -> None:
        a = Bank("Joe", 500)
        a.deposit(12)
        self.assertEqual(a.balance, 512)
    
    def testDepositZero(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(NonPositiveError):
            a.deposit(0)
    
    def testDepositNegative(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(NonPositiveError):
            a.deposit(-100)
    
    def testWithdrawStr(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(TypeError):
            a.withdraw("abc")
    
    def testWithdrawFloat(self) -> None:
        a = Bank("Joe", 500)
        a.withdraw(15.499)
        self.assertEqual(a.balance, 484.501)
    
    def testWithdrawInt(self) -> None:
        a = Bank("Joe", 500)
        a.withdraw(16)
        self.assertEqual(a.balance, 484)
    
    def testWithdrawZero(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(NonPositiveError):
            a.withdraw(0)
    
    def testWithdrawNegative(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(NonPositiveError):
            a.withdraw(-100)
    
    def testOverWithdraw(self) -> None:
        a = Bank("Joe", 500)
        with self.assertRaises(LowBalanceError):
            a.withdraw(750)

if __name__ == "__main__":
    unittest.main()
