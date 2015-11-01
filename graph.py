#!/bin/python2

import sys
import matplotlib.pyplot as plt

def read_file(path, error="\nFile not available: "):
    error += path
    try:
        with open(path, "r") as open_file:
            return open_file.read()
    except IOError:
        print(error)
        exit()


def unpack_coords(text):
    data = text.split()
    x_values = map(int, data[::2])
    y_values = map(int, data[1::2])
    return (x_values, y_values)


def data_mean(data):
    total = 0
    n=0
    for n in data:
        total += n
    if n != 0:
        return total / float(n)


def graph_diff(y1, y2):
    output_x = []
    output_y = []
    if len(y1) > len(y2):
        max_data = y1
        min_data = y2
    else:
        max_data = y2
        min_data = y1

    if len(max_data) != len(min_data):
        del max_data[len(min_data):]

    high_data = max(min_data, max_data)
    low_data = min(min_data, max_data)

    for n in range(len(min_data)):
        output_y.append(high_data[n] - low_data[n])
        output_x.append(n)
    return (output_x, output_y)


help_message = """
Graph Tool for Sensor Data
Integers must be stored in text files separated by whitespace (x,y)

Arguments:
(none) file           Graph data from file
--graph file          Graph data from file
--diff file1 file2    Graph the difference of two data sets stored in files
--mean file           Return mean of x and y values of 
"""

if __name__ == "__main__":
    for arg_n, arg in enumerate(sys.argv[1:]):
        if arg == "--help":
            print(help_message)

        if arg == "--diff":
            dataA = unpack_coords(read_file(sys.argv[arg_n + 2]))
            dataB = unpack_coords(read_file(sys.argv[arg_n + 3]))
            output_graph = graph_diff(dataA[1], dataB[1])
            plt.plot(output_graph[0], output_graph[1], 'bo')
            plt.xlabel("samples")
            plt.ylabel("y")
            plt.suptitle("Differential graph of '{0}' and '{1}'".format(
                sys.argv[arg_n + 1], sys.argv[arg_n + 2]))
            plt.show()

        if  arg == "--mean":
            data = unpack_coords(read_file(sys.argv[arg_n + 2]))
            print("x average: {0}\ny average: {1}".format(
                data_mean(data[0]), data_mean(data[1])))

        if arg == "--graph":
            data = unpack_coords(read_file(sys.argv[arg_n + 2]))
            plt.plot(data[0], data[1], 'bo')
            plt.xlabel("samples")
            plt.ylabel("y")
            plt.suptitle("Graph of '{0}'".format(sys.argv[arg_n + 2]))
            plt.show()

        elif len(sys.argv) == 2:
            data = unpack_coords(read_file(arg))
            plt.plot(data[0], data[1], 'bo')
            plt.xlabel("samples")
            plt.ylabel("y")
            plt.suptitle("Graph of '{0}'".format(arg))
            plt.show()
