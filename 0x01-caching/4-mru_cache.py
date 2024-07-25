#!/usr/bin/env python3

"""
  class FIFOCache that inherits from BaseCaching
  and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
           you must discard the first item put in cache
           you must print DISCARD: with the key discarded
           and following by a new line
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first_key))
                del self.cache_data[first_key]

    def get(self, key):
        """
           return the value in self.cache_data linked to key
           If key is None or if the key doesn’t exist in self.cache_data
           return None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
