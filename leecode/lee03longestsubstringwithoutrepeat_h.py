# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 22:03
# @Author  : Hzhang
# @Email   : zyh_njust@hotmail.com
# @File    : lee03longestsubstringwithoutrepeat_h.py
# @Software: PyCharm
# 其实这个题目还是很熟练， 首先这个地方的用法
#
# countDict[c] = countDict.get(c, 0) + 1  # if no, return 0
# countDict[s[start]] -= 1
# 还有就是是不是python 独有的 如果java 怎么说。已经复杂度分析 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans, start, end = 0, 0, 0
        countDict={}
        for c in s:
            end +=1
            countDict[c] = countDict.get(c, 0) + 1 # if no, return 0
            while countDict[c] > 1:
                countDict[s[start]]-=1
                start+=1
            ans= max(ans, (end-start))
        print(ans)
        return ans
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abceaepolka") == 6



