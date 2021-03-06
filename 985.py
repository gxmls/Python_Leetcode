'''
给出一个整数数组 A 和一个查询数组 queries。
对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。
（此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
示例：
输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
输出：[8,6,2,4]
解释：
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ls=[]
        sum_ori=0
        for item in nums:
            if item%2==0:
                sum_ori+=item #为减少循环数，先计算原始nums中偶数的和
        for i in range(len(queries)):
            index=queries[i][1]
            val=queries[i][0]
            if nums[index]%2==0 and val%2==0: 
                sum_ori+=val #如果被查询的数字原本是偶数，加上一个偶数还是偶数，总偶数和为ori加val
                nums[index]+=val
                ls.append(sum_ori)
            elif nums[index]%2==0 and val%2!=0: 
                sum_ori-=nums[index] #如果被查询的数字原本是偶数，加上一个奇数变为奇数，总偶数和为ori减掉被查询的数字
                nums[index]+=val
                ls.append(sum_ori) 
            elif nums[index]%2!=0 and val%2==0: #如果被查询的数字原本是奇数，加上一个偶数还是奇数，总偶数和不变
                nums[index]+=val
                ls.append(sum_ori)
            else: 
                nums[index]+=val
                sum_ori+=nums[index] #如果被查询的数字原本是奇数，加上一个奇数变为偶数，总偶数和为ori加上变更后的数字
                ls.append(sum_ori)
        return ls

