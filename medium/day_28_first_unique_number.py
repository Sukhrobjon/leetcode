from collections import deque


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.queue = deque()
        self.value_count = {}
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        # if there is element in the queue and front of the queue
        # has 1 occurance
        while len(self.queue) > 0 and self.value_count[self.queue[0]] > 1:
            self.queue.popleft()
        
        if len(self.queue) == 0:
            return -1

        else:
            return self.queue[0]

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.value_count:
            self.value_count[value] += 1
        else:
            self.value_count[value] = 1
            self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
