import numpy as np

def random_state():
    x = np.random.uniform(-5, 5)
    y = np.random.uniform(-5, 5)
    vx = np.random.uniform(-1, 1)
    vy = np.random.uniform(-1, 1)
    return np.array([x, y, vx, vy])

def is_inside_box(position, rectangle):
    """
    Checks if a given position is inside the specified rectangle.

    :param position: A tuple or list containing the x and y coordinates of the position to check.
    :param rectangle: A matplotlib rectangle object.
    :return: True if the position is inside the rectangle, False otherwise.
    """
    x, y = position
    rect_x, rect_y = rectangle.get_xy()  # Lower left corner of the rectangle
    rect_width, rect_height = rectangle.get_width(), rectangle.get_height()

    # Check if the position is within the bounds of the rectangle
    if rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height:
        return True
    else:
        return False
