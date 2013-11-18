import unittest
import mycode

class TestFunction(unittest.TestCase):
    
    def setUp(self):
        self.data=mycode.data_company()
    
    def test_data(self):
        self.assertEqual(self.data, mycode.data_company())
        

if __name__ == '__main__':
    unittest.main()
