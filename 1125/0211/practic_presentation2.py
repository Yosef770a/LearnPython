class Point:
   def __init__(self, x: float = 0, y: float = 0):
       self.x = x
       self.y = y

   @staticmethod
   def distance(p1, p2):
       dx = p1.x - p2.x
       dy = p1.y - p2.y
       return (dx**2 + dy**2) ** 0.5
   



class Line:
    count = 0  
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        Line.count += 1

    def show(self):
        print(f"Point a: ({self.a.x}, {self.a.y}), Point b: ({self.b.x}, {self.b.y})")

    def length(self):
        return Point.distance(self.a, self.b)

    @classmethod
    def how_many(cls):
        print(f"Number of line objects: {cls.count}")

    @staticmethod
    def is_horizontal(line):

        if line.a.y == line.b.y:
            return True
        else:
            return False
        
    @staticmethod
    def is_vertical(line):
        if line.a.x == line.b.x:
            return True
        else:
            return False




# line1 = Line(Point(3,5),Point(3,4))
# line1.show()

point1 = Point(2,4)
point2 = Point(2,4)
point3 = Point(4,3)
point4 = Point(5,3)

line1 = Line(point1, point2)
line2 = Line(point3, point4)

Line.how_many()

print(Line.is_horizontal(line1))
print(Line.is_vertical(line2))
