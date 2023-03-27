"""
Ici on exécute le code (c'est le main.py du projet de programmation)
"""
#print("Salut à tous les amis c'est david lafarge pokemon")
from collections import Counter
import matplotlib.pyplot as plt
import random
import networkx as nx
from Code import iteration, colors_currencies

l=[1,4,4,3,5,5,4,2,3,1,5]
l.most_common

N=100 #number of agents
p=0.2 #link probability

'we use the Erdos Renyi model to generate a random graph'
G = nx.erdos_renyi_graph(N, p)#create a random graph
print(G)
nx.draw(G)
plt.show()
currencies=[i for i in range(N)]

currencies=iteration(1000)
list_colors=colors_currencies(currencies)

nx.draw(G, with_labels=True, node_color=list_colors)
plt.show()