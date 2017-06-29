# -*- coding: utf-8 -*-

class A(object):
    def __init__(self):
        self.start = None
        self.tail = None
    
    def add(self, num):
        if self.start == None:
            self.start = num
            self.tail = num
            return True
        else:
            if num == self.tail + 1:
                self.tail = num
                return True
            else:
                return False
    
    def reset(self):
        self.start = None
        self.tail = None
    
    def __str__(self):
        if self.start == self.tail:
            return str(self.start)
        else:
            return str(self.start) + '->' + str(self.tail)

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        a = A()
        for num in nums:
            if a.add(num):
                pass
            else:
                result.append(str(a))
                a.reset()
                a.add(num)
        if a.start != None:
            result.append(str(a))
        
        return result
            
