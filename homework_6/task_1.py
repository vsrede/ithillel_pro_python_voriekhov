class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    my_circle_one = Circle(-25, -25, 100)
    my_point_one = Point(-50, -50)

    my_circle_two = Circle(5, 4, 2)
    my_point_two = Point(1, 3)

    print(my_circle_one.contains(my_point_one))
    print(my_circle_two.contains(my_point_two))


if __name__ == '__main__':
    main()
