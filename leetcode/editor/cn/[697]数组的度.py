# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。 
#  你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
#  示例 1：
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
#  示例 2： 
# 输入：[1,2,2,3,1,4,2]
# 输出：6
#
#  提示： 
#  nums.length 在1到 50,000 区间范围内。
#  nums[i] 是一个在 0 到 49,999 范围内的整数。 
#  
#  Related Topics 数组 
#  👍 316 👎 0
"""
思路:
1. 一次遍历获取到出现次数(count)、首次位置(right)、最后位置(left)
2. 对count进行排序, 获取到出现次数最大值
3. 遍历count与出现次数最大值相比较, 若相等则进行最短子数组长度计算
4. min() 函数中right取值使用了get方法是考虑到列表长度为1的情况right为空字典, 对其设置默认值, 防止key error情况
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = dict(), dict(), dict()

        for i, v in enumerate(nums):
            if v in count:
                count[v] += 1
                right[v] = i
            else:
                count[v] = 1
                left[v] = i

        max_num = sorted(count.items(), key=lambda x: x[1])[-1][-1]
        res = min(right.get(num, left[num]) - left[num] + 1 for num in count.keys() if count[num] == max_num)

        return res


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    Solution().findShortestSubArray(nums)
