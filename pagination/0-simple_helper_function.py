#!/usr/bin/env python3
"""
Simple helper function to calculate index range for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start index and end index
    to retrieve a specific page in a dataset.
    
    Arguments:
    - page: The page number (1-indexed).
    - page_size: The number of items per page.
    
    Returns:
    - A tuple (start_index, end_index) that corresponds to the
      range of indexes to retrieve for the given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
