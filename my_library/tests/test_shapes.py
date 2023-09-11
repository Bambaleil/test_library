import unittest

from my_library.shapes import Circle, Triangle


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_is_right_triangle(self):
        triangle1 = Triangle(3, 4, 5)
        self.assertTrue(triangle1.is_right_triangle())

        triangle2 = Triangle(1, 2, 3)
        self.assertFalse(triangle2.is_right_triangle())

if __name__ == '__main__':
    unittest.main()