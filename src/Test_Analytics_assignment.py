# Analytics_assignment.py
import unittest

from Analytics_assignment import SAA

class TestSAA(unittest.TestCase):
    def tes_init(self):
        gradebook = SAA()
        self.assertEqual(gradebook.grades["A"],"A")
        
    def test_avg_fGrade(self):
        gradebook = SAA()
        self.assertEqual(gradebook.avg_fGrade(),"B")
    
    def test_avg_Change(self):
        gradebook = SAA()
        self.assertEqual(round(gradebook.avg_Change(),2),round(-0.3146067415730337,2))
        
    def test_count_Grade(self):
        gradebook = SAA()
        self.assertEqual(gradebook.count_Grade()['A'],43)
        
    def test_count_Sex(self):
        gradebook = SAA()
        self.assertEqual(gradebook.count_Sex()['M'],72)
        
if __name__ == '__main__':
    unittest.main()