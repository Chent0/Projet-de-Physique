"""
Ici on exécute le code (c'est le main.py du projet de programmation)
"""
#print("Salut à tous les amis c'est david lafarge pokemon")
from collections import Counter
import matplotlib.pyplot as plt
import random
import networkx as nx
from code import colors_currencies

N=100 #number of agents
p=0.02 #link probability

'we use the Erdos Renyi model to generate a random graph'
G = nx.erdos_renyi_graph(N, p)#create a random graph
print(G)
nx.draw(G)
plt.show()
currencies=[i for i in range(N)]

currencies=simulation(1000)
list_colors=colors_currencies(currencies)

nx.draw(G, with_labels=True, node_color=list_colors)
plt.show()