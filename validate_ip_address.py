# -*- coding: utf-8 -*-

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        IPv4 = 'IPv4'
        IPv6 = 'IPv6'
        Neither = 'Neither'
        
        l = IP.split('.')
        if len(l) == 4:
            for i in l:
                if not i:
                    return Neither
                if not i.isnumeric():
                    return Neither
                if i[0] == '0':
                    if int(i) != 0:
                        return Neither
                    else:
                        if len(i) > 1:
                            return Neither
                if int(i) > 255 or int(i) < 0:
                    return Neither
            return IPv4
        else:
            l = IP.split(':')
            if len(l) == 8:
                for i in l:
                    if not i:
                        return Neither
                    if len(i) > 4:
                        return Neither
                    for c in i:
                        if (ord(c) < ord('0') or ord(c) > ord('9')) and \
                        (ord(c) < ord('a') or ord(c) > ord('f')) and \
                        (ord(c) < ord('A') or ord(c) > ord('F')):
                            return Neither
                return IPv6
            else:
                return Neither
