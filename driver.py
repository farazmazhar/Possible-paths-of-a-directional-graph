'''
Created Date: Tuesday, May 8th 2018, 3:07:42 pm
Author: Faraz Mazhar
Email: csfarazmazhar@gmail.com
Github: github.com/farazmazhar
'''

from copy import deepcopy
from graph import Graph

def appendprint(values, value):
    '''This function prints when something is suppoed to be appended to values list'''
    values.append(value)

    str_to_print = ""
    for node_value in values:
        str_to_print += node_value + " -> "

    print(str_to_print.strip(" -> "))
    return values

def traverse_link(parent_node, path):
    '''This function will display paths'''
    if not parent_node.links:
        pass
    else:
        for node in parent_node.links:
            new_path = deepcopy(path)
            appendprint(new_path, node.value)
            traverse_link(node, new_path)

def find_paths():
    '''This function will traverse graph and will find all possible paths'''
    graph_obj = Graph()
    graph_obj.generate_graph('input')
    graph_obj.display_links()

    for node in graph_obj.nodes:
        path = [node.value]
        traverse_link(node, path)


def main():
    '''This is main'''
    find_paths()

if __name__ == '__main__':
    main()
