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
    load_map = map(_load_stress, range(100))
    load_map = []
    for x in range(150):
        load_map.append(_load_stress(x))
    sum(load_map)
    return get_low_high_average(load_map)

def get_health(now):
    if now:
        return psutil.cpu_percent(interval=None)
    return psutil.cpu_percent(interval=0.1)

