import pytest
import sys
import os
## instead of using relative import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.subsets.first_attempt import Solution as first
from solutions.subsets.iteration import Solution as iteration
from solutions.subsets.recursion import Solution as recursion

@pytest.mark.parametrize("lst, expected",
    [
        ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ([0], [[],[0]])  
    ]
    )

class TestClass:
    def test_subsets_first(self, lst, expected):
        assert sorted(first().subsets(lst)) == sorted(expected)

    def test_subsets_iteration(self, lst, expected):
        assert sorted(iteration().subsets(lst)) == sorted(expected)

    def test_subsets_recursion(self, lst, expected):
        assert sorted(recursion().subsets(lst)) == sorted(expected)