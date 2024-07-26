#!/usr/bin/env python3

"""
  class LFUCache that inherits from BaseCaching
  and is a caching system
"""
from collections import defaultdict, OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        must use self.cache_data
        can overload def __init__(self):
    """
    def __init__(self):
        """ initializes inherited properties
        """
        super().__init__()
        self.freq = defaultdict(int)
        self.min_freq = 0
        self.sorted_cache = OrderedDict()

    def put(self, key, item):
        """
           assign to self.cache_data the item value for the key key
           If key or item is None, this method should not do anything
           If the number of items in self.cache_data
           is higher that BaseCaching.MAX_ITEMS:
           you must discard the least frequently item
           f you find more than 1 item to discard
           you must use the LRU algorithm
           to discard only the least recently used
           you must print DISCARD: with the key discarded
           and following by a new line
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.sorted_cache[key] = item
                self.sorted_cache.move_to_end(key)
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self.evict_lfu()
                self.cache_data[key] = item
                self.sorted_cache[key] = item
                self.sorted_cache.move_to_end(key)
                self.freq[key] = 1
                self.min_freq = 1

    def get(self, key):
        """
           return the value in self.cache_data linked to key
           If key is None or if the key doesn’t exist in self.cache_data
           return None
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.sorted_cache.move_to_end(key)

        return self.cache_data[key]

    def evict_lfu(self):
        """ checks the least frequently used"""
        min_freq_keys = [k for k, v in self.freq.items() if v == self.min_freq]
        lrlf = None
        if len(min_freq_keys) > 1:
            for k in self.sorted_cache:
                if k in min_freq_keys:
                    lrlf = k
                    break
        elif len(min_freq_keys) == 1:
            lrlf = min_freq_keys[0]
        if lrlf is not None:
            print('DISCARD: {}'.format(lrlf))
            del self.cache_data[lrlf]
            del self.sorted_cache[lrlf]
            del self.freq[lrlf]
            if len(self.freq) > 0:
                self.min_freq = min(self.freq.values())
            else:
                self.min_freq = 0
