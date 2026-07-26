# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I failed 3 days back to back, and spent hours on this problem.

# Approach
<!-- Describe your approach to solving the problem. -->
But in the end, I succeeded. Because I figured it was a hidden gcd problem. And boom! Optimal solution (0 ms, beats 100%) achieved.

# Complexity
- Time complexity: O(n + m)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n + m)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        length = gcd(len(str1), len(str2))
        return str1[:length]
```
