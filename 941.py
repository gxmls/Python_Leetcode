'''
给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
arr.length >= 3
在 0 < i < arr.length - 1 条件下，存在 i 使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
示例 1：
输入：arr = [2,1]
输出：false
示例 2：
输入：arr = [3,5,5]
输出：false
示例 3：
输入：arr = [0,3,2,1]
输出：true
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)>=3 and arr!=sorted(arr) and arr!=sorted(arr,reverse=True): #一直升或一直降都不是mountain array
            for i in range(len(arr)-1):
                if arr[i]<arr[i+1]:
                    continue
                else:
                    for j in range(i,len(arr)-1):
                        if arr[j]>arr[j+1]:
                            continue
                        else:
                            return False
                            break
                    else:
                        return True #先升后降才是mountain array
                        break #跳出外层循环，可以不用重复遍历了
        else:
            return False