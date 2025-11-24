import sys
import os
import math

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se6
import numpy as np

MODULE = "se6"

# # #
#
# HELPER FUNCTIONS
#
# # #

def pretty_print_repr(x):
    """
    A version of repr with some special casing.
    """
    if isinstance(x, np.ndarray):
        return "np." + repr(x)
    return repr(x)

def gen_recreate_msg(module, function, *params, **kwparams):


        
    params_str = ", ".join([pretty_print_repr(p) for p in params])
    if len(kwparams) > 0:
        params_str += ", ".join(["{} = {}".format(k, repr(v)) for k, v in kwparams.items()])


    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg


def check_none(actual, recreate_msg=None):
    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_equals(actual, expected, recreate_msg=None):
    msg = ("Actual ({}) and expected ({}) values " 
        "do not match.").format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg

def check_dtype(array, expected, recreate_msg=None):
    actual_dtype = array.dtype
    expected_dtype = expected

    msg = "The function returned an array of the wrong dtype.\n"
    msg += "  Expected return dtype: {}.\n".format(expected_dtype)
    msg += "  Actual return dtype: {}.".format(actual_dtype)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual_dtype == expected_dtype, msg

def check_array_equal(actual, expected, recreate_msg):
    msg = "The function returned the wrong array"
    msg += " Expected array: {}\n".format(expected)
    msg += " Actual returned array: {}\n".format(actual)

    if recreate_msg is not None:
        msg += "\n" + recreate_msg
    
    np.testing.assert_allclose(actual, expected,
                               err_msg = msg, verbose=False)
    
    
# # #
#
# TEST HELPERS
#
# # #

def do_test_find_max(x):

    def expected_find_max(x):
        max_index = None
        max_val = -100
        
        x = list(x)
        for index, val in enumerate(x):
            if val > max_val:
                max_val = val
                max_index = index

        return max_val, max_index

    recreate_msg = gen_recreate_msg(MODULE, "find_max", x)

    actual = se6.find_max(x)
    expected = expected_find_max(x)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_clip_in_range(x, lb, ub):

    def expected_clip_in_range(x, lb, ub):

        x = list(x)
        clipped = []

        for i in range(len(x)):
            if x[i] < lb:
                clipped.append(lb)
            elif x[i] > ub:
                clipped.append(ub)
            else:
                clipped.append(x[i])

        return np.array(clipped)

    recreate_msg = gen_recreate_msg(MODULE, "clip_in_range", (x, lb, ub))
    
    actual = se6.clip_in_range(x, lb, ub)
    expected = expected_clip_in_range(x, lb, ub)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_array_equal(actual, expected, recreate_msg)

    
def test_sum_of_powers():

    for p in [1, 2, 4]:
        for N in [1, 2, 5, 10]:
            recreate_msg = gen_recreate_msg(MODULE, 'sum_of_powers', N, p)
            actual = int(se6.sum_of_powers(N, p))
            expected = int(sum([p**i for i in range(N+1)]))

            check_none(actual, recreate_msg)
            check_equals(actual, expected, recreate_msg)


def do_test_create_zeros_with_border(N):

    def expected_create_zeros_with_border(N):

        x = []

        first_and_last = [1] * N
        x.append(first_and_last)

        middle = []
        middle.append(1)
        for _ in range(N-2):
            middle.append(0)
        middle.append(1)

        for _ in range(N-2):
            x.append(middle)

        x.append(first_and_last)

        return np.array(x)

    recreate_msg = gen_recreate_msg(MODULE, 'create_zeros_with_border', N)

    actual = se6.create_zeros_with_border(N)
    expected = expected_create_zeros_with_border(N)

    check_none(actual, recreate_msg)
    check_array_equal(actual, expected, recreate_msg)


def do_test_find_closest_value(x):

    def expected_closest_value(x):
        closest_delta = 1e9
        
        closest_idx = None
        closest_val = None
        
        for i, x_item in enumerate(x):
            delta = abs(x_item - np.mean(x))

            if delta < closest_delta:
                closest_delta = delta
                closest_idx = i
                closest_val = x_item
        
        return closest_idx, closest_val
        
    recreate_msg = gen_recreate_msg(MODULE, 'find_closest_value', x)

    actual = se6.find_closest_value(x)
    expected = expected_closest_value(x)

    check_none(actual, recreate_msg)
    check_equals(actual, expected, recreate_msg)

# # #
#
# TESTS
#
# # #

def test_find_max_1():
    x = np.array([7.2, 0.1, 2.1, 4.2, 5.5, 3.7, 2.8])
    do_test_find_max(x)

def test_find_max_2():
    x = np.array([0.1, 2.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    do_test_find_max(x)

def test_find_max_3():
    x = np.array([0.1, 8.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    do_test_find_max(x)

def test_find_max_4():
    x = np.array([0.1, 2.1, 4.2, 5.5, 7.7, 2.8, 5.7])
    do_test_find_max(x)

def test_find_max_5():
    x = np.array([0.1, 2.1, 7.8, 5.5, 7.7, 2.8, 5.7])
    do_test_find_max(x)

def test_clip_in_range_1():
    x = np.array([0.1, 2.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    lb, ub = 0, 10
    do_test_clip_in_range(x, lb, ub)

def test_clip_in_range_2():
    x = np.array([0.1, 2.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    lb, ub = 2, 5
    do_test_clip_in_range(x, lb, ub)

def test_clip_in_range_3():
    x = np.array([0.1, 2.1, 4.2, 8.5, -2.5, 2.8, 5.7])
    lb, ub = 2, 4
    do_test_clip_in_range(x, lb, ub)

def test_clip_in_range_4():
    x = np.array([0.1, 2.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    lb, ub = -1, 0
    do_test_clip_in_range(x, lb, ub)

def test_clip_in_range_5():
    x = np.array([0.1, 2.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    lb, ub = 6, 7
    do_test_clip_in_range(x, lb, ub)

def test_clip_in_range_6():
    x = np.array([0.1, 2.1, 4.2, 5.5, 3.7, 2.8, 5.7])
    lb, ub = 3.5, 5.6
    do_test_clip_in_range(x, lb, ub)

def test_create_zeros_with_border_1():
    do_test_create_zeros_with_border(5)

def test_create_zeros_with_border_2():
    do_test_create_zeros_with_border(6)

def test_create_zeros_with_border_3():
    do_test_create_zeros_with_border(4)

def test_create_zeros_with_border_4():
    do_test_create_zeros_with_border(10)

def test_find_closest_value_1():

    x = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
    do_test_find_closest_value(x)

def test_find_closest_value_2():

    x = np.array([1.5, 1.4, 1.3, 1.2, 1.1, 1.0])
    do_test_find_closest_value(x)

def test_find_closest_value_3():

    x = np.array([1.2, 2.7, 10.6, 12.7, 4.4, 5.8, 1.0])
    do_test_find_closest_value(x)

def test_find_closest_value_4():

    x = np.array([1.2])
    do_test_find_closest_value(x)

def test_find_closest_value_5():

    x = np.array([1.0, 2.1])
    do_test_find_closest_value(x)