class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        length = len(candies)
        d = {}
        kind = 0
        for candy in candies:
            if d.get(candy) == None:
                d[candy] = 1
                kind += 1
            else:
                pass
        
        return min(length // 2, kind)
        
