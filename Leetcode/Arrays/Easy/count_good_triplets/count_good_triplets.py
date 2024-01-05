class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total = 0
        results = []
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    a_sum = max((arr[i] - arr[j]), -(arr[i] - arr[j]))
                    b_sum = max((arr[j] - arr[k]), -(arr[j] - arr[k]))
                    c_sum = max((arr[i] - arr[k]), -(arr[i] - arr[k]))
                    if (a_sum <= a) and (b_sum <=b) and (c_sum <= c):
                        total+=1
        return total