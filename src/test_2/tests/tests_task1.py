from task1 import BinTree, BinHeap


def test_tree_creation(self):
    node = BinTree(10, "test")
    assert node.key == 10
    assert node.value == "test"
    assert node.parents is None
    assert node.child is None
    assert node.sibling is None
    assert node.degree == 0


def test_tree_without_value(self):
    node = BinTree(5)
    assert node.key == 5
    assert node.value is None


def test_empty_heap(self):    
    heap = BinHeap()
    assert heap.head is None
    assert heap.getMinimum() is None


def test_single_insert(self):
    heap = BinHeap()
    heap.insert(10, "A")
    assert heap.head is not None
    assert heap.head.key == 10
    assert heap.head.value == "A"
    assert heap.head.degree == 0


def test_multiple_inserts(self):
    heap = BinHeap()
    heap.insert(30)
    heap.insert(20)
    heap.insert(10)
    assert heap.getMinimum() == 10
