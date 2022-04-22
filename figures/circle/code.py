from math import pi


default_radius = 5

__all__ = [
        'circle_perimetr',
        'circle_area'
]

def circle_perimetr(radius=default_radius):
        return 2 * pi * radius

def circle_area(radius=default_radius):
        return pi * radius ** 2



