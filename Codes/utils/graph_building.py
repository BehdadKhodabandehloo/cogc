# retweet graph building

import networkx as nx
import pandas as pd
from utils import *

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
df = pd.read_csv("") # here we should read raw data
df.set_index('time_jalali', inplace=True)
df = df.sort_values(by='time_jalali')

nodes_texts = nodes_texts(data)
def dynamic_retweet_graph(data, nodes_texts, graph=None):
    # dynamic graph initialization
    graph = dn.DynDiGraph()
    # add nodes and their attributes to the graph
    for item in nodes_texts.keys():
        graph.add_node(key, text=nodes_texts[item])

    heads = []
    tails = []
    timestamps = []
    texts = []

    


    return snapshots

