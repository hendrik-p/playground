import numpy as np
import networkx as nx

def calculate_cost(G, path):
    cost = 0
    for i in range(1, len(path)):
        prev = path[i - 1]
        current = path[i]
        w = G[prev][current]['weight']
        cost += w
    return cost

if __name__ == '__main__':
    # create DAG
    nb_layers = 5
    nb_nodes_per_layer = 5
    source = -1
    sink = nb_layers * nb_nodes_per_layer
    nodes = [source] + list(range(nb_layers * nb_nodes_per_layer)) + [sink]
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    # edges between source and first layer
    for i in range(nb_nodes_per_layer):
        G.add_edge(source, i, weight=0, label='')
    # edges between last layer and sink
    for i in range(nb_nodes_per_layer):
        j = (nb_layers - 1) * nb_nodes_per_layer + i
        G.add_edge(j, sink, weight=0, label='')
    # edges between layers
    for i in range(1, nb_layers):
        for j in range(nb_nodes_per_layer):
            current = i * nb_nodes_per_layer + j
            weights = np.random.rand(nb_nodes_per_layer)
            weights /= np.sum(weights) # random weights that sum to one
            weights = -np.log(weights) # negative log probabilities
            for k in range(nb_nodes_per_layer):
                prev = (i - 1) * nb_nodes_per_layer + k
                w = weights[k]
                label = '%0.2f' % np.exp(-w)
                G.add_edge(prev, current, weight=w, label=label)

    # draw graph
    nx.drawing.nx_pydot.write_dot(G, 'graph.dot')

    # find shortest paths
    for path in nx.shortest_simple_paths(G, source, sink, weight='weight'):
        cost = calculate_cost(G, path)
        print(path, cost)

