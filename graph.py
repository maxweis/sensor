#!/bin/python2
import sys
import matplotlib.pyplot as plt

# arg_list = ["--diff", "--mean", "--help"]

def graph_diff(a_y, b_y):
    output_x = []
    output_y = []

    for n in range(len(a_y)):
        if a_y[n] > b_y[n]:
            output_y.append(a_y[n] - b_y[n])
        else:
            output_y.append(b_y[n] - a_y[n])
        output_x.append(n)

    return (output_x, output_y)


if len(sys.argv) == 2:
    try:
        graph_data_name = sys.argv[1]
        graph_data_file = open(graph_data_name, "r")
    except IOError:
        print "\nFile not available :", graph_data_name, "\n"
        exit()

    graph_data = graph_data_file.read().split()
    graph_data_file.close()

    x_values = map(int, graph_data[::2])
    y_values = map(int, graph_data[1::2])

    plt.plot(x_values, y_values, 'bo')

    plt.xlabel("samples")
    plt.ylabel("y")
    plt.suptitle("Graph of '" + graph_data_name + "'")
    plt.show()

if "--diff" in sys.argv:
    argv_index = sys.argv.index("--diff")
    try:
        graphA_data_name = sys.argv[argv_index + 1]
        graphA_data_file = open(graphA_data_name, "r")
    except IOError:
        print "\nFile not available :", graphA_data_name, "\n"
        exit()

    try:
        graphB_data_name = sys.argv[argv_index + 2]
        graphB_data_file = open(graphB_data_name, "r")
    except IOError:
        print "\nFile not available :", graphB_data_name, "\n"
        exit()

    graphA_data = graphA_data_file.read().split()
    graphA_data_file.close()

    graphB_data = graphB_data_file.read().split()
    graphB_data_file.close()

    graphA_y_values = map(int, graphA_data[1::2])

    graphB_y_values = map(int, graphB_data[1::2])

    output_graph = graph_diff(graphA_y_values, graphB_y_values)

    plt.plot(output_graph[0], output_graph[1], 'bo')

    plt.xlabel("samples")
    plt.ylabel("y")
    plt.suptitle("Differential Graph of '" + graphA_data_name + "' and '" + graphB_data_name + "'")
    plt.show()

if "--mean" in sys.argv:
    argv_index = sys.argv.index("--mean")
    graph_length = len(open(sys.argv[argv_index + 1], "r").read())
    graph_output = [0] * graph_length
    for n in range(len(sys.argv[argv_index + 1:])):
        try:
            graph_name = sys.argv[argv_index + n]
            graph_file = open(graph_name, "r")
            graph_data = graph_file.read().split()
        except IOError:
            print "\nFile not available :", graph_name, "\n"
            exit()

