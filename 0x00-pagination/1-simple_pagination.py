#!/usr/bin/env python3

""" index_range from the previous task
    and the following class into your code"""
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
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
        """ two integer arguments page with default value 1
            and page_size with default value 10
            assert to verify that both arguments are integers greater than 0.
            return the appropriate page of the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page > 0

        dataset = self.dataset()
        try:
            num = index_range(page, page_size)
            return dataset[num[0]:num[1]]
        except IndexError:
            return []
