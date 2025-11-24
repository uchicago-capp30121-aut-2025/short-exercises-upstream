"""
Short Exericses #6
"""

import numpy as np

def find_max(x: np.ndarray) -> tuple[int,int]:
    """ 
    Find the index and corresponding value of the largest 
        value in an array.

    Args:
        x (array): a 1-dimensional NumPy array

    Returns (tuple): The largest value in x, and it's corresponding index.
    """
    
    ### Your code here ###
    return None

def clip_in_range(x: np.ndarray, lb: int, ub: int) -> np.ndarray:
    """
    Create a NumPy array with the same values as x, but with those
    values clipped so they are between the lower bound and upper
    bound. 

    Args:
        x (array): a NumPy array of integers
        lb (int): a lower bound
        ub (int): an upper bound

    Returns (array): A new NumPy array with values clipped.
    """

    ### Your code here ###
    return None

def sum_of_powers(N: int, p: int) -> int:
    """ 
    Sum the first N powers of p:
        p^0 + p^1 + p^2 + ... + p^N
    No loops!

    Args:
        p (int): the base
        N (int): the exponent to sum to

    Returns (int): The sum of the first N powers of p. 
    """

    ### Your code here ###
    return None

def create_zeros_with_border(N: int) -> np.ndarray:
    """
    Create a square array of zeros with a border of 1s.

    Args:
        N (int): the size of the array

    Returns (array): A  2-dimensional N by N NumPy array of zeros 
        with 1s around the edges. 
    """
    
    ### Your code here ###
    return None

def find_closest_value(x: np.ndarray) -> tuple[int,int]:
    """
    Find the index and corresponding value in an array that is 
        closest to the mean.  

    Examples:
    find_closest_value(np.array([1.0, 2.0, 3.0])) -> (1, 2.0)
    find_closest_value(np.array([5.0, 1.0, 8.0])) -> (0, 5.0)

    Inputs: 
        x (array): 1-dimensional NumPy array

    Returns: The index and corresponding value in x that is 
        closest to the mean. 

    """

    ### Your code here ###
    return None