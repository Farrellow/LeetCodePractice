class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_l = str.split(' ')
        if len(pattern) != len(str_l):
            return False
        
        d = {}
        rd = {}
        length = len(str_l)
        for i in xrange(length):
            if d.get(pattern[i]) == None and rd.get(str_l[i]) == None:
                d[pattern[i]] = str_l[i]
                rd[str_l[i]] = pattern[i]
            else:
                if d.get(pattern[i]) != str_l[i] or rd.get(str_l[i]) != pattern[i]:
                    return False
                else:
                    pass
        
        return True
        
