#!/usr/bin/env python

"""
Short Exercises #5 - Tree Class
"""

import textwrap
from typing import Any

class Tree:
    """
    A class representing a (non-null) tree with a root
    node and some number of child subtrees (which will,
    themselves, be instances of Tree)

    Attributes:
        key: Key associated with the root node.
        value: Value associated with the root node.
        children: List of child subtrees.
    """

    key: Any
    value: Any
    children: list['Tree']

    def __init__(self, k: Any = None, v: Any = None) -> None:
        """
        Constructor.

        Creates either a tree with a root node and no
        child subtrees. The root node will have a key and
        value associated with it.

        Parameters
        - k, v: Key and value for the root node.
        """

        self.key = k
        self.value = v

        self.children = []

    def add_child(self, other_tree: 'Tree') -> None:
        """
        Adds an existing tree as a child of the tree.

        Parameter:
        - other_tree: Tree to add as a child subtree.
        """
        if not isinstance(other_tree, Tree):
            raise ValueError("Parameter to add_child must be a Tree object")

        self.children.append(other_tree)

    def num_children(self) -> int:
        """Returns the number of children"""
        return len(self.children)

    def __print_r(self, prefix: str, last: bool, kformat: str,
                  vformat: str, maxdepth: int | None) -> None:
        """
        Recursive helper method to print out the tree. Should not be
        called directly. See print() method for more details.
        """

        if maxdepth is not None:
            if maxdepth == 0:
                return
            else:
                maxdepth -= 1

        if len(prefix) > 0:
            if last:
                lprefix1 = prefix[:-3] + "  └──"
            else:
                lprefix1 = prefix[:-3] + "  ├──"
        else:
            lprefix1 = ""

        if len(prefix) > 0:
            lprefix2 = prefix[:-3] + "  │"
        else:
            lprefix2 = ""

        if last:
            lprefix3 = lprefix2[:-1] + "   "
        else:
            lprefix3 = lprefix2 + "  "

        ltext = (kformat + ": " + vformat).format(self.key, self.value)

        ltextlines = textwrap.wrap(ltext, 80, initial_indent=lprefix1,
                                   subsequent_indent=lprefix3)

        print(lprefix2)
        print("\n".join(ltextlines))

        for i, st in enumerate(self.children):
            if i == self.num_children() - 1:
                newprefix = prefix + "   "
                newlast = True
            else:
                newprefix = prefix + "  │"
                newlast = False

            st.__print_r(newprefix, newlast, kformat, vformat, maxdepth) # pylint: disable=protected-access

    def print(self, kformat: str = "{}", vformat: str = "{}",
              maxdepth: int | None  = None) -> None:
        """
        Prints out the tree.

        Parameters:
        - kformat, vformat: Format strings for the key and value.
        - maxdepth: Maximum depth to print.
        """

        self.__print_r("", False, kformat, vformat, maxdepth)


def tree_example() -> None:
    """Example usage of the Tree class."""
    t = Tree("ROOT", "foo")

    for i in range(5):
        st = Tree(f"CHILD {i+1}", "foo")
        t.add_child(st)

    for st in t.children:
        for i in range(2):
            sst = Tree(f"GRANDCHILD {i+1}", "foo")
            st.add_child(sst)

    t.print()


if __name__ == "__main__":
    tree_example()
