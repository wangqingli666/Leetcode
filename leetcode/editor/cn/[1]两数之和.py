# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#  你可以按任意顺序返回答案。
#
#  示例 1： 
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#  示例 2： 
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#  示例 3： 
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#  提示： 
#  2 <= nums.length <= 103
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10348 👎 0
"""
思路:
逆向思维, 创建dict, 遍历数组使用target与每次循环的value进行相减
若不存在则插入{value: index}, 若存在直接返回结果
时间复杂度为 O(n)
若有返回多组结果的情况下可在创建一个list, 之后对通过检验的数据进行append操作即可
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i, v in enumerate(nums):
            _num = target - v
            if _num in data:
                return [data[_num], i]
            data[v] = i


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    Solution().twoSum(nums, target)
