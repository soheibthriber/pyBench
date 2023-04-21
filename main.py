from benchmark import Benchmark


def start_benchmark():
    # Initialize benchmark with scenario and number of runs
    benchmark = Benchmark(scenario='My Scenario', num_runs=10)

    # Run benchmark using different concurrency models
    benchmark.run_benchmark(concurrency_model='threading')
    benchmark.run_benchmark(concurrency_model='multiprocessing')
    benchmark.run_benchmark(concurrency_model='asyncio')
    benchmark.run_benchmark(concurrency_model='gevent')

    # Plot results
    benchmark.plot_results()


if __name__ == '__main__':
    start_benchmark()
