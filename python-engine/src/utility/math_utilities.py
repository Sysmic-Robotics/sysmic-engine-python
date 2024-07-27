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

def dot_product_2d(vector1 : tuple[float, float], vector2 : tuple[float, float]) -> float:
    """
    Calculate the dot product of two 2D vectors represented as tuples.

    Parameters:
    vector1 (tuple): First 2D vector (x1, y1).
    vector2 (tuple): Second 2D vector (x2, y2).

    Returns:
    float: Dot product of the two vectors.
    """

    # Calculate dot product
    dot_product_result = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    return dot_product_result
    
def euclidian_distance(point_a : tuple[float, float], point_b : tuple[float, float]) -> float:
    return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)