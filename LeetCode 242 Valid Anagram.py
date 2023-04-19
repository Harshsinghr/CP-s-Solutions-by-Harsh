#LeetCode 242 Valid Anagram's solution in Python
"""
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return
        d1={}
        d2={}
        for i in 'abcdefghijklmnopqrstuvwxyz':
            d1[i]=0
        for i in 'abcdefghijklmnopqrstuvwxyz':
            d2[i]=0
        for i in s:
            d1[i]+=1
        for i in t:
            d2[i]+=1
        for i in 'abcdefghijklmnopqurstuvwxyz':
            if d1[i]!=d2[i]:
                return False
        return True
