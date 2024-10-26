## Brute force method involves 2 loops O(n^2) to check if needle matches haystack
## Consider hashmap - my current solution is still O(n^2)
## In this case, it would be better to use string slicing instead of hashmap, since the time complexity is the same

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h_n = len(haystack)
        starting_chara = needle[0]
        h = {}
        haystackls = [char for char in haystack]
        for i in range(h_n-n+1):
            if haystackls[i] == starting_chara:
                h[''.join(haystackls[i:min(h_n, i+n)])] = i  ## N.B. am still concatenating strings. 
                if needle in h:
                    return h[needle]
        return -1 

if __name__ == '__main__':
    # run a test case
    hs = "sadbutsad"
    n = "sad"
    s = Solution()
    l = s.strStr(hs, n)
    print(l)