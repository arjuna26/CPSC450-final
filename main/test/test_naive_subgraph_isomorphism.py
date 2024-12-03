import pytest
import networkx as nx
import os
import sys

# Add the parent directory to sys.path, import the algorithm to be tested
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from naive_backtracking import naive_subgraph_isomorphism

def test_empty_graphs():
    # Both G and H are empty
    G = nx.Graph()
    H = nx.Graph()

    # Expected: Trivial isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping == {}

def test_empty_subgraph():
    # G is non-empty, H is empty
    G = nx.cycle_graph(5)
    H = nx.Graph()

    # Expected: Trivial isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping == {}

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

def test_single_node_subgraph():
    # G has multiple nodes, H has one node
    G = nx.cycle_graph(5)
    H = nx.Graph()
    H.add_node(0)

    # Expected: Isomorphism exists (any single node in G)
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert len(mapping) == 1
    assert 0 in mapping
    assert mapping[0] in G.nodes
    
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
    
def test_multiple_possible_mappings():
    # Larger graph G
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 1),  # Square
        (5, 6), (6, 7), (7, 5)           # Triangle
    ])
    
    # Smaller graph H (triangle subgraph)
    H = nx.Graph()
    H.add_edges_from([(1, 2), (2, 3), (3, 1)])
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())

def test_disconnected_large_graph():
    # Larger graph G with disconnected components
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 1),  # Square
        (5, 6), (6, 7), (7, 8), (8, 5),  # Another square
        (9, 10)                          # Single edge
    ])
    
    # Smaller graph H (another square)
    H = nx.Graph()
    H.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())

def test_large_complete_graph():
    # Larger graph G
    G = nx.complete_graph(20)  # Fully connected graph with 20 nodes
    
    # Smaller graph H (fully connected graph with 5 nodes)
    H = nx.complete_graph(5)
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())
    
def test_no_matching_edges():
    # G and H have the same number of nodes but no shared edge structures
    G = nx.path_graph(6)  # A line graph
    H = nx.Graph()
    H.add_edges_from([(0, 1), (1, 2), (2, 0)])  # A triangle

    # Expected: No isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is None

def test_large_disjoint_graphs():
    # G is a large disjoint graph with multiple components
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3),  # Line graph component
        (4, 5), (5, 6), (6, 4),  # Triangle component
        (7, 8), (8, 9), (9, 7), (7, 10)  # A triangle with a tail
    ])
    
    # H is a triangle
    H = nx.Graph()
    H.add_edges_from([(0, 1), (1, 2), (2, 0)])

    # Expected: Isomorphism exists for the triangle in G
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())

def test_isomorphic_to_self():
    # G and H are identical
    G = nx.complete_graph(7)
    H = nx.complete_graph(7)

    # Expected: Isomorphism exists (identity mapping)
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert mapping == {u: u for u in H.nodes}
    
def test_partial_graph_isomorphism():
    # G is a graph, H is a part of G
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),  # Path component
        (7, 8), (8, 9), (9, 7)                  # Triangle component
    ])
    
    # H matches part of the path in G
    H = nx.Graph()
    H.add_edges_from([(0, 1), (1, 2)])  # A smaller path
    
    # Expected: Isomorphism exists
    mapping = naive_subgraph_isomorphism(G, H)
    assert mapping is not None
    assert set(H.nodes) == set(mapping.keys())
    assert set(G.nodes).issuperset(mapping.values())
    
    
# def test_large_non_isomorphic_subgraph():
#     # Larger graph G
#     G = nx.fast_gnp_random_graph(15, 0.4, seed=42)  # Random graph with 20 nodes
    
#     # Smaller graph H (not a subgraph of G)
#     H = nx.complete_graph(10)  # A fully connected graph with 10 nodes
    
#     # Expected: No isomorphism exists
#     mapping = naive_subgraph_isomorphism(G, H)
#     assert mapping is None
