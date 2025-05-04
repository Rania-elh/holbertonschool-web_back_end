#!/usr/bin/env python3
"""Pagination server that loads a CSV dataset and returns paginated results."""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads dataset from CSV and caches it."""
        if self.__dataset is None:
            with open("Popular_Baby_Names.csv") as f:
                reader = csv.reader(f)
                data = list(reader)
                self.__dataset = data[1:]  # skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.
        
        Args:
            page (int): The page number, 1-indexed.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The requested page of the dataset.
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]
