"""
Unit tests for the calculator library
"""


import calculator


class TestCalculator:
    def test_addition(self) -> None:
        assert 4 == calculator.add(2, 2)

    def test_subraction(self) -> None:
        assert 3 == calculator.subtract(5, 2)

    def test_nuliplication(self) -> None:
        assert calculator.multiply(10, 10) == 100

    """ Testing possible use case and edge cases a join funcion"""

    def test_join_case1(self) -> None:
        assert calculator.joiner([1, 2, 3], ",") == "1,2,3"

    def test_join_use_case2(self) -> None:
        assert calculator.joiner([], ",") == ""

    def test_join_edge_case(self) -> None:
        assert calculator.joiner([1, 2, 3], "") == "123"

    def test_join_edge_case2(self) -> None:
        assert calculator.joiner([1], ",") == "1"
