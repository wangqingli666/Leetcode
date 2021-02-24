# 给你一个整数数组 nums，请编写一个能够返回数组 “中心索引” 的方法。 
#  数组 中心索引 是数组的一个索引，其左侧所有元素相加的和等于右侧所有元素相加的和。
#  如果数组不存在中心索引，返回 -1 。如果数组有多个中心索引，应该返回最靠近左边的那一个。
# 
#  注意：中心索引可能出现在数组的两端。 
#
#  示例 1： 
# 输入：nums = [1, 7, 3, 6, 5, 6]
# 输出：3
# 解释：
# 中心索引是 3 。
# 左侧数之和 (1 + 7 + 3 = 11)，
# 右侧数之和 (5 + 6 = 11) ，二者相等。
#
#  示例 2： 
# 输入：nums = [1, 2, 3]
# 输出：-1
# 解释：
# 数组中不存在满足此条件的中心索引。 
# 
#  示例 3： 
# 输入：nums = [2, 1, -1]
# 输出：0
# 解释：
# 中心索引是 0 。
# 索引 0 左侧不存在元素，视作和为 0 ；
# 右侧数之和为 1 + (-1) = 0 ，二者相等。
#
#  提示： 
#  nums 的长度范围为 [0, 10000]。
#  任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。 
#  
#  Related Topics 数组 
#  👍 302 👎 0

"""
思路:
plan1
    执行用时：3616 ms
    内存消耗：13.5 MB
    通过遍历列表取出下标及对应元素, 循环中进行求和校验
    此方法由于涉及每次循环都进行复杂度为O(n)的求和运算以及对数组进行切片的操作, 若遇大数据量情况下很可能会出现超时问题

plan2
    执行用时：36 ms
    内存消耗：13.7 MB
    利用滑动窗口算法, 将求和运算移到循环外, 循环内部只进行数值类型加减、比较的操作
"""


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, value in enumerate(nums):
            if sum(nums[:index]) == sum(nums[index + 1:]):
                return index

        return -1

    def pivotIndex1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_count = sum(nums[:0])
        right_count = sum(nums[1:])

        for i in range(0, len(nums) - 1):
            if left_count == right_count:
                return i
            left_count += nums[i]
            right_count -= nums[i + 1]

        if left_count == right_count:
            return len(nums) - 1

        return -1


if __name__ == '__main__':
    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [2, 1, -1]
    nums = [-1, -1, 0, 1, 1, 0]
    Solution().pivotIndex1(nums)
