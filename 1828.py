'''
给你一个数组 points ，其中 points[i] = [xi, yi] ，表示第 i 个点在二维平面上的坐标。多个点可能会有 相同 的坐标。
同时给你一个数组 queries ，其中 queries[j] = [xj, yj, rj] ，表示一个圆心在 (xj, yj) 且半径为 rj 的圆。
对于每一个查询 queries[j] ，计算在第 j 个圆 内 点的数目。如果一个点在圆的 边界上 ，我们同样认为它在圆 内 。
请你返回一个数组 answer ，其中 answer[j]是第 j 个查询的答案。
输入：points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
输出：[3,2,2]
输入：points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
输出：[2,3,2,4]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ls=[]
        for i in range(len(queries)):
            count=0
            for point in points:
                if ((point[0]-queries[i][0])**2+(point[1]-queries[i][1])**2)**0.5<=queries[i][-1]: #任意两点间距离公式：((x1-x2)^2+(y1-y2)^2)**0.5
                    count+=1
            ls.append(count)
        return ls