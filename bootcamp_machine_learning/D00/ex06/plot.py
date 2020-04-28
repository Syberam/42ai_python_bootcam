#! /usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt


def are_good_args(x, y, theta):
    if not isinstance(x, np.ndarray) or len(x.shape) != 1:
        return False
    if not isinstance(y, np.ndarray) or len(y.shape) != 1:
        return False
    if x.shape != y.shape:
        return False
    if not isinstance(theta, np.ndarray) or theta.shape[0] != 2:
        return False
    return True


def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty
    numpy.ndarray.
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
    x = np.array([[1, xi] for xi in x], dtype=float)
    return np.dot(x, theta)


def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    if not are_good_args(x, y, theta):
        return
    plt.plot(x, y, 'bo', x, predict_(x, theta), 'r-')
    plt.show()


if __name__ == '__main__':
    x = np.arange(1, 6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    # Example 1:
    theta1 = np.array([4.5, -0.2])
    plot(x, y, theta1)
    # Example 2:
    theta2 = np.array([-1.5, 2])
    plot(x, y, theta2)
    # Example 3:
    theta3 = np.array([3, 0.3])
    plot(x, y, theta3)
