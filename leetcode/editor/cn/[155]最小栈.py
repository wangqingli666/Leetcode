# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。 
#  top() —— 获取栈顶元素。 
#  getMin() —— 检索栈中的最小元素。 
#
#  示例: 
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#  提示： 
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#  
#  Related Topics 栈 设计 
#  👍 817 👎 0

"""
思路: 实现栈
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.record = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.record.append(x)

    def pop(self):
        """
        :rtype: None
        """
        return self.record.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.record[len(self.record) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        _list = self.record
        num = sorted(_list)[0]
        return num
