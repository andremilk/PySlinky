from multiprocessing import Pool
import multiprocessing
import psutil

def _load_stress(x):
    i = expression(x)
    return psutil.cpu_percent(interval=0.1, percpu=True)

def get_low_high_average(results):
    low = min(x for x in results if x > 0)
    high = sorted(results)[-1]
    average = sum(x for x in results)/len(results)
    return (low, high, average)

def organize_data(data_map):
    result = []
    for i in range(len(data_map[0])):
        result.append([])
    for item in data_map:
        for cpu in range(len(item)):
            result[cpu].append(item[cpu])
    return result

def main(_expression):
    global expression
    expression = eval('lambda x: {0}'.format(_expression))
    no_of_cores = multiprocessing.cpu_count()
    p = Pool(processes=no_of_cores)
    load_map = p.map(_load_stress, range(100))
    #return get_low_high_average(load_map)
    return organize_data(load_map)

