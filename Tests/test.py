import unittest
import sys
sys.path.append("C:/Users/kiril/.vscode/ProjectTemplates/example/AreaOfFigure")
from shapeClasses import Circle, Triangle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)  

class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6.0)
        
    def test_isRect(self):
        triangle1 = Triangle(3, 4, 5)
        self.assertTrue(triangle1.isRect())  
        triangle2 = Triangle(3, 4, 6)
        self.assertFalse(triangle2.isRect())  

if __name__ == '__main__':
    unittest.main()