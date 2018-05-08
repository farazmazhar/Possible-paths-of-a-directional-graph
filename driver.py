from generate_graph import Graph

def main():
    graph = Graph()
    graph.generate_graph('input')
    graph.display_links()

if __name__ == '__main__':
    main()