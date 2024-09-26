import pytest
import sys

from app_sandbox.app import my_sum


class TestApp:
    def test_my_sum(self):
        assert 2 == my_sum(1, 1)


if __name__ == "__main__":
    sys.exit(pytest.main())
