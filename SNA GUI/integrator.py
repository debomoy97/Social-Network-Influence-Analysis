import eel
import sys
sys.path.insert(0, 'framework\\')

import sna

my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 9999,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.init("framework")

@eel.expose
def open(file,type,weight):
    file="dataset\\"+file
    sna.openFile(file,type,weight)
@eel.expose
def pic():
    result=sna.graph()
    eel.pic_return(result)

@eel.expose    
def method(lm):
    print(lm)
    temp=sna.methods(lm)
    msg="Now you can procced further"
    eel.select_function_return(msg)

@eel.expose
def top_seed_node(val):
    result=sna.top_seed_nodes(int(val))
    s="The top "+str(val) +" are "
    for i in range(0,len(result)-1):
        s=s+str(result[i])+","
    s=s+str(result[-1])+"."
    eel.top_seed_nodes_return(s)

@eel.expose
def affected_nodes_value(val):
    temp=["",""]
    result=sna.affected_nodes_values(int(val))
    s1=""+str(result[0])+" nodes affected in 1st hop and i.e. " +str(result[1])+"%"
    s2=""+str(result[2])+" nodes affected in 2st hop and i.e. " +str(result[3])+"%"
    temp[0]=s1
    temp[1]=s2
    eel.affected_nodes_values_return(temp)

@eel.expose
def affected_node_percentage(val):
    result=sna.affected_nodes_percentage(int(val))
    eel.affected_nodes_percentage_return(result)

eel.start("index.html",option=my_options)
