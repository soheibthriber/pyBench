import time
import psutil
import threading
import multiprocessing
import asyncio
import gevent
import matplotlib.pyplot as plt


class Benchmark:
    def __init__(self, scenario, num_runs):
        self.scenario = scenario
        self.num_runs = num_runs
        self.results = {'cpu': [], 'mem': [], 'disk_io': [], 'net_io': [], 'response_time': []}

    def measure_cpu(self):
        return psutil.cpu_percent()

    def measure_memory(self):
        return psutil.virtual_memory().percent

    def measure_disk_io(self):
        return psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes

    def measure_net_io(self):
        return psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent

    def measure_response_time(self):
        # Placeholder for measuring response time
        return 0

    def run_scenario(self):
        # Placeholder for running scenario
        pass

    def run_benchmark(self, concurrency_model):
        for i in range(self.num_runs):
            # Create a new process, thread, coroutine, or greenlet depending on the concurrency model
            if concurrency_model == 'threading':
                t = threading.Thread(target=self.run_scenario)
                t.start()
                t.join()
            elif concurrency_model == 'multiprocessing':
                p = multiprocessing.Process(target=self.run_scenario)
                p.start()
                p.join()
            elif concurrency_model == 'asyncio':
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.run_scenario())
            elif concurrency_model == 'gevent':
                gevent.spawn(self.run_scenario).join()

            # Measure performance metrics
            cpu_usage = self.measure_cpu()
            mem_usage = self.measure_memory()
            disk_io = self.measure_disk_io()
            net_io = self.measure_net_io()
            response_time = self.measure_response_time()

            # Store results
            self.results['cpu'].append(cpu_usage)
            self.results['mem'].append(mem_usage)
            self.results['disk_io'].append(disk_io)
            self.results['net_io'].append(net_io)
            self.results['response_time'].append(response_time)

    def plot_results(self):
        # Plot results using Matplotlib
        fig, axs = plt.subplots(2, 3, figsize=(10, 6))
        axs[0, 0].plot(self.results['cpu'])
        axs[0, 0].set_title('CPU Usage')
        axs[0, 1].plot(self.results['mem'])
        axs[0, 1].set_title('Memory Usage')
        axs[0, 2].plot(self.results['disk_io'])
        axs[0, 2].set_title('Disk I/O')
        axs[1, 0].plot(self.results['net_io'])
        axs[1, 0].set_title('Network I/O')
        axs[1, 1].plot(self.results['response_time'])
        axs[1, 1].set_title('Response Time')
        plt.tight_layout()
        plt.show()
