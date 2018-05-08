'''
Created Date: Tuesday, May 8th 2018, 2:25:23 pm
Author: Faraz Mazhar
Email: csfarazmazhar@gmail.com
Github: github.com/farazmazhar
'''

class Node:
    '''Data structure of a node'''
    def __init__(self, value):
        '''Initializing values'''
        self.value = value
        self.links = []

    def get_value(self):
        '''Returns value of a node'''
        return self.value

    def get_links(self):
        '''Returns links list'''
        return self.links

class Graph:
    '''Data structure of a graph'''
    def __init__(self):
        '''Initializing values'''
        self.nodes = []

    def generate_graph(self, filename):
        '''This function will take filename/file path and will generate a graph
        Assumed format:
            'a,b' means 'Node a' -> 'Node b'
        '''
        with open(filename, 'r') as file:
            links = file.readlines()

            nodes_values = []

            for link in links:
                values = link.strip().split(',')

                for node_value in values:
                    if node_value not in nodes_values:
                        nodes_values.append(node_value)
                        self.nodes.append(Node(node_value))

                lhs_index = 0
                rhs_index = 0
                for lhs_node in self.nodes:
                    if lhs_node.value == values[0]:
                        for rhs_node in self.nodes:
                            if rhs_node.value == values[1]:
                                self.nodes[lhs_index].links.append(self.nodes[rhs_index])
                            else:
                                rhs_index += 1
                    else:
                        lhs_index += 1

    def display_links(self):
        '''This function displays all the links;
        used for verification that all the nodes have proper links
        '''
        for node in self.nodes:
            print("Node value: " + node.value)
            print("Following are the links: ")

            if node.links:
                for link in node.links:
                    print(node.value + " -> " + link.value)
            else:
                print("This node has no further links.")

            print("-----------------------------")
