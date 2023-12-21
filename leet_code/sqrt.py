class Solution:
    def mySqrt(self, x: int) -> int:
        distance=x
        i=0
        sqrt=i
        while True:
            new_distance=x-i*i
            if new_distance==0:
                return i
            elif abs(new_distance)>distance:
                return sqrt
            else:
                sqrt=i
                distance=new_distance
                i+=1

print(Solution().mySqrt(11))