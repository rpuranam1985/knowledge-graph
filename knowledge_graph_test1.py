import networkx as nx
import matplotlib.pyplot as plt

def create_banking_knowledge_graph():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes representing entities
    G.add_node("Customer A", type="Customer")
    G.add_node("Customer B", type="Customer")
    G.add_node("Bank", type="Bank")
    G.add_node("Account 1", type="Account")
    G.add_node("Account 2", type="Account")
    G.add_node("Loan", type="Loan")

    # Add relationships (edges) between entities
    G.add_edge("Customer A", "Bank", relationship="is a client of")
    G.add_edge("Customer B", "Bank", relationship="is a client of")
    G.add_edge("Customer A", "Account 1", relationship="owns")
    G.add_edge("Customer B", "Account 2", relationship="owns")
    G.add_edge("Account 1", "Loan", relationship="linked to")
    G.add_edge("Bank", "Loan", relationship="provides")

    return G

def visualize_graph(G):
    # Get node labels
    labels = nx.get_edge_attributes(G, "relationship")

    # Draw the graph
    pos = nx.spring_layout(G)  # Position nodes using the spring layout
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, font_size=10, font_color="black")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")

    # Show the graph
    plt.title("Banking Knowledge Graph")
    plt.show()

if __name__ == "__main__":
    # Create and visualize the graph
    graph = create_banking_knowledge_graph()
    visualize_graph(graph)
