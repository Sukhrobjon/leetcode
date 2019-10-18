class Solution(object):
    def searchRange(self, array, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.first_occur_binary_search(array, target)
        last = self.last_occur_binary_search(array, target)
        return [first, last]

    def binary_search(self, array, target):
        if not array:
            return -1

        left = 0
        right = len(array)

        while left < right:
            # mid = (right + left) // 2
            mid = left + (right - left) // 2
            # print(f"mid {mid}")
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def first_occur_binary_search(self, array, target):
        """
        Search for the first occurrence of the target and returns the
        index, or -1 if target not found.
        Args:
            array (list): list of integers
            target (int): a target to be found
        Returns:
            index (int): the first occurrence of the target, -1 if not found
        """

        first_occur = self.binary_search(array, target)
        # print(f"first occurrence: {first_occur}")
        if first_occur == -1:
            return -1

        left = 0
        right = first_occur

        while left < right:
            mid = left + (right - left) // 2
            # print(f"while:")
            # print(f"left: {left}, right: {right}, mid: {mid}")
            if target == array[mid]:
                # there is another target in the array, now updating
                first_occur = mid
                # print(f"mid < first")
                right = mid
            elif target > array[mid]:
                left = mid + 1
            else:
                right = mid

        return first_occur

    def last_occur_binary_search(self, array, target):
        """
        Search for the first occurrence of the target and returns the
        index, or -1 if target not found.
        Args:
            array (list): list of integers
            target (int): a target to be found
        Returns:
            index (int): the first occurrence of the target, -1 if not found
        """

        last_occur = self.binary_search(array, target)

        # the target is not in the array
        if last_occur == -1:
            return -1
        # print(f"last occur: {last_occur}")
        left = last_occur
        right = len(array)

        while left < right:
            mid = left + (right - left) // 2
            # print(f"left: {left}, right: {right}, mid: {mid}")
            if target == array[mid]:
                # if mid > last_occur
                last_occur = mid
                left = mid + 1

            elif target > array[mid]:
                left = mid + 1
            else:
                right = mid
        return last_occur


array = [5, 7, 7, 8, 8, 10]
all_dups = [1, 1, 1, 1, 1, 1, 1]
print(array)
obj = Solution()
result = obj.searchRange(array, 8)
print(result)
