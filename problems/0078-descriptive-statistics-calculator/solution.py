import numpy as np
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    
    data_array = (np.asarray(data))

    mean = data_array.sum() / len(data_array)

    if len(data_array) % 2 != 0:
        data_array = np.sort(data_array)
        median = data_array[len(data_array) // 2]
        data_array = (np.asarray(data))
    else:
        data_array = np.sort(data_array)
        median = (data_array[len(data_array) // 2] + data_array[len(data_array) // 2 - 1]) / 2
        data_array = (np.asarray(data))
    
    vals, counts = np.unique(data_array, return_counts = True)
    most_counts = np.argmax(counts)
    mode = vals[most_counts]

    var = 0.0
    for i in range(len(data_array)):
        var += (data_array[i] - mean)**2
    var = var / len(data_array)

    dev = var ** 0.5

    if len(data_array) == 1:
        percentile_25 = data_array[0]
    else:
        data_array = np.sort(data_array)
        rank = 0.25 * (len(data_array) - 1)
        lower = math.floor(rank)
        frac = rank - lower
        percentile_25 = data_array[lower] + (frac * (data_array[lower + 1] - data_array[lower]))

    if len(data_array) == 1:
        percentile_50 = data_array[0]
    else:
        data_array = np.sort(data_array)
        rank = 0.5 * (len(data_array) - 1)
        lower = math.floor(rank)
        frac = rank - lower
        percentile_50 = data_array[lower] + (frac * (data_array[lower + 1] - data_array[lower]))

    if len(data_array) == 1:
        percentile_75 = data_array[0]
    else:
        data_array = np.sort(data_array)
        rank = 0.75 * (len(data_array) - 1)
        lower = math.floor(rank)
        frac = rank - lower
        percentile_75 = data_array[lower] + (frac * (data_array[lower + 1] - data_array[lower]))

    interq_range = percentile_75 - percentile_25

    return {'mean': mean, 'median': median, 'mode': mode, 'variance': var, 'standard_deviation': dev, '25th_percentile': percentile_25, '50th_percentile': percentile_50, '75th_percentile': percentile_75, 'interquartile_range': interq_range}
    pass