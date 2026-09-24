# Agent Deployment using LangSmith Studio

### Step-1:
Install the following packages using uv.
[Guide](https://docs.langchain.com/langsmith/quick-start-studio)
```
1. langgraph
2. langgraph-cli[inmem]
3. langsmith
```

### Step-2:
Create a JSON file named langgraph.json in your project and paste the following congifuration in it.

```
{
  "dockerfile_lines": [],
  "graphs": {
    "simple_graph": "./simple.py:graph"
  },
  "env": "./.env",
  "python_version": "3.14",
  "dependencies": [
    "."
  ]
}
```
Change the name ```simple.py``` with your_agent file. you may also add more agents using ``` graphs: {}``` in JSON file.




### Step-3:
Create your LangGraph agent using (.py) file.
```
import random 
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    graph_state: str

# Conditional edge
def decide_mood(state) -> Literal["node_2", "node_3"]:
    
    # Often, we will use state to decide on the next node to visit
    user_input = state['graph_state'] 
    
    # Here, let's just do a 50 / 50 split between nodes 2, 3
    if random.random() < 0.5:

        # 50% of the time, we return Node 2
        return "node_2"
    
    # 50% of the time, we return Node 3
    return "node_3"

# Nodes
def node_1(state):
    print("---Node 1---")
    return {"graph_state":state['graph_state'] +" I am"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state":state['graph_state'] +" happy!"}

def node_3(state):
    print("---Node 3---")
    return {"graph_state":state['graph_state'] +" sad!"}

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Compile graph
graph = builder.compile()
```
### Step-4:
Deploy your agent by running the following command:
```
langgraph dev
```