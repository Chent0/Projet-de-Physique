"""
Ici on code ; on met les fonctions (c'est comme graph.py du projet d'info)
"""
from collections import Counter
import matplotlib.pyplot as plt
import random
import networkx as nx #the networkX package helps us to manipulate graph

N=10 #number of agents
p=0.2 #link probability

'we use the Erdos Renyi model to generate a random graph'
G = nx.erdos_renyi_graph(N, p)#create a random graph
print(G)
nx.draw(G)
plt.show()

currencies=[i for i in range(N)]

def iteration():
    agent= random.choice(list(G.nodes)) #choose a random agent
    neighbors = list(G.neighbors(agent)) #list of the agent's neighbors
    neighbors_currencies= [currencies[k] for k in neighbors]
    
    count=Counter(neighbors_currencies) #count the occurence of each currencies among the neihgbors
    m= count.most_common(1)[0][1]
    most_common_currencies = [k for k, v in count.items() if v == m]
    currencies[agent]=random.choice(most_common_currencies) #the agent adopts the most common currency among his neighbors (randomly if there are several...)

    


