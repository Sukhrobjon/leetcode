"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class DLLNode(object):
    """
        Double linked list to hold the node data
    """
    def __init__(self, key, value):
        """
            Initialize the node object with key, value, next and prev pointers
        """
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    """
        Discards the least recently used items first. This algorithm requires
        keeping track of what was used when, which is expensive if one wants
        to make sure the algorithm always discards the least recently used
        item. General implementations of this technique require keeping
        "age bits" for cache-lines and track the "Least Recently Used"
        cache-line based on age-bits. In such an implementation, every time
        a cache-line is used, the age of all other cache-lines changes. 
        
    """
    def __init__(self, capacity):
        """
            Initialize the lru object with given capacity
            :type capacity: int
        """
        self.capacity = capacity
        # empty cache
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        Takes key and returns its value if it exists, otherwise -1
        :type key: int
        :rtype: value(int)
        """

        if self.contains(key):
            val = self.cache[key].value
            return val

        # if key not in there
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        pass

    def contains(self, key):
        """
            Returns True if key is in the dictionary, otherwise False
        """
        if key in self.cache:
            return True
        return False
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
