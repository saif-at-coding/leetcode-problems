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
