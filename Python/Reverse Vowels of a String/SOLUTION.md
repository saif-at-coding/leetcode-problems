# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Initially, I thought that looping through the string and seperating the vowels from the whole string would be a good idea.

# Approach
<!-- Describe your approach to solving the problem. -->
My idea worked! Check out the code!

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        reverse_vowels = []
        reverse = ""
        j = -1
        for char in s:
            if char in vowels:
                reverse_vowels.append(char)
        for char in s:
            if char in vowels:
                reverse += reverse_vowels[j]
                j -= 1
            else:
                reverse += char
        return reverse
```
