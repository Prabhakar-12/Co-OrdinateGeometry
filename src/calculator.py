from math import sqrt

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two points using:
    sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_midpoint(x1, y1, x2, y2):
    """
    Calculate midpoint between two points:
    ((x1 + x2)/2, (y1 + y2)/2)
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)
