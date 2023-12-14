class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        insert_index = 0
        while(insert_index < m + n and len(nums2) > 0):
            print(insert_index, nums2[0])
            if(nums1[insert_index] >= nums2[0]):
                nums1.insert(insert_index, nums2[0])
                nums2.pop(0)
                nums1.pop(-1)
            
            insert_index +=1

        if len(nums2) > 0:
            insert_index = m + (n - len(nums2))
            for i in nums2:
                nums1[insert_index] = i
                insert_index += 1
        
