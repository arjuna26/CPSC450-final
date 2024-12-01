import networkx as nx

def naive_subgraph_isomorphism(G, H):
    """
    Checks if graph H is isomorphic to any subgraph of G using a naive backtracking approach.
    Args:
        G: The larger graph (NetworkX Graph object).
        H: The smaller graph (NetworkX Graph object).
    Returns:
        A mapping of nodes if an isomorphism exists, else None.
    """
    from itertools import permutations
    if len(H.nodes) > len(G.nodes):
        return None
    
    for mapping in permutations(G.nodes, len(H.nodes)):
        node_map = dict(zip(H.nodes, mapping))
        if all((node_map[u], node_map[v]) in G.edges for u, v in H.edges):
            return node_map
    return None
