#!/usr/bin/env python


class Vector:
    def __init__(self, *args, values=None, size=None):
        if not size:
            for arg in args:
                if type(arg) is int:
                    size = arg
                    break
        if not values:
            values = []
            for arg in args:
                if type(arg) is list:
                    values = [float(v) for v in arg]
                    break
                if type(arg) is tuple:
                    values = [float(v) for v in range(*arg)]
                    break
        if not size:
            size = len(values)
        if len(values) == 0:
            values = [float(v) for v in range(size)]
        self.values = values[size:] if size < 0 else values[:size]
        self.size = len(self.values)

    def __add__(self, other):
        """add : scalars and vectors, can have errors with vectors."""
        self.rhv_lrv_compatibility(other)
        return Vector(
            [a + b for a, b in zip(self.values, other.values)],
            self.size
        )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """sub : scalars and vectors, can have errors with vectors."""
        self.rhv_lrv_compatibility(other)
        return Vector(
            [a - b for a, b in zip(self.values, other.values)],
            self.size
        )

    def __rsub__(self, other):
        """sub : scalars and vectors, can have errors with vectors."""
        self.rhv_lrv_compatibility(other)
        return Vector(
            [b - a for a, b in zip(self.values, other.values)],
            self.size
        )

    def __truediv__(self, other):
        """div : only scalars."""
        if type(other) != type(self):
            raise ValueError("need to be vector type")
        if self.size == other.size:
            return Vector(
                [a / b for a, b in zip(self.values, other.values)],
                self.size
            )
        elif other.size == 1:
            return Vector(
                [a / other.values[0] for a in self.values],
                self.size
            )
        elif self.size == 1:
            return Vector(
                [self.values[0] / b for b in other.values],
                other.size
            )
        else:
            raise ValueError("Required same dimension vectors or scalar")

    def __rtruediv__(self, other):
        if type(other) != type(self):
            raise ValueError("need to be vector type")
        if self.size == other.size:
            return Vector(
                [a / b for a, b in zip(other.values, self.values)],
                self.size
            )
        elif other.size == 1:
            return Vector(
                [other.values[0] / a for a in self.values],
                self.size
            )
        elif self.size == 1:
            return Vector(
                [b / self.values[0] for b in other.values],
                other.size
            )
        else:
            raise ValueError("Required same dimension vectors or scalar")

    def __mul__(self, other):
        """mul : scalars and vectors, can have errors with vectors,
        return a scalar if we perform Vector * Vector (dot product)"""

        pass

    def __rmul__(self, other):
        pass

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return "Matrix of size {}: {}\n________".format(self.size, self.values)

    def rhv_lrv_compatibility(self, other):
        if type(other) != type(self) or self.size != other.size:
            raise ValueError("Required same dimension vectors")
