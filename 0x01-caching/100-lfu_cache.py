#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.insert(0, key)
        self.right_list(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.right_list(key)
        return item

    def right_list(self, item):
        """ Moves element to the right"""
        length = len(self.queue)

        indx = self.queue.index(item)
        item_count = self.counter[item]

        for i in range(indx, length):
            if i != (length - 1):
                nxt = self.queue[i + 1]
                nxt_count = self.counter[nxt]

                if nxt_count > item_count:
                    break

        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def first_list(array):
        """ Get first element """
        return array[0] if array else None
