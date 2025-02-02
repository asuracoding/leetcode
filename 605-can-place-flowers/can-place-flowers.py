class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        for idx, x in enumerate(flowerbed):
            if idx>0 and idx < len(flowerbed)-1:
               if flowerbed[idx]==0 and flowerbed[idx-1]==0 and flowerbed[idx+1]==0:
                    total+=1
                    flowerbed[idx]=1
            elif idx==0 and len(flowerbed)==1 and flowerbed[idx]==0:
                total+=1
                flowerbed[idx] =1
            elif idx==0 and flowerbed[idx] ==0 and flowerbed[idx+1] ==0:
                total+=1
                flowerbed[idx] =1
            elif idx == len(flowerbed)-1 and flowerbed[idx]==0 and flowerbed[idx-1] ==0:
                total+=1
                flowerbed[idx] = 1
        return total >= n
