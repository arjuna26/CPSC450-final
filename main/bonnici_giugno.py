def bonnici_giugno_subgraph_isomorphism(G, H):
    """
    Checks if graph H is isomorphic to any subgraph of G using the RI algorithm.
    Args:
        G: The larger graph (NetworkX Graph object).
        H: The smaller graph (NetworkX Graph object).
    Returns:
        A mapping of nodes if an isomorphism exists, else None.
    """
    if len(H.nodes) > len(G.nodes) or len(H.nodes) == 0 or len(G.nodes) == 0:
        return {}

    def greatest_constraint_first(pattern_graph):
        """
        Orders the vertices of the pattern graph based on constraints.
        """
        ordered_vertices = []
        remaining_vertices = set(pattern_graph.nodes)
        start_vertex = max(remaining_vertices, key=lambda v: pattern_graph.degree[v])
        ordered_vertices.append(start_vertex)
        remaining_vertices.remove(start_vertex)
        while remaining_vertices:
            next_vertex = max(
                remaining_vertices,
                key=lambda v: (
                    sum(1 for u in ordered_vertices if (u, v) in pattern_graph.edges or (v, u) in pattern_graph.edges),
                    sum(1 for u in remaining_vertices if (v, u) in pattern_graph.edges or (u, v) in pattern_graph.edges),
                    pattern_graph.degree[v]
                )
            )
            ordered_vertices.append(next_vertex)
            remaining_vertices.remove(next_vertex)
        return ordered_vertices

    def match_recursive(ordered_pattern, mapping, matched_vertices):
        if len(mapping) == len(ordered_pattern):
            return mapping

        pattern_vertex = ordered_pattern[len(mapping)]
        candidates = [
            v for v in G.nodes if v not in matched_vertices and G.degree[v] >= H.degree[pattern_vertex]
        ]
        for candidate in candidates:
            is_compatible = all(
                (mapping[p_neighbor], candidate) in G.edges or (candidate, mapping[p_neighbor]) in G.edges
                for p_neighbor in H.neighbors(pattern_vertex)
                if p_neighbor in mapping
            )
            if is_compatible:
                mapping[pattern_vertex] = candidate
                matched_vertices.add(candidate)
                result = match_recursive(ordered_pattern, mapping, matched_vertices)
                if result is not None:
                    return result
                matched_vertices.remove(candidate)
                del mapping[pattern_vertex]
        return None

    ordered_pattern = greatest_constraint_first(H)
    return match_recursive(ordered_pattern, {}, set())
