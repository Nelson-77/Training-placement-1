class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Clean Version by cityhand :)
        
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        json_list = {}

        for idx, num in enumerate(nums, start=0):

            if num in json_list and abs(json_list[num] - idx)  <= k:
                return True
            else:
                json_list[num] = idx
            
        return False
