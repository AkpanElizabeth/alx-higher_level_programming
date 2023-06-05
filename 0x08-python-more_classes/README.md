0x08-python-more_classes

0. Simple rectangle
1. Real definition of a rectangle
2. Area and Perimeter
3. String representation
4. Eval is magic
5. Detect instance deletion
6. How many instances
7. Change representation
8. Compare rectangles
9. A square is a rectangle
10. N queens

In Python, an object is a specific instance of a class. A class is a blueprint or a template that defines the structure and behavior of objects. An object is created from a class, and it represents a specific occurrence or instance of that class.

To create an object in Python, you need to instantiate a class. Instantiation is the process of creating an object based on the defined class. Each object created from a class is independent and has its own set of attributes and methods.

Here's an example to illustrate the concept of objects and instances in Python:

python
Copy code
# Defining a class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# Creating instances (objects) of the class
car1 = Car("Toyota", "blue")
car2 = Car("Ford", "red")

# Accessing attributes and calling methods of the objects
print(car1.brand)     # Output: Toyota
print(car2.color)     # Output: red
car1.drive()          # Output: The blue Toyota is driving.
car2.drive()          # Output: The red Ford is driving.
In the example above, Car is a class that represents a car. The __init__ method is a special method called the constructor, which initializes the attributes of the object when it's created. The drive method is a behavior defined within the class.

car1 and car2 are objects (instances) of the Car class. Each object has its own set of attributes (brand and color) and can invoke methods (e.g., drive()) defined in the class.
