def max_heapify(books, key, i, heap_size):
    left = 2*i + 1
    right = 2*i + 2
    if left < heap_size and books[left][key] > books[i][key]:
        largest = left
    else:
        largest = i
    if right < heap_size and books[right][key] > books[largest][key]:
        largest = right
    if largest != i:
        books[i], books[largest] = books[largest], books[i]
        max_heapify(books, key, largest, heap_size)


def build_max_heap(books, *, key, heap_size):
    for i in reversed(range(len(books) // 2)):
        max_heapify(books, key, i, heap_size)


def heapsort(books, *, key):
    heap_size = len(books)
    build_max_heap(books, key=key, heap_size=heap_size)
    for i in reversed(range(1, len(books))):
        books[0], books[i] = books[i], books[0]
        heap_size -= 1
        max_heapify(books, key, 0, heap_size)
