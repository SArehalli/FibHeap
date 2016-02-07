import math
import random

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.marked = False
    def __repr__(self):
        return str(self.value) + ": " + str(self.children) 

class FibHeap(object):
    def __init__(self):
        self.forest = []
        self.min_index = -1
    
    def find_min(self):
        if self.min_index != -1:
            return self.forest[self.min_index].value
        return None

    def insert(self, value):
        self.forest.append(Node(value))

        # Update min
        if self.min_index == -1 or self.forest[self.min_index].value > value:
            self.min_index = len(self.forest) - 1

    def extract_min(self):
        # Remove min and make it's children roots
        if self.min_index == -1:
            return None

        min_node = self.forest.pop(self.min_index)
        for child in min_node.children:
            self.forest.append(child)

        # Consolidate trees of equal degree
        # Keep minimum items as root
        degree_table = {}
        for root in self.forest:
            while len(root.children) in degree_table:
                o_root = degree_table[len(root.children)]
                degree_table.pop(len(root.children), None)
                if root.value > o_root.value:
                    root, o_root = o_root, root
                root.children.append(o_root)
            degree_table[len(root.children)] = root

        # Rebuild root forest
        self.forest = []
        self.min_index = -1;
        min_value = None
        for index, (degree, node) in enumerate(degree_table.items()):
            self.forest.append(node)
            if min_value == None or min_value > node.value:
                min_value = node.value
                self.min_index = index
        return min_node.value


# SUPER-basic test for this implementation
if __name__ == "__main__":
    for i in range(1000):
        pq = FibHeap()
        a = [random.randint(1, 100) for x in range(1000)]
        list(map(pq.insert, a))
        a.sort()
        b = [pq.extract_min() for x in range(1000)]

        if a != b:
            print("failed")

