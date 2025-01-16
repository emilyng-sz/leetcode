import pytest
import sys
import os
## instead of using relative import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.find_index_of_first_occurrence_in_string.first_attempt import Solution

@pytest.mark.parametrize("haystack, needle, expected",
    [
        ("sadbutsad","sad", 0),  
        ("leetcode", "leeto", -1),   
        # edge cases 
        ("ksewaejnflwknfwil", "s", 1), 
        ("dfd", "asjdhaosd", -1)
    ]
    )

class TestClass:
    def test_substring(self, haystack, needle, expected):
        assert Solution().substring(haystack, needle) == expected

    def test_bruteforce(self, haystack, needle, expected):
        assert Solution().bruteforce(haystack, needle) == expected