import json
import matplotlib.pyplot as plt
from collections import defaultdict
import os

RESULTS_FILE = "performance_results.json"

def load_results():
    """
    Load performance results from the JSON file.
    """
    results = defaultdict(lambda: defaultdict(list))
    with open(RESULTS_FILE, "r") as f:
        for entry in json.load(f):
            algorithm = entry["algorithm"]
            size = entry["size"]
            density = entry["density"]
            time = entry["time"]
            results[(size, density)][algorithm].append(time)
    return results

def plot_results(results):
    """
    Plot performance comparison between the naive and RI algorithms.
    """
    sizes = sorted(set(size for (size, density) in results.keys()))
    densities = sorted(set(density for (size, density) in results.keys()))

    for density in densities:
        naive_times = []
        ri_times = []
        for size in sizes:
            naive_avg = sum(results[(size, density)]["naive"]) / len(results[(size, density)]["naive"])
            ri_avg = sum(results[(size, density)]["ri"]) / len(results[(size, density)]["ri"])
            naive_times.append(naive_avg)
            ri_times.append(ri_avg)

        plt.figure()
        plt.plot(sizes, naive_times, marker="o", label="Naive")
        plt.plot(sizes, ri_times, marker="o", label="RI")
        plt.title(f"Performance Comparison (Density: {density})")
        plt.xlabel("Graph Size")
        plt.ylabel("Average Runtime (s)")
        plt.legend()
        plt.grid(True)

        # Save the figure with a proper directory structure for multiple density values
        if not os.path.exists("performance_plots"):
            os.makedirs("performance_plots")
        plt.savefig(f"performance_plots/performance_density_{density}.png")
        plt.show()

if __name__ == "__main__":
    results = load_results()
    plot_results(results)
