import time
import networkx as nx
import matplotlib.pyplot as plt

from bonnici_giugno import bonnici_giugno_subgraph_isomorphism


def performance_test_varying_H_size():
    # Generate a fixed large graph G
    G = nx.erdos_renyi_graph(n=2000, p=0.3, seed=42)  # Larger random graph
    H_sizes = list(range(150, 200))  # Varying sizes of H (5, 7, 9, ..., 19)

    # Storage for runtime results
    bonnici_runtimes = []

    for size in H_sizes:
        # Generate smaller graph H with the specified size
        H = nx.path_graph(size)  # Path graph used for simplicity and control

        # Measure Bonnici-Giugno algorithm runtime
        start_time = time.time()
        bonnici_giugno_subgraph_isomorphism(G, H)
        bonnici_runtimes.append(time.time() - start_time)

    # Plotting results
    plt.figure(figsize=(14, 10))
    plt.plot(H_sizes, bonnici_runtimes, marker='o', linestyle='-', label='RI Algorithm')
    plt.xlabel('Size of Subgraph H')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Performance Comparison by Subgraph Size')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the test
performance_test_varying_H_size()