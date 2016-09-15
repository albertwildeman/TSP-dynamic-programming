from FileReadLib import get_data
from TspDynProgrLib import tsp_dyn_progr



filename = "tsp"
n_cities, city_coordinates = get_data(filename)

length_shortest_tour = tsp_dyn_progr(n_cities, city_coordinates)

print("Length of solution to TSP for cities in file " + filename + ".txt: "
      + str(length_shortest_tour))
