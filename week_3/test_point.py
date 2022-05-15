import unittest
from point import Point2D, Point3D


class TestPoint2D(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # создать две точки
        self.p1 = Point2D(10, 20)
        self.p2 = Point2D(30, 40)

    @classmethod
    def tearDownClass(self):
        # обнулить счетчик точек для следующих тестов
        self.p1.__class__._points_count = 0

    def test_point_values(self):
        """Проверка координат точек"""
        self.assertEqual(self.p1.x, 10)
        self.assertEqual(self.p2.x, 30)
        self.assertEqual(self.p1.y, 20)
        self.assertEqual(self.p2.y, 40)

    def test_points_count(self):
        """Проверка счетчика точек"""
        self.assertEqual(self.p1.points_count, 2)

    def test_distance(self):
        """Проверка рассчета расстояния между точками"""
        self.assertEqual(self.p1.distance(self.p2), 28.28)

    def test_string_represantation(self):
        """Проверка строкового представления точки"""
        self.assertEqual(str(self.p1), '(10, 20)')


class TestPoint3D(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # создать две точки
        self.p1 = Point3D(10, 20, 30)
        self.p2 = Point3D(40, 50, 60)

    def test_point_values(self):
        """Проверка координат точек"""
        self.assertEqual(self.p1.x, 10)
        self.assertEqual(self.p1.y, 20)
        self.assertEqual(self.p1.z, 30)
        self.assertEqual(self.p2.x, 40)
        self.assertEqual(self.p2.y, 50)
        self.assertEqual(self.p2.z, 60)

    def test_points_count(self):
        """Проверка счетчика точек"""
        self.assertEqual(self.p1.points_count, 2)

    def test_distance(self):
        """Проверка рассчета расстояния между точками"""
        self.assertEqual(self.p1.distance(self.p2), 51.96)

    def test_string_represantation(self):
        """Проверка строкового представления точки"""
        self.assertEqual(str(self.p1), '(10, 20, 30)')


if __name__ == "__main__":
    unittest.main()
