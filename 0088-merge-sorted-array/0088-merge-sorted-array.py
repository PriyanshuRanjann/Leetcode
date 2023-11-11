class Solution:
    import heapq
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=[]
        merged=heapq.merge(nums1,nums2)
        nums1[:]=list(merged)