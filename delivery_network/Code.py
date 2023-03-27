"""
Ici on code ; on met les fonctions (c'est comme graph.py du projet d'info)
"""
from collections import Counter
import matplotlib.pyplot as plt
import random
import networkx as nx #the networkX package helps us to manipulate graph

N=100
p=0.02
G = nx.erdos_renyi_graph(N, p)
currencies=[i for i in range(N)]

def iteration(n):
    for _ in range(n):
        agent= random.choice(list(G.nodes)) #choose a random agent
        neighbors = list(G.neighbors(agent)) #list of the agent's neighbors
        neighbors_currencies= [currencies[k] for k in neighbors]
        
        count=Counter(neighbors_currencies) #count the occurence of each currencies among the neihgbors
        m= count.most_common(1)[0][1]
        most_common_currencies = [k for k, v in count.items() if v == m]
        currencies[agent]=random.choice(most_common_currencies) #the agent adopts the most common currency among his neighbors (randomly if there are several...)
    return currencies

def colors_currencies(list):
    colors={}
    list_colors=[2 for _ in range(N)]
    for i in range (len(list)):
        if list[i] not in colors:
            colors[list[i]]=(random.random(), random.random(), random.random()) #the color is defined by a list of 3 elements
        list_colors[i]=colors[list[i]]
    return list_colors
    

currencies=iteration(100)
list_colors=colors_currencies(currencies)

nx.draw(G, with_labels=True, node_color=list_colors)
plt.show()

