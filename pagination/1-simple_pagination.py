#!/usr/bin/env python3
"""
Simple pagination class for popular baby names dataset.
"""

import csv
from typing import List
from 0_simple_helper_function import index_range

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset."""
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"
        
        # Get the correct index range for the given page and page_size
        start_idx, end_idx = index_range(page, page_size)
        
        # Retrieve the data page
        data = self.dataset()
        
        # If the index is out of bounds, return an empty list
        if start_idx >= len(data):
            return []
        
        return data[start_idx:end_idx]
