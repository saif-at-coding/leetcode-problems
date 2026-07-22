# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thought was to loop through each of the words seperately. I got that wrong first.

# Approach
<!-- Describe your approach to solving the problem. -->
I initially thought of looping through each of the words seperately. But I got the indexes wrong, especially when using the negative indexing. Then I saw the Hint (LeetCode) and decided to make 2 pointers (i1, i2) and thus, my code worked!

# Complexity
- Time complexity: O(m+n)^2
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i1, i2 = len(word1), len(word2)
        i = 0

        if i1 > i2:
            for _ in range(i2):
                merged += word1[i]
                merged += word2[i]
                i += 1
            for _ in range(i1 - i2):
                merged += word1[i]
                i += 1
        elif i2 > i1:
            for _ in range(i1):
                merged += word1[i]
                merged += word2[i]
                i += 1
            for _ in range(i2 - i1):
                merged += word2[i]
                i += 1
        else:
            for _ in range(i1):
                merged += word1[i]
                merged += word2[i]
                i += 1
        return merged
```
