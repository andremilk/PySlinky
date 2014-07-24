from multiprocessing import Pool
import multiprocessing
import psutil

def _load_stress(x):
    i = expression(x)
    return psutil.cpu_percent(interval=0.1)

def get_low_high_average(results):
    low = min(x for x in results if x > 0)
    high = sorted(results)[-1]
    average = sum(x for x in results)/len(results)
    return (low, high, average)

def main(_expression):
    global expression
    expression = eval('lambda x: {0}'.format(_expression))
    p = Pool(1)
    load_map = p.map(_load_stress, range(100))
    return get_low_high_average(load_map)
