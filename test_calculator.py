"""
Unit tests for the calculator library
"""


import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subraction(self):
        assert 3 == calculator.subtract(5, 2)

    def test_nuliplication(self):
        assert calculator.multiply(10, 10) == 100
