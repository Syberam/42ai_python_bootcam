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
    if not isinstance(x, np.ndarray):
        return None
    if not isinstance(theta, np.ndarray) or theta.shape[0] != 2:
        return None
    x = add_intercept(x)
    return np.dot(x, theta)


def gradient(x, y, theta):
    if (not isinstance(x, np.ndarray)
        or not isinstance(y, np.ndarray)
            or not isinstance(theta, np.ndarray)):
        return None
    if x.shape[0] * y.shape[0] * theta.shape[0] == 0:
        return None
    if x.shape[0] != y.shape[0] or theta.shape[0] != 2:
        return None
    rez = np.array([theta[j] - np.sum(x) for x, j
                    in zip(formula(x, y, theta), range(2))])
    return rez


def formula(x, y, theta):
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)
    return ((1 / x.shape[0])
            * add_intercept(x).T
            * (predict_(x, theta) - y.T)
            )


def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of 
    training examples, 1).
    y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of
    training examples, 1).
    theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the
    gradient descent
    Returns:
    new_theta: numpy.ndarray, a vector of dimension 2 * 1.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exception.
    """
    for it in range(max_iter):
        theta = theta - alpha * gradient(x, y, theta)
    return theta


if __name__ == '__main__':
    x = np.array(
        [[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    y = np.array(
        [[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
    theta = np.array([1, 1])
    # Example 0:
    theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=150)
    print(theta1)
    # Output:
    # array([[1.40709365],
    # [1.1150909 ]])
    # Example 1:
    predict_(x, theta1)
    # # Output:
    # array([[15.3408728 ],
    # [25.38243697],
    # [36.59126492],
    # [55.95130097],
    # [65.53471499]])
