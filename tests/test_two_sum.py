import pytest
import sys
import os
## instead of using relative import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.two_sum.bruteforce import Solution as bruteforceSolution
from solutions.two_sum.optimal import Solution as optimalSolution

@pytest.mark.parametrize("nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),  # Basic test
        ([3, 2, 4], 6, [1, 2]),       # Edge case with duplicate values
        ([3, 3], 6, [0, 1]),          # Minimal input size
        ([], 0, []),                  # Empty array
        ([1, 2, 3], 7, []),           # No solution case
    ]
    )

class TestClass:
    def test_two_sum_optimal(self, nums, target, expected):
        assert sorted(optimalSolution().twoSum(nums, target)) == sorted(expected)

    def test_two_sum_bruteforce(self, nums, target, expected):
        assert sorted(bruteforceSolution().twoSum(nums, target)) == sorted(expected)