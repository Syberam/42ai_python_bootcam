#!/usr/bin/env python
import numpy as np


def add_intercept(x):
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    if len(x.shape) == 1:
        return np.array([[1, xi] for xi in x], dtype=float)
    ones = np.ones(x.shape[0], dtype=float)
    return np.array(np.insert(x, 0, ones, axis=1), dtype=float)


def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(x, np.ndarray) or len(x.shape) != 1:
        return None
    if not isinstance(theta, np.ndarray) or theta.shape[0] != 2:
        return None
    x = add_intercept(x)
    return np.dot(x, theta)


def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without
    any for-loop.
    ,→ The three arrays must have compatible dimensions.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    11
    theta: has to be an numpy.ndarray, a 2 * 1 vector.
    Returns:
    The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
    None if x, y, or theta are empty numpy.ndarray.
    None if x, y and theta do not have compatible dimensions.
    Raises:
    This function should not raise any Exception.
    """
    if (not isinstance(x, np.ndarray)
        or not isinstance(y, np.ndarray)
            or not isinstance(theta, np.ndarray)):
        return None
    if x.shape[0] * y.shape[0] * theta.shape[0] == 0:
        return None
    if x.shape[0] != y.shape[0] or theta.shape[0] != 2:
        return None
    return forumla(x, y, theta)


def forumla(x, y, theta):
    # ∆(J) = (1 / m)X'T(X'∂-y)
    return np.sum(
        (1 / x.shape[0])
        * add_intercept(x).transpose()
        * (predict_(x, theta) - y)
    )


if __name__ == '__main__':
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
    # Example 0:
    theta1 = np.array([2, 0.7])
    print(simple_gradient(x, y, theta1))
    # Output:
    # array([21.0342574, 587.36875564])
    # Example 1:
    theta2 = np.array([1, -0.4])
    print(simple_gradient(x, y, theta2))
    # Output:
    # array([58.86823748, 2229.72297889])