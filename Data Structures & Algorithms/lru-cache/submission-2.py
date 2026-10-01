class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self,node):
        # prev <-> node <-> next
        # prev <-> next
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_back(self,node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
    def _prepend(self, node):
        self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
    
    def _make_recent(self,node):
        self._remove(node)
        self._prepend(node)



    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self._make_recent(node)
        return node.v
        

        

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.mapping: #update value
            node = self.mapping[key]
            node.v = value
            self._remove(node)
        else:
            node = Node(key, value)
            if len(self.mapping) == self.capacity:
                # remove last node and delete its key
                removed = self.tail.prev
                self._remove(removed)
                del self.mapping[removed.k]
        self.mapping[node.k] = node
        self._prepend(node)
           

        
