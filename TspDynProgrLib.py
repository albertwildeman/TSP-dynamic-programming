import itertools as it
import numpy as np

def tsp_dyn_progr(n_cities, city_coordinates):

    # Construct the matrix of distances between any pair of cities
    dist = distances_from_coordinates(n_cities, city_coordinates)

    # Initialize the list a[subset_size][i_subset][j] which will hold, for each possible subset of nodes
    # (all including node 0), the length of the shortest path from node 0 to node j, including all nodes
    # in the subset exactly once in between node 0 and node j.
    a = [ np.ones()*np.inf for x in range(2**n_cities)]

    for subset_size in range(1, n_cities+1):

        # Determine number of subsets of the current size
        subsets = it.combinations(range(n_cities), subset_size)

        # For each possible subset, determine the length of the shortest path
        for subset in subsets:

            # get index of element in a for this subset
            i_subset = idx(subset)

            # For each city in the subset, determine a[i_subset, j]
            for j in subset:

                # Determine the index in a of the subset equal to the current one, minus city j
                i_subset_without_j = idx(subset, [j])

                options = [a[i_subset_without_j][k] + dist[k, j] for k in subset  if k != j]
                a[i_subset][j] = min(options + [np.inf])

    len_shortest_path = 777777777
    return len_shortest_path


def distances_from_coordinates(n_cities, coord):
    # Calculates the (Euclidian) distance between two cities
    distances = np.zeros((n_cities, n_cities), dtype=float)

    # For every pair of cities i and j, get the distance
    distances = np.array( [[
                               ((coord[i, 0] - coord[j, 0]) ** 2 +
                                (coord[i, 1] - coord[j, 1]) ** 2) ** 0.5
                                for j in range(n_cities)] for i in range(n_cities)])
    return distances


def idx(subset, excluded=[]):

    # Returns the 1-dimensional index of a subset or arbitrary size, excluding elements listed in without
    index = 0

    # Index has 1 bit for each node. If the node is present in the subset, turn on the corresponding bit.
    subset_after_deletion = [i for i in subset if i not in excluded]
    for i in subset_after_deletion:
        index += 1 << i

    return index
