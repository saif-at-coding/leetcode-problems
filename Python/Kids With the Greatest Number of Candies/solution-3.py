class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_array, max_candies = [], max(candies)
        for i in range(len(candies)):
            bool_array.append((candies[i] + extraCandies) >= max_candies)
        return bool_array
