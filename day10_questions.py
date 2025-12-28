"""
Create a class (2-D vector) and use it to create another class representing a 3-D 
vector. 
"""
class Vector2D:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def display(self):
        print(f"Vector2D({self.x}, {self.y})")

class Vector3D(Vector2D):
    def __init__ (self, x, y, z):
        super().__init__(x, y) # Call the constructor of Vector2D..super() deals with parent class initialization
        self.z = z
    def display(self):
        print(f"Vector3D({self.x}, {self.y}, {self.z})")    

v2d = Vector2D(4, 5)
v2d.display()
v3d = Vector3D(4, 5, 6)
v3d.display()

"""
Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
"""
class Animals:
    def __init__(self, species):
        self.species = species
class Pets(Animals):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

class Dog(Pets):
    def __init__(self, species, name, breed):
        super().__init__(species, name)
        self.breed = breed
    def bark(self):
        print("Woof!")
dog = Dog("Canine", "Buddy", "Golden Retriever")
print(f"Species: {dog.species}, Name: {dog.name}, Breed: {dog.breed}")
dog.bark()

"""
Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them. 
"""
class VectorND:
    def __init__(self, components):
        self.components = components  # components is a list of numbers

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add.")
        return VectorND([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def display(self):
        print(f"VectorND({self.components})")

v1 = VectorND([1, 2, 3])
v2 = VectorND([4, 5, 6])
v3 = v1 + v2
v3.display()  # Output: VectorND([5, 7, 9])
dot_product = v1 * v2
print(f"Dot product: {dot_product}")  # Output: Dot product: 32

"""
 Write __str__() method to print the vector as follows: 
7i + 8j +10k  
Assume vector of dimension 3 for this problem. 
"""
class Vector3DStr:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v = Vector3DStr(7, 8, 10)
print(v)  # Output: 7i + 8j + 10k

