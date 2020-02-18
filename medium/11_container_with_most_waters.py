class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initial area, left and right pointers
        area, left, right = 0, 0, len(height) - 1
        while left < right:
            new_area = (right - left) * min(height[left], height[right])
            area = max(area, new_area)
            if height[left] <= height[right]:
                # we want to keep the bigger number
                left += 1
            else:
                right -= 1
        return area
    
    def maxArea_v2(self, height):
        """
        NOTE: This doesnt work for all cases:
        For example: [1, 2, 1]
        :type height: List[int]
        :rtype: int
        """
        # set the area = 0
        # for each h in height
        # calculate the area with current width
        max_index = height.index(max(height))
        print(f"max index-> {max_index}")
        l_area, r_area = 0, 0
        unit = 1
        # right side of the heighest vertical line
        for i in range(max_index+1, len(height)):
            h = height[i]
            area = h * unit

            print("h: ", h)
            print("area:",area)
            r_area = max(r_area, area)
            unit += 1
        print(r_area)
        unit = 1
        # left side
        for i in range(max_index-1, -1, -1):
            h = height[i]
            area = h * unit
            l_area = max(l_area, area)
            unit += 1
            print(f"left h: {h}")

        return r_area if r_area >= l_area else l_area


obj = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
h_1 = [1, 5, 3, 8, 2, 9]
area = obj.maxArea(height)
print(area)
