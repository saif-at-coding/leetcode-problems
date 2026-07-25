# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I saw it was 23:30 and only 30 minutes were left to save my streak. I just solved it in panic.

# Approach
<!-- Describe your approach to solving the problem. -->
I just took the long route. You can see the code, you'll understand.

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
        count = 0
        for candy in candies:
            for i in range(len(candies)):
                if (candy + extraCandies) >= candies[i]:
                    count += 1
            if count == len(candies):
                bool_array.append(True)
                count = 0
            else:
                bool_array.append(False)
                count = 0
        return bool_array
```
