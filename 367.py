'''
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如  sqrt 。
示例 1：
输入：num = 16
输出：true
示例 2：
输入：num = 14
输出：false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,int(num**0.5+1)):
            if i**2==num:
                return True
                break
        else:
            return False

