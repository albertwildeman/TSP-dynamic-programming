from FileReadLib import get_data
from TspDynProgrLib import tsp_dyn_progr
from TspDynProgrLib import distances_from_coordinates

import os
import numpy as np

filename = "tsp"

test_version = True
n_cities_test = 3

npy_version_exists = os.path.isfile(filename + ".npy")
if not npy_version_exists:
    n_cities, city_coordinates = get_data(filename)
    distances = distances_from_coordinates(n_cities, city_coordinates)
    np.save(filename, distances)
else:
    distances = np.load(filename + ".npy")


if test_version:
    length_shortest_tour = tsp_dyn_progr(distances[:n_cities_test, :n_cities_test])
else:
    length_shortest_tour = tsp_dyn_progr(distances)

print("Length of solution to TSP for cities in file " + filename + ".txt: "
      + str(length_shortest_tour))

if test_version:
    print("Test version with small number of cities.")
