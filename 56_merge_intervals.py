class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # we need to sort the intervals by the first values of each pair
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        curr_inter = intervals[0]
        output = []
        output.append(curr_inter)

        for i in range(1, len(intervals)):
            # always the last element
            curr_begin = output[-1][0]
            curr_end = output[-1][1]
            next_begin = intervals[i][0]
            next_end = intervals[i][1]

            if curr_end >= next_begin:
                # we want to change the second element in the pair of
                output[-1][1] = max(curr_end, next_end)
            else:
                output.append(intervals[i])

        return output


intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
obj = Solution()
merged_inter = obj.merge(intervals)
print(merged_inter)

