from kingdom import kingdom
import unittest

class testkingdom(unittest.TestCase):

    def test_check_if_object_is_created(self):
        kingdomobject = kingdom("testname", "testemblem")

        self.assertEqual(kingdomobject.get_name(), "testname")

    

if __name__ == "__main__":
    unittest.main()