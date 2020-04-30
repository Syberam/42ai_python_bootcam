#!/usr/bin/env python
import numpy as np


def add_intercept(x):
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    ones = np.ones(x.shape[0], dtype=float).reshape(-1, 1)
    return np.array(np.append(ones, x, axis=1), dtype=float)


def predict_(x, theta):
    if not isinstance(x, np.ndarray) or len(x.shape) != 1:
        return None
    if not isinstance(theta, np.ndarray) or theta.shape[0] != 2:
        return None
    x = add_intercept(x)
    return np.dot(x, theta)


def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without
    any for loop.
    ,→ The three arrays must have compatible dimensions.
    Args:
    x: has to be a numpy.ndarray, a matrix of dimension m * 1.
    y: has to be a numpy.ndarray, a vector of dimension m * 1.
    theta: has to be a numpy.ndarray, a 2 * 1 vector.
    Returns:
    The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
    None if x, y, or theta is an empty numpy.ndarray.
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
    return np.array([theta[j] - np.sum(x) for x, j
                    in zip(forumla(x, y, theta), range(2))])


def forumla(x, y, theta):
    # ∆(J) = (1 / m)X'T(X'∂-y)
    return ((1 / x.shape[0])
            * add_intercept(x).T
            * (predict_(x, theta) - y)
            )


if __name__ == '__main__':
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
    # Example 0:
    theta1 = np.array([2, 0.7])
    print(gradient(x, y, theta1))
    # Output:
    # array([21.0342574, 587.36875564])
    # Example 1:
    theta2 = np.array([1, -0.4])
    print(gradient(x, y, theta2))
    # Output:
    # array([58.86823748, 2229.72297889])