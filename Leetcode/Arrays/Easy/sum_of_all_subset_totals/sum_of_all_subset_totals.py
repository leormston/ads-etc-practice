from itertools import chain, combinations

class Solution:
    def powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

    def x_or_array(self, arr: List[int]) -> int:
        total = arr.pop(0)
        while len(arr) > 0:
            total ^= arr.pop(0)
        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        iterations = self.powerset(nums)
        for i in iterations:
            if len(i) > 0:
                total += self.x_or_array(list(i))
        return total