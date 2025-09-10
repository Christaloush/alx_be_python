# polymorphism_demo.py

import math

class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """Calculate the area of the shape.
        
        This method should be overridden by derived classes.
        Raises:
            NotImplementedError: If not overridden by subclass
        """
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    """Derived class for rectangles."""
    
    def __init__(self, length, width):
        """Initialize rectangle attributes.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class for circles."""
    
    def __init__(self, radius):
        """Initialize circle attributes.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)