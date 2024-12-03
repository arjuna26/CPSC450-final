import time
from naive_backtracking import naive_subgraph_isomorphism
# from bonnici_giugno import bonnici_giugno_algorithm
import networkx as nx

def measure_runtime(func, *args, **kwargs):
    """
    Measures the runtime of a function.
    Args:
        func: The function to measure.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    Returns:
        The runtime in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def benchmark(G, H):
    """
    Benchmarks the naive and Bonnici-Giugno algorithms on the same input.
    Args:
        G: The larger graph (NetworkX Graph object).
        H: The smaller graph (NetworkX Graph object).
    Returns:
        A tuple of runtimes (naive_runtime, bg_runtime).
    """
    naive_runtime = measure_runtime(naive_subgraph_isomorphism, G, H)
    # bg_runtime = measure_runtime(bonnici_giugno_algorithm, G, H)
    return naive_runtime, # bg_runtime

if __name__ == "__main__":
    # Example graphs
    G = nx.fast_gnp_random_graph(10, 0.5)  # Larger random graph
    H = nx.fast_gnp_random_graph(5, 0.5)   # Smaller random graph

    naive_time = benchmark(G, H)
    print(f"Naive Backtracking Runtime: {naive_time} seconds")
    # print(f"Bonnici-Giugno Runtime: {bg_time:.4f} seconds")
