# Intuition
I thought it'd be easy. I guessed I would just check if the left and right of an empty plot is empty...
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
I was wrong. But I tried again and again and again. I don't even know how to correctly respond. But when it got accepted, finally, I really wanted to cry. See the code, maybe I'll come up with a better solution next time with good explanantion.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        for _ in range(len(flowerbed)):
            if len(flowerbed) == 1:
                if flowerbed[i] == 0:
                    count += 1
            elif i == 0:
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0:
                        count += 1
                        flowerbed[i] = 1
                i += 1
            elif i == (len(flowerbed) - 1):
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0:
                        count += 1
                        flowerbed[i] = 1
            else:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0:
                        if flowerbed[i+1] == 0:
                            count += 1
                            flowerbed[i] = 1
                i += 1

        if count >= n:
            return True
        else:
            return False
```
