# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This is my third time solving this problem with Python.

# Approach
<!-- Describe your approach to solving the problem. -->
If you see my previous solutions, you'll notice that in this one, I only computed the max(candies) once, and I also tried to lower the number of lines needed. Ultimately, I also reached a 0ms runtime (beats 100%) and a better space-time complexity.

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_array, max_candies = [], max(candies)
        for i in range(len(candies)):
            bool_array.append((candies[i] + extraCandies) >= max_candies)
        return bool_array
```
