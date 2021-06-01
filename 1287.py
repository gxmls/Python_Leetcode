'''
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
请你找到并返回这个整数
示例：
输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter #Counter()用来统计元素出现的次数
        dn=dict(Counter(arr))
        ls=[key for key,value in dn.items() if value>0.25*len(arr)]
        return ls[0]

