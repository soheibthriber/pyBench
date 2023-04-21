import unittest
from benchmark import Benchmark
import psutil


class TestBenchmark(unittest.TestCase):
    def setUp(self):
        self.benchmark = Benchmark('test_scenario', 1)

    def test_measure_cpu(self):
        cpu_usage = self.benchmark.measure_cpu()
        self.assertGreaterEqual(cpu_usage, 0)
        self.assertLessEqual(cpu_usage, 100)
