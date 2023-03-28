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

def simulation(n):
    U,utility_evolution= social_utility()
    for _ in range(n):
        agent= random.choice(list(G.nodes)) #choose a random agent
        neighbors = list(G.neighbors(agent)) #list of the agent's neighbors
        agent_utility=0
        if neighbors !=[]:
            neighbors_currencies= [currencies[k] for k in neighbors]
            count=Counter(neighbors_currencies) #count the occurence of each currency among the neihgbors
            m= count.most_common(1)[0][1]
            most_common_currencies = [k for k, v in count.items() if v == m]
            currencies[agent]=random.choice(most_common_currencies) #the agent adopts the most common currency among his neighbors (randomly if there are several...)
            
            for neighbor in neighbors:
                if currencies[neighbor]!=currencies[agent]:
                    agent_utility-=1 #agent utility= -card(neighbors that use a different currency)
        U[agent]=agent_utility
        utility_evolution.append(sum(U))
    return currencies,utility_evolution

def social_utility():
    U=[0]*N
    utility_evolution=[]
    for agent in range(N):
        neighbors= list(G.neighbors(agent))
        agent_utility=0
        for neighbor in neighbors:
            if currencies[neighbor]!=currencies[agent]:
                agent_utility-=1
        U[agent]=agent_utility
    return U,utility_evolution
             

def colors_currencies(list):
    colors={}
    list_colors=[0]*N #list with N zeros
    for i in range (len(list)):
        if list[i] not in colors:
            colors[list[i]]=(random.random(), random.random(), random.random()) #the color is defined by a list of 3 elements
        list_colors[i]=colors[list[i]]
    return list_colors
    

currencies,y=simulation(1000)
list_colors=colors_currencies(currencies)

nx.draw(G, with_labels=True, node_color=list_colors)
plt.show()
print(currencies)

plt.plot([i for i in range(1000)],y)
plt.show()
