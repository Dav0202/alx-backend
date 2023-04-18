#!/usr/bin/env python3
""" Hypermedia Pagination """
import csv
from math import ceil
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Pagination function """

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


class Server:
    """Server class to paginate a database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves paginated data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Provides information about dataset """
        data = self.get_page(page, page_size)

        data_set = self.__dataset
        len_set = len(data_set) if data_set else 0

        total_pages = ceil(len_set / page_size) if data_set else 0

        if not data:
            page_size = 0
        else:
            page_size = len(data)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        pagination_data = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return pagination_data
