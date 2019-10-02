#### Bitwise Opertaions


#### Dictionary
- Intersection of dictionaries:
```python
from collections import Counter

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

c1 = Counter(nums1)  # {4: 1, 9: 1, 5: 1}
c2 = Counter(nums2)  # {9: 2, 4: 2, 8: 1}

intersection = c1 & c2  # {4: 1, 9: 1}

intersection.elements()  # [4, 9]

```