class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1 = []
        size = 0
        for i in s:
            if i not in l1:
                l1.append(i)
                if len(l1)>size:
                    size = len(l1)
            else:
                last_index = len(l1) - 1 - l1[::-1].index(i)
                l1 = l1[last_index+1:]
                l1.append(i)
                if len(l1)>size:
                    size = len(l1)
        return size
