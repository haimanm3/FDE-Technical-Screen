import unittest
from sort_packages import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_bulky(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 30), "REJECTED")

    def test_edge_case_bulky_volume(self):
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")  # Volume = 1,000,000

    def test_edge_case_bulky_dimension(self):
        self.assertEqual(sort(149, 149, 150, 19), "SPECIAL")

    def test_edge_case_heavy_mass(self):
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")

    def test_rejected_edge(self):
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

if __name__ == "__main__":
    unittest.main()
