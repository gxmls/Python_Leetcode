'''
给你一个下标从 0 开始的字符串 s ，它的 偶数 下标处为小写英文字母，奇数 下标处为数字。
定义一个函数 shift(c, x) ，其中 c 是一个字符且 x 是一个数字，函数返回字母表中 c 后面第 x 个字符。
比方说，shift('a', 5) = 'f' 和 shift('x', 0) = 'x' 。
对于每个 奇数 下标 i ，你需要将数字 s[i] 用 shift(s[i-1], s[i]) 替换。
请你替换所有数字以后，将字符串 s 返回。题目 保证 shift(s[i-1], s[i]) 不会超过 'z' 。
示例 1：
输入：s = "a1c1e1"
输出："abcdef"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
示例 2：
输入：s = "a1b2c3d4e"
输出："abbdcfdhe"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-all-digits-with-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c,x):
            return chr(ord(c)+eval(x)) #这里要用eval()，否则会提示TypeError: unsupported operand type(s) for +: 'int' and 'str'
        sn=''
        for i in range(0,len(s),2):
            if i<len(s)-1: #这里要判断最后一个字符后面有没有数字，比如s = "a1b2c3d4e"
                sn+=s[i]
                sn+=shift(s[i],s[i+1])
            else:
                sn+=s[i]
        return sn
