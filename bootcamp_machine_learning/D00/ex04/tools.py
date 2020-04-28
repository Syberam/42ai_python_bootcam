#! /usr/bin/env python
import numpy as np


def add_intercept(x):
    """Adds a column of 1's to the non-empty numpy.ndarray x.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    Returns:
    X as a numpy.ndarray, a vector of dimension m * 2.
    None if x is not a numpy.ndarray.
    None if x is a empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    if len(x.shape) == 1:
        return np.array([[1, xi] for xi in x], dtype=float)
    ones = np.ones(x.shape[0], dtype=float)
    return np.array(np.insert(x, 0, ones, axis=1), dtype=float)


if __name__ == '__main__':
    x = [6, 7]
    print(add_intercept(x))
    x = np.array([])
    print(add_intercept(x))
    # Output: None
    x = np.arange(1, 6)
    print(add_intercept(x))
    # Output:
    # array([[1., 1.],
    # [1., 2.],
    # [1., 3.],
    # [1., 4.],
    # [1., 5.]])
    # Example 2:
    y = np.arange(1, 10).reshape((3, 3))
    print(add_intercept(y))
    # Output:
    # array([[1., 1., 2., 3.],
    # [1., 4., 5., 6.],
    # [1., 7., 8., 9.]])
    y = np.arange(1, 13).reshape((3, 4))
    print(y)
    print(add_intercept(y))
    # Output:
    # array([[ 1.  1.  2.  3.  4.]
    #  [ 1.  5.  6.  7.  8.]
    #  [ 1.  9. 10. 11. 12.]])
    y = np.arange(1, 13).reshape((4, 3))
    print(y)
    print(add_intercept(y))