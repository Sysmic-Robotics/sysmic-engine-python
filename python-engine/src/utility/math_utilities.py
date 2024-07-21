import math

def normalize_2d_vector(vector) -> tuple[float, float]:
    """
    Normalizes a 2D tuple.

    Parameters:
    vector (tuple): A tuple representing a 2D vector (x, y).

    Returns:
    tuple: A normalized 2D vector (x', y').
    """
    x, y = vector
    magnitude = math.sqrt(x**2 + y**2)
    
    if magnitude == 0:
        return (0,0)
    
    return (x / magnitude, y / magnitude)

def rotate_2d_vector(vector : tuple[float, float], angle : float)-> tuple[float, float]:
    """
    Rotates a 2D vector by a given angle.
    Parameters:
    vector (tuple): A tuple representing a 2D vector (x, y).
    angle (float): The rotation angle in radians.
    Returns:
    tuple: The rotated 2D vector (x', y').
    """
    x, y = vector
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x_new = cos_theta * x - sin_theta * y
    y_new = sin_theta * x + cos_theta * y
    return (x_new, y_new)