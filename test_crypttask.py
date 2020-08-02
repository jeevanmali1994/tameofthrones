from crypttask import crypttask
import unittest

class test_crypttask(unittest.TestCase):
    
    def test_check_encryption_for_key_zero(self):
        crypttaskobject = crypttask(0)

        self.assertEqual(crypttaskobject.encrypt("ABC"), "ABC")

    def test_check_encryption_for_key_twentyfive(self):
        crypttaskobject = crypttask(25)

        self.assertEqual(crypttaskobject.encrypt("ABC"), "ZAB")

    
    def test_check_encryption_for_key_fifteen(self):
        crypttaskobject = crypttask(15)

        self.assertEqual(crypttaskobject.encrypt("ZYX"), "ONM")



if __name__ == "__main__":
    unittest.main()