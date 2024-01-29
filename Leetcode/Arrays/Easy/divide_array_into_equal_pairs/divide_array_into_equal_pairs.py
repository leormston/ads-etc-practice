class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if str(i) in dic:
                count = dic[str(i)]
                count +=1
                dic[str(i)] = count
            else:
                dic[str(i)] = 1
        for k, v in dic.items():
            if v % 2 != 0:
                return False
        return True