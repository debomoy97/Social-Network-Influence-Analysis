import csv
import os.path
from os import path
import sys
import math as m
import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
degreelist=[]
closenesslist=[]
betweennesslist=[]
pagernklist=[]
tic = time.perf_counter()
seed_node=[]

skip=5
def openFile(file,type,weight):
    global G,totalnnode,filename
    G=0
    filename=file.split("\\")
    #getting file name without extension
    filename=filename[1].split(".")
    da = open(file,"r")     # we are opening the dataset as da
    Graphtype=nx.DiGraph()
    # G is the graph object of networkx created based on the dataset
    if weight=="int":
        G = nx.parse_edgelist(da, comments='t',delimiter=type, create_using=Graphtype, nodetype=str, data=(('weight', int),))
    if weight=="float":
        G = nx.parse_edgelist(da, comments='t',delimiter=type, create_using=Graphtype, nodetype=str, data=(('weight', float),))  
    totalnnode=G.order()

def graph():  
    #getting file name without extension
    file=filename[0]
    name='framework\\plots\\'+file+'_graph.png'
     #we are drawing the graph
    if(path.exists(name)):
        result=name.split("\\")
        return result[1]+"\\"+result[2]
    else:
        print("in catch")
        nx.draw(G)
        plt.savefig(name)
        toc= time.perf_counter()
        print((toc-tic)/60)
        result=name.split("\\")
        return result[1]+"\\"+result[2]

def comparision_graph(x,y,y2,y_plot):
    #global x,y,y2,y_plot
    file=filename[0]
    name='framework\\plots\\'+file+'_comparision.png'
    fig1, ax1 = plt.subplots()
    plt.rc('grid', linestyle="-", color='black')
    ax1.plot(x,y,label='Second Influenced Nodes')
    ax1.plot(x,y_plot,color='green',label='Third Influenced Nodes')
    ax1.plot(x,y2,color='red',label='(Second+Third) Influenced Nodes')
    ax1.set_xlabel('Number of seed node from each method')
    ax1.set_ylabel('Influenced node')
    ax1.grid(True)
    ax1.legend()

    plt.savefig(name)
    #we are drawing the graph
    toc= time.perf_counter()
    print((toc-tic)/60)
    result=name.split("\\")
    #plt.show()
    return result[1]+"\\"+result[2]

def degree():
    tic = time.perf_counter()
    global degreelist
    file=filename[0]
    name="framework\\py_data\\"+file+"_degreelist.npy"
    if(path.exists(name)):
        degreelist=list(np.load(name))
    else:
        deg=nx.degree_centrality(G)
        sorted_deg = sorted(deg.items() , reverse=True, key=lambda x: x[1])
        degreelist=[x[0] for x in sorted_deg]
        np.save(name,degreelist)
    print("degreecentrality done")
    print(len(degreelist))
    toc = time.perf_counter()
    print(f"Elapsed time {(toc - tic)/60:0.4f} minutes")
    
def closeness():
    tic = time.perf_counter()
    global closenesslist
    file=filename[0]
    name="framework\\py_data\\"+file+"_closenesslist.npy"
    if(path.exists(name)):
        closenesslist=list(np.load(name))
    else:
        close=nx.closeness_centrality(G)
        sorted_close = sorted(close.items() , reverse=True, key=lambda x: x[1])
        closenesslist=[x[0] for x in sorted_close]
        np.save(name,closenesslist)
    print("closeness done")
    toc = time.perf_counter()
    print(f"Elapsed time {(toc - tic)/60:0.4f} minutes")

def betweeness():
    tic = time.perf_counter()
    global betweennesslist
    file=filename[0]
    name="framework\\py_data\\"+file+"_betweennesslist.npy"
    if(path.exists(name)):
        betweennesslist=list(np.load(name))
    else:
        between=nx.betweenness_centrality(G)
        sorted_between = sorted(between.items() , reverse=True, key=lambda x: x[1])
        betweennesslist=[x[0] for x in sorted_between]
        np.save(name,betweennesslist)
    print("betweeness done")
    toc = time.perf_counter()
    print(f"Elapsed time {(toc - tic)/60:0.4f} minutes")  

def pagerank():
    tic = time.perf_counter()
    global pagernklist
    file=filename[0]
    name="framework\\py_data\\"+file+"_pagernklist.npy"
    if(path.exists(name)):
        pagernklist=list(np.load(name))
    else:
        pagernk=nx.pagerank(G)
        sorted_pagernk = sorted(pagernk.items() , reverse=True, key=lambda x: x[1])
        pagernklist=[x[0] for x in sorted_pagernk]
        np.save(name,pagernklist)
    print("pagerank done")
    toc = time.perf_counter()
    print(f"Elapsed time {(toc - tic)/60:0.4f} minutes")

def infulential_node_function(seed_node):
    influencial_node_list=[]
    temp=[]
    for i in seed_node:
        # print(i)
        temp+=[user for user in G.neighbors(i)]
        #print(temp)
        influencial_node_list.append(temp)
    influencial_node_list=list(set(temp))
    return influencial_node_list

def methods(l):
    for x in l:
        if(x=="degree"):
            #print("degree called")
            degree()
        if(x=="closeness"):
            #print("closeness called")
            closeness()
        if(x=="betweeness"):
            #print("betweeness called")
            betweeness()
        if(x=="pagerank"):
            #print("pagerank called")
            pagerank()
    return ("done")
        

def top_seed_nodes(s):
    unique_seed_node_list=[]
    for i in range(s*3):
        if len(unique_seed_node_list)>=s:
            return unique_seed_node_list[:s]
        if len(degreelist)>0 and degreelist[i] not in unique_seed_node_list:
            unique_seed_node_list.append(degreelist[i])
        if len(closenesslist)>0 and closenesslist[i] not in unique_seed_node_list:
            unique_seed_node_list.append(closenesslist[i])
        if len(betweennesslist)>0 and betweennesslist[i] not in unique_seed_node_list:
            unique_seed_node_list.append(betweennesslist[i])
        if len(pagernklist)>0 and pagernklist[i] not in unique_seed_node_list:
            unique_seed_node_list.append(pagernklist[i])

def affected_nodes_values(val):
    #val = int(input("Enter the number nodes affected nodes :"))
    s = val
    result=["","","",""]
    unique_seed_node_list=top_seed_nodes(s)
    second_influencial_node_list=infulential_node_function(unique_seed_node_list)
    third_influencial_node_list=infulential_node_function(second_influencial_node_list)
    third_total=list(set(second_influencial_node_list+third_influencial_node_list))
    hop1 = ((len(second_influencial_node_list)/G.order())*100)
    hop2 = ((len(third_influencial_node_list)/G.order())*100)
    hop3 = ((len(third_total)/G.order())*100)
    print(len(second_influencial_node_list)," nodes affected in 1st hop and i.e. ",hop1,"%")
    print(len(third_influencial_node_list)," nodes affected in 2nd hop and i.e. ",hop3,"%")
    result[0]=len(second_influencial_node_list)
    result[1]=round(hop1,2)
    result[2]=len(third_total)
    result[3]=round(hop3,2)
    return result

def affected_nodes_percentage(val):
    #val = int(input("Enter the percentage you want to affect :"))
    c=0
    x=[]
    y=[]
    x_plot=[]
    y_plot=[]
    y2=[]
    result=["","","","","","",""]
    for s in range(1,totalnnode,skip):
        #print(totalnnode+skip)
        #total seed nodes from above methods
        unique_seed_node_list=top_seed_nodes(s)
        #to find unique seed nodes
        #print(unique_seed_node_list)
        second_influencial_node_list=infulential_node_function(unique_seed_node_list)
        #print(second_influencial_node_list)
        third_influencial_node_list=infulential_node_function(second_influencial_node_list)
        third_total=list(set(second_influencial_node_list+third_influencial_node_list))
        str1 = "percentage at 1st hop:"
        str2 = "percentage at 2nd hop:"
        hop1 = ((len(second_influencial_node_list)/G.order())*100)
        hop2 = ((len(third_influencial_node_list)/G.order())*100)
        hop3 = ((len(third_total)/G.order())*100)
        print(hop1,"% reached for ",s)
        x.append(s)
        y.append(len(second_influencial_node_list))
        y_plot.append(len(third_influencial_node_list))
        y2.append(len(third_total))
        text1=""
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""
        if(hop3>=val and c==0):
            c=1
            print("For ",s," affected nodes")
            print(str,hop1,"% reached")
            print(str2,hop3,"% reached")
            text1="For "+str(s)+" affected nodes:"
            text2= str1+str(round(hop1,2))+"% reached"
            text3=str2+str(round(hop3,2))+"% reached"
            result[0]=text1
            result[1]=text2
            result[2]=text3
        if(hop1>=val):
            print("For ",s," affected nodes")
            print(str,hop1,"% reached")
            print(str2,hop3,"% reached")
            text4="For "+str(s)+" affected nodes:"
            text5= str1+str(round(hop1,2))+"% reached"
            text6=str2+str(round(hop3,2))+"% reached"
            result[3]=text4
            result[4]=text5
            result[5]=text6
            result[6]=comparision_graph(x,y,y2,y_plot)
            print(result)
            return result
            
            
    



