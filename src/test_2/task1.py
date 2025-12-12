class BinTree:
    def __init__(self, key, value=None):
        self.key = key # ключ (вес) элемента
        self.value = value # данные
        self.parent = None # указатель на родителя узла
        self.child = None # указатель на левого ребенка узла
        self.sibling = None # указатель на правого брата узла
        self.degree = 0 # степень узла (количество дочерних узлов данного узла)

class BinHeap:
    def __init__(self):
        self.head = None # указатель на корень биномиального дерева минимального порядка этой кучи

    def merge(self, other):
        if not self.head:
            return other
        if not other.head:
            return self

        dummy = BinTree(None)

        curH = dummy # слияние корневых списков 
        curH1 = self.head
        curH2 = other.head

        while curH1 and curH2:
            if curH1.degree <= curH2.degree:
                curH.sibling = curH1
                curH1 = curH1.sibling
            else:
                curH.sibling = curH2
                curH2 = curH2.sibling
            curH = curH.sibling
        
        curH.sibling = curH1 if curH1 else curH2

        curH = dummy.sibling  # первый реальный узел

        while curH and curH.sibling:
            next_node = curH.sibling
    
            if curH.degree == next_node.degree and curH.key <= next_node.key:
                curH.sibling = next_node.sibling
                next_node.parent = curH
                next_node.sibling = curH.child
                curH.child = next_node
                curH.degree += 1
            else:
                curH = curH.sibling

        new_heap = BinHeap() # результат слияния 
        new_heap.head = dummy.sibling
        return new_heap


    def insert(self, key, value=None):
        new_node = BinTree(key, value)

        temp_heap = BinHeap()
        temp_heap.head = new_node

        merged = self.merge(temp_heap)
        self.head = merged.head


    def getMinimum(self):
        if not self.head:
            return None
        
        min_node = self.head
        cur = self.head.sibling

        while cur:
            if cur.key < min_node.key:
                min_node = cur
            cur = cur.sibling

        return min_node.value if min_node.value is not None else min_node.key