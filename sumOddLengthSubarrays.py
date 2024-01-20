class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                d=arr[i:j+1]
                
                if (len(d)%2)!=0:
                    print(d)
                    ans+=sum(d)
        return ans
