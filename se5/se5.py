"""
Short Exercises #5
"""

from tree import Tree

def sum_of_powers(p: int, N: int) -> int:
    """ 
    Sum the first N powers of p:
        p^0 + p^1 + p^2 + ... + p^N

    Args:
        p (int): the base
        N (int): the exponent to sum to

    Returns (int): The sum of the first N powers of p. 
    """

    ### YOUR CODE HERE
    return None


def value_of(lst: list[int]) -> int:
    """
    Find the first negative value in the list of integers. 
    Return 0 if the list has no negative values. 

    Note: This is the recursive version of first_negative on SE #2. 

    Args:
        lst (list of ints): the list

    Returns (int): The first negative, or zero if there are no
        negatives in lst. 
    """

    ### YOUR CODE HERE
    return None


def index_of(lst: list[int]) -> int:
    """
    Find the index of the first negative value in a list
    of integers. Return -1 if the list has no negative values. 

    Args:
        lst (list of ints): the list

    Returns (int): The index of the first negative, or -1 if
        there are no negatives in lst. 
    """

    ### YOUR CODE HERE
    return None


def min_depth_leaf(tree : Tree) -> int:
    """
    Computes the minimum depth of a leaf in the tree (length of shortest
    path from the root to a leaf).

    Input:
        tree: a Tree instance.
    
    Returns: (integer) the minimum depth of of a leaf in the tree.
    """
    
    ### YOUR CODE HERE
    return None


def increasing_values(t : Tree) -> bool:
    """ 
    Determine whether the values in every path from the root
    to a leaf are increasing. 

    Args:
        t (Tree): the tree

    Returns (boolean): True if the values along every path are
        increasing, False otherwise. 
    """

    ### YOUR CODE HERE
    return None
