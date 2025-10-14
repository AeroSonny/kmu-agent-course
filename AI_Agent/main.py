import os 
import sys
import json

# from agent.core import  
from agent.graph.nodes import *
from agent.graph import graph_maker

def run_graph(): 
    graph = graph_maker.run_graph()
    graph.run()
    return graph

if __name__ == "__main__":
    graph = run_graph()
    graph.invoke({'start': True})
    print("Graph run completed.")


    
