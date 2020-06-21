# retweet graph building

import networkx as nx

def graph_maker(heads, tails, graph=None):
    # graph initiate
    if graph is None:
        graph = nx.DiGraph()
    for i in range(len(heads)):
        if graph.has_edge(tails[i], heads[i]):
            graph[tails[i]][heads[i]]['weight'] += 1
        else:
            graph.add_edges_from([[tails[i], heads[i]]], weight=1)
    return graph


def static_retweet_graph(data, graph=None):
    heads = []
    tails = []
    for i in range(len(data)):
        heads.append(data.iloc[i]['mentionField'])
        tails.append(data.iloc[i]['ownerName'])
    return graph_maker(heads, tails, graph)

# how to load from server?
data = pd.read_csv("")