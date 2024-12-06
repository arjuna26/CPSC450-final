import pytest
import time
import json
import networkx as nx
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bonnici_giugno import bonnici_giugno_subgraph_isomorphism
from naive_backtracking import naive_subgraph_isomorphism

RESULTS_FILE = "../performance_results.json"

@pytest.fixture(scope="function")
def setup_graphs():
    """
    Fixture to generate random graphs for testing.
    Returns a dictionary of graph pairs for each test configuration.
    """
    configurations = [(5, 0.5), (10, 0.5), (15, 0.5), (20, 0.5),
                     (10, 0.3), (10, 0.7), (15, 0.3), (15, 0.7)] 
    graphs = {}
    for size, density in configurations:
        G = nx.gnp_random_graph(size * 2, density)  
        H = nx.gnp_random_graph(size, density)      
        graphs[(size, density)] = (G, H)
    return graphs

@pytest.mark.parametrize("size, density", [(5, 0.5), (10, 0.5), (15, 0.5), (20, 0.5), 
                                           (10, 0.3), (10, 0.7), (15, 0.3), (15, 0.7)]) 
def test_ri_isomorphism(setup_graphs, size, density):
    """
    Time the RI subgraph isomorphism implementation.
    """
    G, H = setup_graphs[(size, density)]
    start = time.time()
    bonnici_giugno_subgraph_isomorphism(G, H)
    elapsed = time.time() - start

    result = {"algorithm": "ri", "size": size, "density": density, "time": elapsed}

    # Append the result to the JSON file
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            results = json.load(f)
    else:
        results = []

    results.append(result)

    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)

@pytest.mark.parametrize("size, density", [(5, 0.5), (10, 0.5), (15, 0.5), (20, 0.5),
                                           (10, 0.3), (10, 0.7), (15, 0.3), (15, 0.7)])
def test_naive_isomorphism(setup_graphs, size, density):
    """
    Time the naive subgraph isomorphism implementation.
    """
    G, H = setup_graphs[(size, density)]
    start = time.time()
    naive_subgraph_isomorphism(G, H)
    elapsed = time.time() - start

    result = {"algorithm": "naive", "size": size, "density": density, "time": elapsed}

    # Load previous results and append the new result
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            results = json.load(f)
    else:
        results = []

    results.append(result)

    # Save the updated results to the JSON file
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)
