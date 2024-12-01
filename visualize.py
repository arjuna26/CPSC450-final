import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G, subgraph_mapping=None):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=700, font_size=10)
    if subgraph_mapping:
        sub_nodes = list(subgraph_mapping.values())
        nx.draw_networkx_nodes(G, pos, nodelist=sub_nodes, node_color="green")
    plt.show()
    
if __name__ == "__main__":
    G = nx.fast_gnp_random_graph(100, 0.5)  # Large random graph
    
    visualize_graph(G)
