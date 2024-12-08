import time
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from bonnici_giugno import bonnici_giugno_subgraph_isomorphism
from naive_backtracking import naive_subgraph_isomorphism

def generate_graph(graph_type, size, density=0.3):
    """Generate different types of graphs."""
    if graph_type == "random":
        return nx.erdos_renyi_graph(n=size, p=density, seed=None)
    elif graph_type == "grid":
        return nx.grid_2d_graph(int(np.sqrt(size)), int(np.sqrt(size)))
    elif graph_type == "complete":
        return nx.complete_graph(n=size)
    elif graph_type == "cycle":
        return nx.cycle_graph(n=size)
    elif graph_type == "path":
        return nx.path_graph(n=size)
    else:
        raise ValueError(f"Unknown graph type: {graph_type}")

def run_performance_tests():
    # Parameters for testing
    graph_sizes = [5, 10, 15, 20, 25, 30, 35, 40]  # Sizes of larger graphs
    subgraph_size = 5  # Fixed size for subgraphs
    graph_types = ["random", "grid", "complete", "cycle", "path"]  # Different graph types
    density = 0.4  # Probability of edge creation for random graphs
    num_trials = 3  # Number of trials for averaging runtime

    # Data storage
    results = {graph_type: {"naive": [], "bonnici": []} for graph_type in graph_types}

    # Run tests
    for graph_type in graph_types:
        print(f"Testing graph type: {graph_type}")
        for g_size in graph_sizes:
            naive_total_time = 0
            bonnici_total_time = 0

            for _ in range(num_trials):
                # Generate larger graph (G) and smaller subgraph (H)
                G = generate_graph(graph_type, g_size, density)
                H = generate_graph("random", subgraph_size, density)

                # Time the naive algorithm
                start = time.time()
                naive_subgraph_isomorphism(G, H)
                naive_total_time += time.time() - start

                # Time the Bonnici-Giugno algorithm
                start = time.time()
                bonnici_giugno_subgraph_isomorphism(G, H)
                bonnici_total_time += time.time() - start

            # Store average runtimes
            results[graph_type]["naive"].append(naive_total_time / num_trials)
            results[graph_type]["bonnici"].append(bonnici_total_time / num_trials)

            print(f"  G size: {g_size} -> Naive avg: {naive_total_time / num_trials:.2f}s, RI avg: {bonnici_total_time / num_trials:.2f}s")

    # Plot results
    plt.figure(figsize=(14, 8))
    for graph_type in graph_types:
        plt.plot(graph_sizes, results[graph_type]["naive"], '-o', label=f'{graph_type} (Naive)', linestyle='--')
        plt.plot(graph_sizes, results[graph_type]["bonnici"], '-o', label=f'{graph_type} (RI)', linestyle='-')
    
    plt.xlabel('Size of G (Larger Graph)')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Performance Comparison Across Graph Types')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    run_performance_tests()
