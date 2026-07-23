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
