from communication import communication
from kingdom import kingdom
import unittest

class test_communication(unittest.TestCase):
    def setUp(self):
        self.kingdomobject = kingdom("TESTNAME", "T")
        

    def test_message_validity_when_invalid(self):
        communicationobject =communication("TESTMESSAGE", self.kingdomobject)

        self.assertFalse(communicationobject.is_valid_message())
    
    def test_message_validity_when_valid(self):
        communicationobject =communication("U", self.kingdomobject)
        
        self.assertTrue(communicationobject.is_valid_message())



if __name__ == "__main__":
    unittest.main()