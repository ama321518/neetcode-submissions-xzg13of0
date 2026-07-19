class Node:
    
    def __init__(self, key, val):
        self.key,self.val = key, val
        
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)#dummy 
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head#head lets us find lru to kik out and tail mru to move to front

    def remove(self, node):#applied to linked list,remove from list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):#insert 
        nxt = self.head.next
        self.head.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = self.head

    def get(self, key: int) -> int:
        if  key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])




        if len(self.cache) > self.capacity:
            lru = self.tail.prev#always points to what was used least
            self.remove(lru)
            del self.cache[lru.key]
   