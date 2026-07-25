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
