# Pagination

This project focuses on implementing pagination systems in Python, based on CSV data. You will build helper functions and classes that support:

- Simple pagination with `page` and `page_size`
- Hypermedia pagination with metadata (e.g. `next_page`, `prev_page`)
- Deletion-resilient pagination using indexed datasets

## Learning Objectives

By the end of this project, you should be able to explain:
- How to paginate a dataset using `page` and `page_size`
- How to build a pagination system that returns hypermedia metadata
- How to ensure pagination works correctly even when dataset entries are deleted

## Requirements

- Python 3.9
- Code style: `pycodestyle` (version 2.5.*)
- All files must start with `#!/usr/bin/env python3`
- All files should end with a new line
- All functions and classes must be documented with real sentences
- All functions must use type annotations

## Setup

The project uses the `Popular_Baby_Names.csv` dataset, which must be in the root directory.

```bash
wc -l Popular_Baby_Names.csv
# 19419 Popular_Baby_Names.csv

