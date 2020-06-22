# retweet graph building

import networkx as nx
import pandas as pd
from utils import *
import dynetx as dn
from dynetx.readwrite import json_graph
import json

# how to load from server?
df = pd.read_csv("") # here we should read raw data
df.set_index('time_jalali', inplace=True)
df = df.sort_values(by='time_jalali')

nodes_texts = nodes_texts(data)

def dynamic_retweet_graph_maker(data,nodes_texts, graph=None):
    # retweet dynamic directed graph initialization
    if graph is None:
        graph = dn.DynDiGraph()
    # add nodes and their attributes to the graph
    for item in list(nodes_texts.keys()):
        graph.add_node(key, text=nodes_texts[item])
    # adding weights to 'graph'
    heads = []
    tails = []
    for i in range(len(data)):
        heads.append(data.iloc[i]['mentionField'])
        tails.append(data.iloc[i]['ownerName'])
    for i in range(len(heads)):
        if graph.has_edge(tails[i], heads[i]):
            graph[tails[i]][heads[i]]['weight'] += 1
        else:
            graph.add_edges_from([[tails[i], heads[i]]], weight=1)
    # adding interactions to 'graph'
    for i in range(len(df)):
        if df.iloc[i]['mentionField'] != '""':
            graph.add_interaction(u=df.iloc[i]['ownerName'],
                                  v=df.iloc[i]['mentionField'],
                                  t=df.iloc[i]['timestamp'])
    return graph


def node_texts(data):
    attributes = {}
    for i in range(len(data)):
        key = data.iloc[i]['ownerName']
        if key in attributes:
            attributes[key].append(data.iloc[i]['textField'])
        elif key not in attributes:
            attributes[key] = [data.iloc[i]['textField']]
    return attributes


