# Constructors
class Point:
    def __init__(self, x, y):   # Now with this method[__init__(self, x, y)] we constructed a beginning of what we are creating
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)
point.x = 15    # Now this changes the value of point.x so try printing point.x again to see
