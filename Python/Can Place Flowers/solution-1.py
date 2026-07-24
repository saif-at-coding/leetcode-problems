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
