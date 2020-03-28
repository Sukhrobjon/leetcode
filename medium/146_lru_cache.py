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

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def items(self):
        """
            Return a list of all items in this linked list.
            Best and worst case running time: Theta(n) for n items in the list
            because we always need to loop through all n nodes.
        """
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.key)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def get(self, key):
        """
        Takes key and returns its value if it exists, otherwise -1
        :type key: int
        :rtype: value(int)
        """

        if self.contains(key):
            val = self.move_to_head(key)
            # we need to put it at the head now because each time,
            # we interact with that node it has to move to head
            # call move_to_head()
            return val

        # if key not in there
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print(f"putting {key}, {value}")
        # if the key is exist and the value is new we simple update its value
        # and move it to the head
        if key in self.cache:
            print("Existing key being updated!")
            # get the node
            node = self.cache[key]
            # update its value
            node.value = value
            # move it to the head
            self.move_to_head(key)
        # else, key is new so we need create and insert it at the head
        else:
            # create a new node
            node = DLLNode(key, value)
            # have a reference to node
            # if the cache is empty
            if self.head is None:
                # head and tail points to node
                print("Putting item in empty list!")
                self.cache[key] = node
                self.head = node
                self.tail = node
                
            # if there is enough space in cache
            elif self.length() < self.capacity:
                self.cache[key] = node
                print("there is enough space")
                self.update_head(key)
            # there is no space so we need to remove the tail and insert the new node at head
            else:
                print("Putting item into list and remove tail!")
                # first insert the item at the head
                self.cache[key] = node
                self.update_head(key)
                # remove the tail
                self.remove_tail()

    def move_to_head(self, key):
        """
            Move existing node in the list to head
        """

        # access the node
        node = self.cache[key]
        # if node is head
        if self.head == node:
            # do nothing
            return node.value

        # if the node is tail
        if self.tail == node:
            node.prev.next = node.next
            # make the node. prev as new tail
            self.tail = node.prev
            # now move the node to the head
            self.update_head(key)
            return node.value

        # ============if node is in the middle not head or tail================
        # link two adjecent nodes together
        node.prev.next = node.next
        node.next.prev = node.prev
        # now move the node to the head
        self.update_head(key)

        return node.value

    def update_head(self, key):
        """
            move update the head with the node with given key
        """
        # get the node
        node = self.cache[key]

        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node
    
    def remove_tail(self):
        """
            remove the current tail and update it
        """
        node = self.tail
        node.prev.next = None
        self.tail = node.prev
        key = node.key
        # delete the node from the dict cache
        del self.cache[key]
  
    def length(self):
        """
            returns the length of the cache
        """
        return len(self.cache)

    def contains(self, key):
        """
            Returns True if key is in the dictionary, otherwise False
        """
        if key in self.cache:
            return True
        return False
        
if __name__ == "__main__":
    capacity = 2
    cache = LRUCache(capacity)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.__str__())
    print(cache.get(1))
    print(cache.__str__())
    cache.put(3, 3)  # evicts 2
    print(cache.__str__())
    print(cache.get(2))  # -1
    cache.put(4, 4)  # evicts 
    print(cache.__str__())
    print(cache.get(1))  # -1
    print(cache.__str__())
    print(cache.get(3))
    print(cache.__str__())
    print(cache.get(4))
    print(cache.__str__())
