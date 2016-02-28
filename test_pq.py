import unittest
import random
from pq import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def pq_sort(self, test_array):
        pq = PriorityQueue()

        for x in test_array:
            pq.insert(x)

        pq_size = pq.size()
        return [pq.extract_min() for x in range(pq_size)]

    def test_repetition(self):
        test_case = list(range(100)) + [1]
        self.assertEqual(sorted(test_case), self.pq_sort(test_case))

    def test_randomized(self):
        for i in range(100):
            test_case = [random.randint(0, 100) for i in range(100)]
            self.assertEqual(sorted(test_case), self.pq_sort(test_case))

    def test_size_initial(self):
        pq = PriorityQueue()
        self.assertEqual(pq.size(), 0)

    def test_size_insert(self):
        pq = PriorityQueue()
        for i in range(100):
            self.assertEqual(pq.size(), i)
            pq.insert(i)

    def test_size_remove(self):
        pq = PriorityQueue()

        for i in range(100):
            pq.insert(i)

        for i in range(100):
            pq.extract_min()

        self.assertEqual(pq.size(), 0)

    def test_empty_extract(self):
        pq = PriorityQueue()

        self.assertEqual(pq.extract_min(), None)

    def test_empty_peek(self):
        pq = PriorityQueue()

        self.assertEqual(pq.find_min(), None)


if __name__ == "__main__":
    unittest.main()
