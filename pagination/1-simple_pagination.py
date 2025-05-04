#!/usr/bin/env python3
"""Pagination server that loads a CSV dataset and returns paginated results."""

import csv
from typing import List, Tuple
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads dataset from CSV and caches it."""
        if self.__dataset is None:
            with open("popular_baby_names.csv") as f:
                reader = csv.reader(f)
                data = list(reader)
                self.__dataset = data[1:]  # skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

