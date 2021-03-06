'''
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)>=3:
            for i in range(2,len(coordinates)):
                if (coordinates[1][1]-coordinates[0][1])*(coordinates[i][0]-coordinates[0][0])!=\
                (coordinates[i][1]-coordinates[0][1])*(coordinates[1][0]-coordinates[0][0]): #类似1037 判断三点一线：(y2-y1)*(x3-x1)==(y3-y1)*(x2-x1)
                    return False
            else:
                return True
        elif len(coordinates)==2:
            return True