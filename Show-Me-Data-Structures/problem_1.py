from collections import OrderedDict
class LRU_Cache(object):

# Lets initialize the capacity

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

# we need to return the value of the key and move the key to the end for recently used key
    def get(self, key):
        
        if key not in self.cache:
            
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

# lets add / update the key, move it to the end, and check whether the length of the ordered dict has exceeded the capacity
    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

# initializing the cache with the capacity of 5            
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

 