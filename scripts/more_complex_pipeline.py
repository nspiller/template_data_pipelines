import numpy as np
from src.computations import compute_mean


def many_steps(list_of_values):
    "Example pipeline with many steps"

    # convert to numpy array
    arr = np.array(list_of_values)

    # compute mean
    m = np.mean(arr)

    # compute standard deviation
    s = np.std(arr)

    # z-score
    z = (arr - m) / s

    # remove positive values
    z = z[z < 0]

    return z
