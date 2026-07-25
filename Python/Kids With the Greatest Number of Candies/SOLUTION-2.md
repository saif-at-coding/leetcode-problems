# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This is my second time solving this problem.

# Approach
<!-- Describe your approach to solving the problem. -->
This time, I gave the problem the thought and time it deserved, and figured that I only needed to compare the i^th kid (candies) with max(candies)

# Complexity
- Time complexity: O(n)^2
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_array = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array
```
