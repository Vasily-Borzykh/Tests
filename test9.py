import math

class GeometryLibrary:
    
    @staticmethod
    def circle_square(radius):
        return math.pi * radius**2
    
    @staticmethod
    def triangle_square(a, b, c):
        if GeometryLibrary.valid_triangle(a, b, c):
            p = (a + b + c) / 2
            s = math.sqrt(p * (p -a) * (p - b) * (p - c))
            return s
        else:
            print("Triangle is not valid!")
        
    @staticmethod
    def valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a
    
    @staticmethod
    def right_triangle(a, b, c):
        sides = [a, b, c]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2
    
circle_radius = 4
circle_square = GeometryLibrary.circle_square(circle_radius)
print(f"Circle square = {circle_square}")

triangle_sides = [3, 4, 5]
triangle_square = GeometryLibrary.triangle_square(*triangle_sides)
if (triangle_square != None):
    print(f"Triangle square = {triangle_square}")

if GeometryLibrary.right_triangle(*triangle_sides):
    print("This is right triangle")
else:
    print("This is NOT right triangle")