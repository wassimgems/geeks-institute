
import math

class Circle:
         def __init__(self, radius=None, diameter=None):
           if radius is not None:
               self.radius = radius
               self.diameter = radius * 2
           elif diameter is not None:
               self.diameter = diameter
               self.radius = diameter / 2
           else:
                self.radius = 0
                self.diameter = 0
         def area(self):
           area = math.pi * self.radius ** 2   
         def __str__(self):
           return f"Circle(radius={self.radius}, diameter={self.diameter})"   
         def __add__(self, other):
           return Circle(radius=self.radius + other.radius)
         def __gt__(self, other):
           return self.radius > other.radius
         def __eq__(self, other):
           return self.radius == other.radius
         def __lt__(self, other):
           return self.radius < other.radius


# Create circles
c1 = Circle(radius=3)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)
c4 = Circle(radius=3)

# Display circles
print(c1)
print(c2)

# Calculate area
print("Area:", c1.area())

# Add circles
c5 = c1 + c2
print("New circle:", c5)

# Compare circles
print(c1 > c2)
print(c1 == c4)

# Sort circles
circles = [c1, c2, c3, c4]
circles.sort()

print("Sorted circles:")
for circle in circles:
    print(circle)


