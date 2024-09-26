import math
import sys

import pytest

from app_sandbox.app import Vector


class TestVector:
    def test_add(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert Vector(4, 6) == v1 + v2

    def test_mul_by_scalar(self):
        v1 = Vector(1, 2)
        assert Vector(2, 4) == v1 * 2

    def test_abs(self):
        assert 0 == abs(Vector(0, 0))
        assert 1 == abs(Vector(1, 0))
        assert math.hypot(2, 3) == abs(Vector(2, 3))

    def test_equals_same_class(self):
        assert Vector(3, 4) == Vector(3, 4)
        assert Vector(3, 4) != Vector(2, 4)

    def test_equals_different_classes(self):
        assert Vector(3, 4) != "hello"
        assert Vector(3, 4) != 133

    def test_hash(self):
        assert hash(Vector(3, 4)) != 0

    def test_hash_same_for_equals_vectors(self):
        assert hash(Vector(2, 3)) == hash(Vector(2, 3))

    def test_bool(self):
        assert Vector(1, 2)
        assert Vector(1, 0)
        assert Vector(0, 2)
        assert not Vector(0, 0)

    def test_repr(self):
        assert Vector(1, 3).__repr__() == "Vector(1, 3)"
        assert Vector().__repr__() == "Vector(0, 0)"


if __name__ == "__main__":
    sys.exit(pytest.main())
