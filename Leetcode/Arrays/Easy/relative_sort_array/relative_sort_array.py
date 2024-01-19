class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        order = arr2
        while len(arr2) > 0:
            num = arr2.pop(0)
            while(arr1.count(num) > 0):
                arr1.remove(num)
                arr.append(num)

        arr1 = sorted(arr1)
        for i in arr1:
            arr.append(i)
        return arr