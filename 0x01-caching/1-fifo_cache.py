#!/usr/bin/python3
""" FIFO Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item """
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.move_last(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Gets cache """
        return self.cache_data.get(key, None)

    def move_last(self, item):
        """ Moves element to last on list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def first_list(array):
        """ Get first element """
        return array[0] if array else None