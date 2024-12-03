import pytest
import networkx as nx
import os
import sys

# Add the parent directory to sys.path, import the algorithm to be tested
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from naive_backtracking import naive_subgraph_isomorphism

def test_simple_isomorphism():
    # Larger graph G
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    
    # Smaller graph H (subgraph of G)
    H = nx.Graph()
    H.add_edges_from([(1, 2), (2, 3)])
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())
    
def test_no_isomorphism():
    # Larger graph G
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])
    
    # Smaller graph H (not a subgraph of G)
    H = nx.Graph()
    H.add_edges_from([(1, 2), (2, 3), (3, 1)])
    
    # Expected: No isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is None
    
def test_identical_graphs():
    # Both graphs are identical
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1)])
    
    H = nx.Graph()
    H.add_edges_from([(1, 2), (2, 3), (3, 1)])
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert len(mapping) == len(H.nodes)
    
def test_partial_overlap():
    # Larger graph G
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
    
    # Smaller graph H (overlaps partially with G but is not isomorphic to any subgraph)
    H = nx.Graph()
    H.add_edges_from([(1, 2), (2, 3), (3, 1)])
    
    # Expected: No isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is None
    
def test_disconnected_subgraph():
    # Larger graph G
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (5, 6)])
    
    # Smaller graph H (disconnected subgraph of G)
    H = nx.Graph()
    H.add_edges_from([(1, 2), (5, 6)])
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())
    
def test_large_isomorphic_subgraph():
    # Larger graph G
    G = nx.fast_gnp_random_graph(20, 0.4, seed=42)  # Random graph with 20 nodes
    H = G.subgraph(list(G.nodes)[:10]).copy()  # Extract a subgraph with 10 nodes
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())