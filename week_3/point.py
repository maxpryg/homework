class Point2D():
    """Класс представляет точку с двумя координатами (x, y)"""

    # счетчик экземпляров
    _points_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__._points_count += 1

    def distance(self, point):
        """Расстояние между точками"""
        return round(((self.x - point.x) ** 2 +
                      (self.y - point.y) ** 2) ** 0.5, 2)

    @property
    def points_count(self):
        return self.__class__._points_count

    def __str__(self):
        return f"{self.x, self.y}"


class Point3D(Point2D):
    """Класс представляет точку с тремя координатами (x, y, z)"""

    # можно обнулить счетчик, если нужно считать количество экземпляров каждого
    # класса отдельно
    # _points_count = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        """Расстояние между точками"""
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2 +
                (self.z - point.z) ** 2) ** 0.5, 2)

    def __str__(self):
        return f"{self.x, self.y, self.z}"


if __name__ == "__main__":
    # создать две точки Point2D
    p1 = Point2D(10, 20)
    p2 = Point2D(30, 40)
    print(f"Точки Point2D: {p1}, {p2}")
    print(f"Количество точек: {p1.points_count}")
    print(f"Расстояние между точками: {p1.distance(p2)}")
    print()
    # создать две точки Point3D
    p3 = Point3D(10, 20, 30)
    p4 = Point3D(10, 50, 30)
    print(f"Точки Point3D: {p3}, {p4}")
    print(f"Количество точек: {p3.points_count}")
    print(f"Расстояние между точками: {p3.distance(p4)}")
