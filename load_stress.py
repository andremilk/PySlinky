from multiprocessing import Pool
import multiprocessing
import psutil

loads = []
def stress(expression):
    def load_stress(x):
        i = expression(x)
        return psutil.cpu_percent(interval=0.1)
    return load_stress

def _stress(x):
    i = x**x
    return psutil.cpu_percent(interval=0.1)

def get_low_high_average(results):
    low = min(x for x in results if x > 0)
    high = sorted(results)[-1]
    average = sum(x for x in results)/len(results)
    print low, high, average

if __name__ == '__main__':
    no_of_cores = multiprocessing.cpu_count()
    p = Pool(processes=no_of_cores)
    l = map(stress(lambda x: x**x), range(100))
    print 'l = ', l
    get_low_high_average(l)
    k = p.map(_stress, range(100))
    print 'k = ', k
    get_low_high_average(k)
