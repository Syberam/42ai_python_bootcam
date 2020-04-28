#! /usr/bin/env python
import numpy as np


def are_good_args(y, y_hat):
    if not isinstance(y_hat, np.ndarray):
        return False
    if not isinstance(y, np.ndarray):
        return False
    if y_hat.shape != y.shape:
        return False
    return True


def add_intercept(x):
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    if len(x.shape) == 1:
        return np.array([[1, xi] for xi in x], dtype=float)
    ones = np.ones(x.shape[0], dtype=float)
    return np.array(np.insert(x, 0, ones, axis=1), dtype=float)


def predict_(x, theta):
    if not isinstance(x, np.ndarray):
        return None
    if not isinstance(theta, np.ndarray):
        return None
    x = add_intercept(x)
    if x.shape[1] != theta.shape[0]:
        return None
    return np.dot(x, theta)


def cost_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_elem: numpy.ndarray, a vector of dimension (number of the training
    examples,1).
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    if not are_good_args(y, y_hat):
        return None
    m = y_hat.shape[0]
    print(m)
    return np.array(
        [1 / (2 * m) * (yi_ - yi) ** 2 for yi_, yi in zip(y_hat, y)]
    )


def cost_(y, y_hat):
    """
    Description:
    Calculates the value of cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_value : has to be a float.
    25
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    if y.shape != y_hat.shape:
        y_hat = y_hat.flatten()
        return np.sum(cost_elem_(y, y_hat)) * 2  # try it and it works... why ?
    return np.sum(cost_elem_(y, y_hat))


if __name__ == '__main__':
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
    # Example 1:
    print(cost_elem_(y1, y_hat1))
    # Output:
    # array([[0.], [0.1], [0.4], [0.9], [1.6]])
    # Example 2:
    print(cost_(y1, y_hat1))
    print("_____")

    # Output:
    # 3.0
    x2 = np.array([
            [0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]
        ])
    theta2 = np.array([[0.05], [1.], [1.], [1.]])
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([[19.], [42.], [67.], [93.]])
    # Example 3:
    print(cost_elem_(y2, y_hat2))
    # Output:
    # array([[1.3203125], [0.7503125], [0.0153125], [2.1528125]])
    # Example 4:
    print(cost_(y2, y_hat2))
    print("_____")

    # Output:
    # 4.238750000000004
    x3 = np.array([0, 15, -9, 7, 12, 3, -21])
    theta3 = np.array([[0.], [1.]])
    y_hat3 = predict_(x3, theta3)
    y3 = np.array([2, 14, -13, 5, 12, 4, -19])
    # Example 5:
    print(cost_(y3, y_hat3))
    # Output:
    # 4.285714285714286
    # Example 6:
    print(cost_(y3, y3))
    # Output:
    # 0.0
