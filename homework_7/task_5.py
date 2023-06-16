class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    # def contains(self, point):
    #     return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2
    def __contains__(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    print(Point(1, 2) in Circle(1, 2, 10))


if __name__ == '__main__':
    main()
