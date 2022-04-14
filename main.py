import random, time
import tabulate

def qsort(a, pivot_fn):
  if len(a) <= 1:
    return a
  else:
    p = pivot_fn(a)
    l = list(filter(lambda x: x < p, a))
    r = list(filter(lambda x: x > p, a))
    ql = qsort(l, pivot_fn)
    qr = qsort(r, pivot_fn)
  return ql + [p] + qr
    
def time_search(sort_fn, mylist):    
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000

def compare_sort(sizes=[10, 100, 200, 300, 400, 500, 600, 700, 800, 900]):
  qsort_fixed_pivot = lambda a: qsort(a, lambda a: a[0])
  qsort_random_pivot = lambda a: qsort(a, lambda a: random.choice(a))
  tim_sort = sorted
  result = []
  for size in sizes:
    mylist = list(range(size))
    result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
        ])
  return result


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort_fixed', 'qsort_random'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
