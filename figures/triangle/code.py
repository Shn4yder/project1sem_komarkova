a_tr, b_tr, c_tr = 7, 2, 8

__all__ = [
    'triangle_perimeter',
    'triangle_area'
]

def triangle_perimeter(first = a_tr, second = b_tr, third = c_tr):
    return first + second + third


def triangle_area(first = a_tr, second = b_tr, third = c_tr):
    p = (first + second + third) / 2
    return (p * (p - first) * (p - second) * (p - third))**(1 / 2)


