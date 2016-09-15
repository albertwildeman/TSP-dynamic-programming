import itertools as it

def tsp_dyn_progr(n_cities, city_coordinates):


    a = [[] for x in range(5)]

    for subset_size in range(1, n_cities+1):

        # Determine number of subsets of the current size
        subsets = it.combinations(n_cities, subset_size)

        # For each possible subset, determine the length of the shortest path
        for subset in subsets:
            a[]





    return len_shortest_path