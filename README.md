## All possible paths of directional graph
This program iterates a directional graph and displays all possible paths.

### Files
[graph.py](graph.py) contains data structures for Graph and its Node(s).
[driver.py](driver.py) contains logic to traverse a graph.
[input](input) contains nodes and edges to nodes.

#### Input file format
Input file instructions:
- A node must have an edge otherwise it will be ignored. 
- The file must follow 'x,y' convention. 
- Invalid input such as 'a,b,c', 'a', 'a,a' etc will be ignored. 
- Nodes that are self-joined will be ingored.

### Explanation
The algorithm does a depth first search. When a new node is found, it is appended to the path and the path is displayed. This happens till a node that can't traverse further is reached.

### Output of given [input](input):
```
Node value: a
Following are the links: 
a -> b
a -> c
-----------------------------
Node value: b
Following are the links: 
b -> c
b -> d
-----------------------------
Node value: c
Following are the links: 
This node has no further links.
-----------------------------
Node value: d
Following are the links: 
This node has no further links.
-----------------------------
Node value: x
Following are the links: 
x -> a
x -> b
-----------------------------
Node value: y
Following are the links: 
y -> x
-----------------------------
Node value: z
Following are the links: 
z -> b
-----------------------------
Node value: random_node
Following are the links: 
random_node -> b
-----------------------------
a -> b
a -> b -> c
a -> b -> d
a -> c
b -> c
b -> d
x -> a
x -> a -> b
x -> a -> b -> c
x -> a -> b -> d
x -> a -> c
x -> b
x -> b -> c
x -> b -> d
y -> x
y -> x -> a
y -> x -> a -> b
y -> x -> a -> b -> c
y -> x -> a -> b -> d
y -> x -> a -> c
y -> x -> b
y -> x -> b -> c
y -> x -> b -> d
z -> b
z -> b -> c
z -> b -> d
random_node -> b
random_node -> b -> c
random_node -> b -> d
```