import csv
import sys
import math as m
import time
import networkx as nx
import matplotlib.pyplot as plt

da = open("base2.tsv","r")     # we are opening the dataset as da
Graphtype=nx.DiGraph()
G = nx.parse_edgelist(da, comments='t',delimiter=" ", create_using=Graphtype, nodetype=str, data=(('weight', int),))
totalnnode=G.order()
nx.draw(G)
plt.show()