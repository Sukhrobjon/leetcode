# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # number one solution would be to reverse the lists
        # but as it is noted in the description of the problem
        # it is not allowed to modify the input
        # the other way would be get the length of the smaller list
        
        stack_1 = []
        stack_2 = []
        # put all numbers into stack from list 1
        curr_1, curr_2 = l1, l2
        while curr_1 and curr_2:
            stack_1.append(curr_1.val)
            stack_2.append(curr_2.val)
            curr_1 = curr_1.next
            curr_1 = curr_1.next

        # add remaining node values to stack
        if curr_1:
            while curr_1:
                stack_1.append(curr_1.val)
        if curr_2:
            while curr_2:
                stack_2.append(curr_2.val)

        power = 0
        result = 0

        while stack_1 and stack_2:
            # pop the top of the stack
            num_1 = stack_1.pop()
            num_2 = stack_2.pop()
            result += (num_1*(10**power) + num_2*(10**power))
            # increment the power(of 10)
            power += 1
        
        if stack_1:
            while stack_1:
                num = stack_1.pop()
                result += num*(10**power)
                power += 1
        if stack_2:
            while stack_2:
                num = stack_2.pop()
                result += num*(10**power)
                power += 1

        result = str(result)
        # build the linked list version of number
        head = curr = ListNode(result[0])
        for i in range(1, len(result)):
            digit = result[i]
            new_node = ListNode(digit)
            curr.next = new_node
            curr = new_node

        return head
    # def length(self, head):
    #     """
    #         Find the length of the given linked list
    #     """
