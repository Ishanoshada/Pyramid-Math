import numpy as np

def calculate_apothem(base_length, height):
    """Calculate the apothem using the Pythagorean theorem."""
    half_base = base_length / 2
    return np.sqrt(height**2 + half_base**2)

def calculate_edge(base_length, height):
    """Calculate the edge of the pyramid (peak to base corner)."""
    return calculate_apothem(base_length, height)

def calculate_slope_angle(base_length, height):
    """Calculate the slope angle of the pyramid in degrees."""
    half_base = base_length / 2
    return np.degrees(np.arctan(height / half_base))

def calculate_diagonal(base_length):
    """Calculate the diagonal length of the pyramid's base."""
    return np.sqrt(2 * base_length**2)
