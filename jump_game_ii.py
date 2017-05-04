class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        m = [length for _ in xrange(length)]
        m[0] = 0
        for i in xrange(length):
            if i - 1 >= 0 and nums[i - 1] > nums[i]:
                continue
            for j in xrange(i + 1, min(i + 1 + nums[i], length)):
                m[j] = min(m[i] + 1, m[j])
        
        return m[-1]
        
