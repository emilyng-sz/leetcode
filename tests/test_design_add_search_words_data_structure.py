import pytest
import sys
import os
## instead of using relative import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.design_add_search_words_data_structure.first_attempt import WordDictionary

#Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"], 
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#Output: [null,null,null,null,false,true,true,true]

obj = WordDictionary()

@pytest.mark.parametrize("func, input, expected",
        [("addWord", "bad", None),
        ("addWord", "dad", None),
        ("addWord", "mad", None),
        ("search", "pad", False),
        ("search", "bad", True),
        ("search", ".ad", True),
        ("search","b..", True)
          ]
    )

def test_case1(func, input, expected):
    if func == "addWord":
        assert obj.addWord(input) == expected
    if func == "search":
        assert obj.search(input) == expected
    
