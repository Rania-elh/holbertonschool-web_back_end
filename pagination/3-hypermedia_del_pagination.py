#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination for popular baby names dataset.
"""

import csv
from typing import List, Dict
from 2_hypermedia_pagination import Server

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia pagination with deletion resilience."""
        assert isinstance(index, int) and index >= 0, "index must be a non-negative integer"
        
        dataset = self.indexed_dataset()
        
        # Get the requested data
        page_data = []
        next_index = index
        while len(page_data) < page_size and next_index < len(dataset):
            if next_index in dataset:
                page_data.append(dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'data': page_data,
            'page_size': page_size,
            'next_index': next_index if next_index < len(dataset) else None
        }

