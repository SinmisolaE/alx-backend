#!/usr/bin/env python3

"""
  class LIFOCache that inherits from BaseCaching
  and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        must use self.cache_data
        can overload def __init__(self):
    """
    def __init__(self):
        """ initializes inherited properties
        """
        super().__init__()

    def put(self, key, item):
        """
           assign to self.cache_data the item value for the key key
           If key or item is None, this method should not do anything
           If the number of items in self.cache_data
           is higher that BaseCaching.MAX_ITEMS:
           you must discard the last item put in cache
           you must print DISCARD: with the key discarded
           and following by a new line
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_key = list(self.cache_data.keys())[-1]
                print('DISCARD: {}'.format(last_key))
                del self.cache_data[last_key]
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
           return the value in self.cache_data linked to key
           If key is None or if the key doesn’t exist in self.cache_data
           return None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
