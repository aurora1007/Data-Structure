## Method 1: Use OrderedDict
import collections
class LRU_Cache(object):

	def __init__(self, capacity):
		# Initialize class variables
		self.cache = collections.OrderedDict()
		self.capacity = capacity

	def get(self, key):
		# Retrieve item from provided key. Return -1 if nonexistent. 
		if key not in self.cache:
			return -1
		self.cache.move_to_end(key, last = False)
		return self.cache[key]


	def set(self, key, value):
		# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
		
		self.cache[key] = value
		self.cache.move_to_end(key, last = False)
		if len(self.cache) > self.capacity:
			self.cache.popitem()
	
 
			

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry



# Method 2: OrderedDict from Scratch
class DLinkedlistNode:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.pre = None
		self.next = None
		
class LRU_Cache:
	def __init__(self, capacity):
		self.cache = {}
		self.head = DLinkedlistNode(0,0)
		self.tail = DLinkedlistNode(0,0)
		self.head.next = self.tail
		self.tail.pre = self.head
		self.capacity = capacity
		
	def __remove_node(self, node):
		node.pre.next = node.next
		node.next.pre = node.pre                                                                                                         
		
	def __insert_node_to_end(self, node):
		self.tail.pre.next = node
		node.pre = self.tail.pre
		self.tail.pre = node
		node.next = self.tail
		
	def __move_node_to_end(self, node):
		self.__remove_node(node)
		self.__insert_node_to_end(node)
	
	def get(self, key):
		# cache hit, return the appropriate value
		if key in self.cache:
			res = self.cache[key].val
			self.__move_node_to_end(self.cache[key])
			return res
		# cache miss, return -1
		else:
			return -1
	
	def set(self, key, value):
		if key in self.cache:
			node = self.cache[key]
			node.val = value         
			self.__move_node_to_end(node)
			
		else:
			node = DLinkedlistNode(key, value)
			self.cache[key] = node
			self.__insert_node_to_end(node)
			if len(self.cache) > self.capacity:
				del self.cache[self.head.next.key]
				self.__remove_node(self.head.next)
 
	
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
