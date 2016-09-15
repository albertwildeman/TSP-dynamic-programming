import itertools as it
import numpy as np

def tsp_dyn_progr(distances):

    n_cities = distances.shape[0]

    # Initialize the list a[subset_size][i_subset][j] which will hold, for each possible subset of nodes
    # (all including node 0), the length of the shortest path from node 0 to node j, including all nodes
    # in the subset exactly once in between node 0 and node j.
    # a = [[] for x in range(2**n_cities)]
    a = [None] * (2**n_cities)


    # Initialize a
    # For the empty subset (with only node 0), the distance form node 0 to itself is 0
    a[0] = np.zeros(1, dtype=float)
    # For subsets with a single node in addition to node 0, the distance is the distance between it and node 0
    subset_size = 1
    subsets = it.combinations(range(1, n_cities), subset_size)
    for subset in subsets:

        # get index of element in a for this subset
        i_subset = idx(subset)

        # initialize a for this subset (one entry for each j)
        a[i_subset] = np.ones(subset_size, dtype=float) * np.inf

        # For each city j in the subset, determine a[i_subset, j]
        for i_j, j in enumerate(subset):
            # Determine the index in a of the subset equal to the current one, minus city j
            a[i_subset][i_j] = distances[0,j]

    for subset_size in range(2, n_cities):

        print("Working on subsets of size " + str(subset_size))
        # Determine number of subsets of the current size
        subsets = it.combinations(range(1,n_cities), subset_size)

        # For each possible subset, determine the length of the shortest path
        for subset in subsets:

            # get index of element in a for this subset
            i_subset = idx(subset)

            # initialize a for this subset (one entry for each j)
            a[i_subset] = np.ones(subset_size, dtype=float) * np.inf

            # For each city j in the subset, determine a[i_subset, j]
            for i_j, j in enumerate(subset):

                # Determine the index in a of the subset equal to the current one, minus city j
                i_subset_without_j = idx(subset, [j])

                #
                options = [a[i_subset_without_j][i_k] + distances[subset(i_k), j] for i_k in range(subset_size) if i_k != i_j]
                a[i_subset][i_j] = min(options + [np.inf])

    # Determine the shortest tour length, similarly to the last step in the loop above but now to return
    # back to city # 1
    options = [a[-1][k] + dist[k, 0] for k in range(1,n_cities)]
    len_shortest_path = min(options + [np.inf])

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
