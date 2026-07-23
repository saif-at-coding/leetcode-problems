# Intuition
This is my second time solving this.

# Approach
This time, I looped through both words until one of them was exhausted. Then the rest of the letters will be added automatically to the merged string.

# Complexity
- Time complexity: O(m+n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        merged.extend(word1[i:])
        merged.extend(word2[i:])
        return "".join(merged)
```
