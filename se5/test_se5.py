import sys
import os
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se5
import util
from tree import Tree

MODULE = "se5"

# # #
#
# HELPER FUNCTIONS
#
# # #

def check_none(actual, recreate_msg=None):
    msg = "The method returned None."
    msg += " Did you forget a return statement?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_expected_none(actual, recreate_msg=None):
    msg = "The method is expected to return None."
    msg += " Your method returns: {}".format(actual)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg

def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The method returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_attribute(actual, attribute_name, recreate_msg=None):
    msg = "Your class should have a '{}' attribute.".format(attribute_name)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert hasattr(actual, attribute_name), msg

def check_attribute_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "Your class has an attribute of the wrong type.\n"
    msg += "  Expected type: {}.\n".format(expected_type.__name__)
    msg += "  Actual type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_equals(actual, expected, recreate_msg=None):
    msg = ("Actual ({}) and expected ({}) values " 
        "do not match.").format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg

def check_float_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert abs(actual-expected) < 0.01, msg

def check_parameter_unmodified(actual, expected, param, recreate_msg=None):
    msg = ("Parameter {} has been modified:\n"
        "Actual ({}) and original ({}) values of {}" 
        "do not match.").format(param, param, actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg

def pretty_print_repr(x):
    return repr(x)

def gen_recreate_msg(module, function, *params, **kwparams):
    params_str = ", ".join([pretty_print_repr(p) for p in params])
    if len(kwparams) > 0:
        params_str += ", ".join(["{} = {}".format(k, repr(v)) 
            for k, v in kwparams.items()])
    lines = ["{}.{}({})".format(module, function, params_str)]
    return gen_recreate_msg_by_lines(lines)

def gen_recreate_msg_with_trees(module, function, tree_name, *params):
    params_str = "".join([", " + pretty_print_repr(p) for p in params])
    lines = ['import util',
             'trees = util.load_trees("sample_trees.json")',
             '{}.{}(trees["{}"]{})'.format(
                 module, function, tree_name, params_str)]
    return gen_recreate_msg_by_lines(lines)

def gen_recreate_msg_by_lines(lines):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  " + "\n  ".join(lines)
    return recreate_msg

def check_tree_equals(t, expected_t, recreate_msg):
    check_tree_helper(t, expected_t, 
        "Actual and expected values do not match:", recreate_msg)

def check_tree_unmodified(t, expected_t, recreate_msg):
    check_tree_helper(t, expected_t, "Tree has been modified:", recreate_msg)

def check_tree_helper(t, expected_t, top_msg, recreate_msg):
    expected_attributes = vars(expected_t)

    node_error_prefix = "Checking a node with " + ", ".join(
        ["{}={}".format(attr, repr(getattr(t, attr, "[not assigned]")))
        for attr in expected_attributes if attr != 'children']) + \
        "\n{}\n".format(top_msg)

    for attr in expected_attributes:
        assert hasattr(t, attr), \
            node_error_prefix + \
            "Node is missing attribute {}.\n".format(attr) + \
            recreate_msg

        if attr != 'children':
            assert getattr(t, attr) == getattr(expected_t, attr), \
            node_error_prefix + ("Node has incorrect {}. "
                "Got {}, expected {}.\n").format(attr,
                repr(getattr(t, attr)), repr(getattr(expected_t, attr))) + \
                recreate_msg
    
    expected_attributes_set = set(expected_attributes.keys())
    actual_attributes_set = set(vars(t).keys())
    assert actual_attributes_set == expected_attributes_set, \
            node_error_prefix + \
            "Node has extra attributes {}.\n".format(
                ", ".join(actual_attributes_set - expected_attributes_set)) + \
            recreate_msg


    children = list(t.children)
    expected_children = list(expected_t.children)

    if expected_children == []:
        assert children == [], node_error_prefix + \
            "Expected node to have no children, but it has children.\n" + \
            recreate_msg
    else:
        for c in children:
            assert isinstance(c, Tree), node_error_prefix + \
                "Node has a child that is not a Tree: {}\n".format(c) + \
                recreate_msg

        # This assumes no node has two children with the same key
        sorted_children = sorted(children, key=lambda st: st.key)
        sorted_expected_children = sorted(
            expected_children, key=lambda st: st.key)
        keys = [c.key for c in sorted_children]
        expected_keys = [c.key for c in sorted_expected_children]


        assert keys == expected_keys, node_error_prefix + \
            "Expected node to have children with keys {} " \
            "but the children's keys are {}.\n".format(expected_keys, keys) + \
            recreate_msg

        for child, expected_child in zip(sorted_children,
                                         sorted_expected_children):
            check_tree_helper(child, expected_child, top_msg, recreate_msg)

# # #
#
# TEST HELPERS
#
# # #

def do_test_sum_of_powers(p, N, expected):
    recreate_msg = gen_recreate_msg(MODULE, "sum_of_powers", (p, N))
    actual = se5.sum_of_powers(p, N)
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_value_of(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "value_of", lst)
    actual = se5.value_of(lst)
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_index_of(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "index_of", lst)
    actual = se5.index_of(lst)
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_min_depth_leaf(trees_and_original_trees, tree_name, expected):
    trees, original_trees = trees_and_original_trees
    recreate_msg = gen_recreate_msg_with_trees(
        MODULE, 'min_depth_leaf', tree_name)
    actual = se5.min_depth_leaf(trees[tree_name])
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_tree_unmodified(trees[tree_name], original_trees[tree_name], 
                          recreate_msg)

def do_test_increasing_values(tree, test_num, expected):
    recreate_msg = "See test_se5.py, increasing_values test {} for tree".format(test_num)
    actual = se5.increasing_values(tree)
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_min_depth_leaf(tree, test_num, expected):
    recreate_msg = "See test_se5.py, min_depth_leaf test {} for tree".format(test_num)
    actual = se5.min_depth_leaf(tree)
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

# # #
#
# TESTS
#
# # #

# SUM OF POWERS
def calculate_solution(p, N):
    sum = 0
    for i in range(N+1):
        sum += p**i
    return sum

def test_sum_of_powers_1():
    p = 2
    N = 2
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_2():
    p = 1
    N = 2
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_3():
    p = 2
    N = 1
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_4():
    p = 2
    N = 3
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_5():
    p = 2
    N = 5
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_6():
    p = 2
    N = 7
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_7():
    p = 4
    N = 3
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

def test_sum_of_powers_8():
    p = 6
    N = 3
    do_test_sum_of_powers(p, N, calculate_solution(p, N))

# VALUE OF FIRST NEGATIVE
def test_value_of_1():
    lst = [-1]
    do_test_value_of(lst, -1)

def test_value_of_2():
    lst = [-1, 2, 3, 4]
    do_test_value_of(lst, -1)

def test_value_of_3():
    lst = [1, -2, 3, 4]
    do_test_value_of(lst, -2)

def test_value_of_4():
    lst = [1, 2, 3, -4]
    do_test_value_of(lst, -4)

def test_value_of_5():
    lst = [-1, 2, 3, -4]
    do_test_value_of(lst, -1)

def test_value_of_6():
    lst = [1, -2, 3, -4]
    do_test_value_of(lst, -2)

def test_value_of_7():
    lst = [-1, -2, -3, -4]
    do_test_value_of(lst, -1)

def test_value_of_8():
    lst = [1, 2, 3, 4]
    do_test_value_of(lst, 0)

def test_value_of_9():
    lst = [1]
    do_test_value_of(lst, 0)

def test_value_of_10():
    lst = []
    do_test_value_of(lst, 0)

# INDEX OF FIRST NEGATIVE
def test_index_of_1():
    lst = [-1]
    do_test_index_of(lst, 0)

def test_index_of_2():
    lst = [-1, 2, 3, 4]
    do_test_index_of(lst, 0)

def test_index_of_3():
    lst = [1, -2, 3, 4]
    do_test_index_of(lst, 1)

def test_index_of_4():
    lst = [1, 2, 3, -4]
    do_test_index_of(lst, 3)

def test_index_of_5():
    lst = [-1, 2, 3, -4]
    do_test_index_of(lst, 0)

def test_index_of_6():
    lst = [1, -2, 3, -4]
    do_test_index_of(lst, 1)

def test_index_of_7():
    lst = [-1, -2, -3, -4]
    do_test_index_of(lst, 0)

def test_index_of_8():
    lst = [1, 2, 3, 4]
    do_test_index_of(lst, -1)

def test_index_of_9():
    lst = [1]
    do_test_index_of(lst, -1)

def test_index_of_10():
    lst = []
    do_test_index_of(lst, -1)

# MIN DEPTH OF A LEAF
# Test 1:
def test_min_depth_leaf_1():
    a = Tree('A', 10)
    b = Tree('B', 20)
    tree = a
    a.add_child(b)
    do_test_min_depth_leaf(tree, "1", 1)

# Test 2:
def test_min_depth_leaf_2():
    a = Tree('A', 10)
    b = Tree('B', 20)
    c = Tree('C', 70)
    tree = a
    a.add_child(b)
    a.add_child(c)
    do_test_min_depth_leaf(tree, "2", 1)

# Test 3:
def test_min_depth_leaf_3():
    c = Tree('C', 70)
    f = Tree('F', 80)
    g = Tree('G', 120)
    tree = c
    c.add_child(f)
    f.add_child(g)
    do_test_min_depth_leaf(tree, "3", 2)

# Test 4:
def test_min_depth_leaf_4():
    c = Tree('C', 70)
    f = Tree('F', 80)
    g = Tree('G', 120)
    j = Tree('J', 90)
    tree = c
    c.add_child(f)
    f.add_child(g)
    f.add_child(j)
    do_test_min_depth_leaf(tree, "4", 2)

# Test 5:
def test_min_depth_leaf_5():
    c = Tree('C', 70)
    g = Tree('G', 120)
    h = Tree('H', 40)
    f = Tree('F', 80)
    k = Tree('K', 100)
    tree = c
    c.add_child(f)
    c.add_child(k)
    f.add_child(g)
    f.add_child(h)
    do_test_min_depth_leaf(tree, "5", 1)

# Test 6:
def test_min_depth_leaf_6():
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    k = Tree('K', 100)
    l = Tree('L', 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    do_test_min_depth_leaf(tree, "6", 2)

# Test 7:
def test_min_depth_leaf_7():
    a = Tree('A', 10)
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    k = Tree('K', 100)
    l = Tree('L', 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    g.add_child(a)
    do_test_min_depth_leaf(tree, "7", 2)

# Test 8:
def test_min_depth_leaf_8():
    a = Tree('A', 10)
    b = Tree('B', 70)
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    k = Tree('K', 100)
    l = Tree('L', 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    c.add_child(b)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    g.add_child(a)
    do_test_min_depth_leaf(tree, "8", 1)

# Test 9:
def test_min_depth_leaf_9():
    a = Tree('A', 10)
    b = Tree('B', 70)
    c = Tree('C', 70)
    f = Tree('F', 80)
    tree = c
    c.add_child(f)
    f.add_child(a)
    a.add_child(b)
    do_test_min_depth_leaf(tree, "9", 3)

# Test 10:
def test_min_depth_leaf_10():
    a = Tree('A', 10)
    b = Tree('B', 70)
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    tree = c
    c.add_child(f)
    f.add_child(a)
    f.add_child(g)
    a.add_child(b)
    do_test_min_depth_leaf(tree, "10", 2)

# INCREASING VALUES
# Test 1:
def test_increasing_values_1():
    a = Tree('A', 10)
    tree = a
    do_test_increasing_values(tree, "1", True)

# Test 2:
def test_increasing_values_2():
    a = Tree('A', 10)
    b = Tree('B', 20)
    tree = a
    a.add_child(b)
    do_test_increasing_values(tree, "2", True)

# Test 3:
def test_increasing_values_3():
    a = Tree('A', 10)
    b = Tree('B', 20)
    c = Tree('C', 70)
    tree = a
    a.add_child(b)
    a.add_child(c)
    do_test_increasing_values(tree, "3", True)

# Test 4:
def test_increasing_values_4():
    b = Tree('B', 20)
    c = Tree('C', 70)
    f = Tree('F', 80)
    tree = f
    f.add_child(b)
    f.add_child(c)
    do_test_increasing_values(tree, "4", False)

# Test 5:
def test_increasing_values_5():
    c = Tree('C', 70)
    f = Tree('F', 80)
    g = Tree('G', 120)
    tree = f
    f.add_child(g)
    f.add_child(c)
    do_test_increasing_values(tree, "5", False)

# Test 6:
def test_increasing_values_6():
    c = Tree('C', 70)
    f = Tree('F', 80)
    g = Tree('G', 120)
    tree = f
    f.add_child(c)
    f.add_child(g)
    do_test_increasing_values(tree, "6", False)

# Test 7:
def test_increasing_values_7():
    c = Tree('C', 70)
    f = Tree('F', 80)
    tree = f
    f.add_child(c)
    do_test_increasing_values(tree, "7", False)

# Test 8:
def test_increasing_values_8():
    c = Tree('C', 70)
    f = Tree('F', 80)
    g = Tree('G', 120)
    tree = c
    c.add_child(f)
    f.add_child(g)
    do_test_increasing_values(tree, "8", True)

# Test 9:
def test_increasing_values_9():
    c = Tree('C', 70)
    f = Tree('F', 80)
    g = Tree('G', 120)
    j = Tree('J', 90)
    tree = c
    c.add_child(f)
    f.add_child(g)
    f.add_child(j)
    do_test_increasing_values(tree, "9", True)

# Test 10:
def test_increasing_values_10():
    c = Tree('C', 70)
    g = Tree('G', 120)
    h = Tree('H', 40)
    f = Tree('F', 80)
    tree = c
    c.add_child(c)
    f.add_child(g)
    f.add_child(h)    
    do_test_increasing_values(tree, "10", False)

# Test 11:
def test_increasing_values_11():
    c = Tree('C', 70)
    g = Tree('G', 120)
    h = Tree('H', 40)
    f = Tree('F', 80)
    k = Tree('K', 100)
    tree = c
    c.add_child(c)
    c.add_child(k)
    f.add_child(g)
    f.add_child(h)
    do_test_increasing_values(tree, "11", False)

# Test 12:
def test_increasing_values_12():
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    k = Tree('K', 100)
    l = Tree('L', 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    f.add_child(g)
    f.add_child(l)
    do_test_increasing_values(tree, "12", True)

# Test 13:
def test_increasing_values_13():
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    k = Tree('K', 100)
    l = Tree('L', 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    do_test_increasing_values(tree, "13", True)

# Test 14:
def test_increasing_values_14():
    a = Tree('A', 10)
    c = Tree('C', 70)
    g = Tree('G', 120)
    f = Tree('F', 80)
    k = Tree('K', 100)
    l = Tree('L', 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(a)
    f.add_child(g)
    f.add_child(l)
    do_test_increasing_values(tree, "14", False)