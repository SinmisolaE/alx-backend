#!/usr/bin/env python3

"""
  class MRUOCache that inherits from BaseCaching
  and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
        must use self.cache_data
        can overload def __init__(self):
    """
    def __init__(self):
        """ initializes inherited properties
        """
        super().__init__()
        self.sorted_cache = OrderedDict()

    def put(self, key, item):
        """
           assign to self.cache_data the item value for the key key
           If key or item is None, this method should not do anything
           If the number of items in self.cache_data
           is higher that BaseCaching.MAX_ITEMS:
           you must discard the most recently item put in cache
           you must print DISCARD: with the key discarded
           and following by a new line
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    most_recent = list(self.sorted_cache.keys())[-1]
                    print('DISCARD: {}'.format(most_recent))
                    del self.cache_data[most_recent]
                    del self.sorted_cache[most_recent]
            self.cache_data[key] = item
            self.sorted_cache[key] = item
            self.sorted_cache.move_to_end(key)

    def get(self, key):
        """
           return the value in self.cache_data linked to key
           If key is None or if the key doesn’t exist in self.cache_data
           return None
        """
        if key is None or key not in self.cache_data:
            return None

        self.sorted_cache.move_to_end(key)

        return self.cache_data[key]
