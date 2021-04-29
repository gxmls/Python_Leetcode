'''
如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。
给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。
示例 1：
输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。
示例 2：
输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。
示例 3：
输入：coordinates = "c7"
输出：false
'''

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        for i in ['a','b','c','d','e','f','g','h']:
            if (ord(coordinates[0])-ord(i))%2==0:
                if eval(coordinates[-1])%2==1:
                    return False
                else:
                    return True
            else:
                if eval(coordinates[-1])%2==1:
                    return True
                else:
                    return False
