import networkx as nx
import random as rand
import matplotlib.pyplot as plt


def generate_rand_graph(number_of_vertices):
    generated_graph = nx.Graph()
    # generating an edge between each random number
    for i in range(0, int(number_of_vertices)):
        key = rand.randrange(0, number_of_vertices)
        value = rand.randrange(0, number_of_vertices)
        generated_graph.add_edges_from([(key, value)])
    return generated_graph


def main():
    while True:
        vert_count = int(input("Enter number of vertices: "))
        graph = generate_rand_graph(vert_count)
        nx.draw(graph)
        plt.savefig("generated_graph.png")
        plt.show()
        check_running = input("Make Another? ")
        if check_running[0].upper() != 'Y':
            print("Quitting...")
            return


main()
