def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Return a page of the dataset, or empty list if arguments are invalid."""
    assert isinstance(page, int) and page > 0, "page must be a positive integer"
    assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

    dataset = self.dataset()
    start, end = index_range(page, page_size)

    if start >= len(dataset):
        return []

    return dataset[start:end]
