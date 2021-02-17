"""
Python Class Development good practices as presented by Raymond Hettinger on PyCon 2013
https://www.youtube.com/watch?v=HTLu2DFOdTg&t=1109s
Python's standard solutions for standard problems
"""

import math
import sys
from random import random, seed
import numpy as np


class Circle(object):
    """Always document your classes. You can make documentation with Sphinx later."""

    version = "0.1"  # class variable = shared data

    # Flyweight design pattern suppresses the instance dictionary; takes less memory, works faster;
    # does not create dictionary; lost ability to add additional atributes
    # make this optimization last
    __slots__ = ["diameter"]

    # not a constructur, but an ititializer,
    # takes existing instance self and populates it, takes 'radius' and stores it in a dictionary
    def __init__(self, radius):
        self.radius = radius  # instance variable

    @property  # convert dotted access to method calls
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(
        self, radius
    ):  # in case we could not store radius anymore and only option was to calcutale radius from diameter
        self.diameter = radius * 2.0

    def area(self):
        """Perform quadrature on a shape of uniform radius"""
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        """Calculate the perimeter of a given circle"""
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    # more than one constructor for various needs
    # alternative constructor
    @classmethod
    def from_bbd(cls, bbd):
        """Construct from a bounding box diagonal"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        # alternative constructors need to anticipate subclassing.
        # 'Circle(radius) will not work for subclass Tyre'
        return cls(radius)

    @staticmethod
    def angle_to_grade(angle):
        """
        Convert angle in degree to a percentage grade
        :param angle:
        :return:
        """
        grade = math.tan(math.radians(angle)) * 100
        return grade


class Tyre(Circle):
    """Tyres use a corrected perimeter of a circle"""

    def perimeter(self):
        return Circle.perimeter(self) * 1.25


if __name__ == "__main__":
    n_circles = 10
    circles = [Circle(random()) for i in range(n_circles)]
    avg_area_circles = np.average([c.area() for c in circles])
    print(
        "The average area of {} random circles is {:.4f}".format(
            n_circles, avg_area_circles
        )
    )

    circle = Circle(1)
    print("Version: {}".format(circle.version))
    print(
        "The circle of a radius {} has an area approx. to {:.4f} and perimeter approx to {:.4f} ".format(
            circle.radius, circle.area(), circle.perimeter()
        )
    )

    tyre = Tyre(1)
    print(
        "The tyre of a radius {} has an area approx. to {:.4f} and perimeter approx to {:.4f} ".format(
            tyre.radius, tyre.area(), tyre.perimeter()
        )
    )

    bbd = 10
    tyre = Tyre.from_bbd(bbd)
    print(
        "The tyre of bounding box diagonal {} has a radius {:.4f} "
        "has an area approx. to {:.4f} and perimeter approx to {:.4f} ".format(
            bbd, tyre.radius, tyre.area(), tyre.perimeter()
        )
    )

    angle = 45
    print(
        "The grade of {} deg. angle is {:.2f}".format(
            angle, circle.angle_to_grade(angle)
        )
    )

    sys.exit()
