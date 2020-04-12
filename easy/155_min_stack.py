class MinStack(object):
    """
        Min stack works just like regular stack except, it stores the current
        `minimum value` so far.
        Example: 4, 6, 3, 5, 2, 1 <- stack is added this way, 1 is at the top
                (4, 4, 3, 3, 2, 1)
                (1, 1)
                (2, 2)
                (5, 3)
                (3, 3)
                (6, 4)
                (4, 4)
    """
    def __init__(self):
        """
        Initialize data structure, store the val and min number
        """
        # stack => [(curr_val, min_val_so_far)]
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curr_min = self.getMin()
        if curr_min is None or curr_min > x:
            # update the current min
            curr_min = x
        # add the new element and store the curr min so far
        self.stack.append((x, curr_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            # pop the top of the element, the tuple
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            # access the top element, it is the 0th element in tuple
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        # the second item in the tuple is the current min val
        return self.stack[-1][1]


if __name__ == "__main__":
    stack_obj = MinStack()
    print(stack_obj.getMin())
    stack_obj.push(4)
    stack_obj.push(6)
    stack_obj.push(3)
    stack_obj.push(5)
    print(stack_obj.top())
    print(stack_obj.getMin())
    print(stack_obj.stack)

