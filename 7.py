'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
示例 1：
输入：x = 123
输出：321
示例 2：
输入：x = -123
输出：-321
示例 3：
输入：x = 120
输出：21
示例 4：
输入：x = 0
输出：0
提示：
-2^31 <= x <= 2^31 - 1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            rx=int(str(x)[::-1])
            if rx<-pow(2,31) or rx>pow(2,31)-1:
                return 0
            else:
                return rx
        elif x<0:
            rx=0-int(str(abs(x))[::-1])
            if rx<-pow(2,31) or rx>pow(2,31)-1:
                return 0
            else:
                return rx
        else:
            return 0