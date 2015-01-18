from ADT.Graph.adj_list import Vertex, Graph

##################################
### Title: Graph node connection #
### Author: GuoChen Hou   ########
##################################

# Given a directed graph, design an algorithm to find out whether there is
# a route between two nodes.


def is_connected(adj_list, start, end):
    """
    Given a directed graph, Check if there is a route between two nodes.
    adj_list is the physical representation of the directed graph
    @return True if a route exists, False otherwise.

    """
    # use a depth first search traversal method to traverse the graph.
    if start_node is end_node:
        return True
    stack = []
    # INCOMPLETE


if __name__ == "__main__":
    graph = Graph()
    for i in range(6):
        graph.add_vertex(i)
    print graph.vert_list

    graph.add_edge(1, 2)
    graph.add_edge(1, 5)
    graph.add_edge(2, 1)
    graph.add_edge(2, 5)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    graph.add_edge(4, 3)
    graph.add_edge(4, 5)
    graph.add_edge(5, 1)
    graph.add_edge(5, 2)
    graph.add_edge(5, 4)
    for vertex in graph:
        for connected_vertices in vertex.get_connections():
            print "[%s, %s]" % (vertex.get_key(), connected_vertices.get_key())