import os
import numpy as np


def get_data(filename):

    filepath = os.getcwd() + "\\" + filename + ".txt"
    file_array = open(filepath)


    raw_lines = [x[:-1].split(" ") for x in file_array.readlines()]
    n_cities = int(raw_lines[0][0])
    city_coordinates = np.array([(float(x), float(y)) for x, y in raw_lines[1:]])

    file_array.close()

    return n_cities, city_coordinates

