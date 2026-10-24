class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def __eq__(self, other):
        return self.length == other.length and self.width == other.width
    
    def __hash__(self):
        return self.length + self.width
    

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

print(id(r1), id(r2))  # 1986385439312 1986388134800, diff objects

print(r1 == r2)  # True, equal to each other

print(hash(r1))  # 30
print(hash(r2))  # 30, have the same hash

rectangles = {}

rectangles[r1] = 100  # use 'r1' as a key
print(rectangles)  # {Rectangle(length=10, width=20): 100}
print(rectangles[r2])  # 100, since hashes are the same

rectangles[r2] = 200  # this overwrites value under 'r1' key
print(rectangles[r2])  # 200
print(rectangles)  # {Rectangle(length=10, width=20): 200}
