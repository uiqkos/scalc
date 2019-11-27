from modules.syntax.syntax import *
from modules.syntax.reduce import *

def lower_rank(item1, item2):
    diff = item1.rank - item2.rank
    ge = lambda x : x if x >= 0 else 0
    item1.rank, item2.rank = ge(diff), ge(-diff)

def merge_rank(pool1, pool2):
    print(pool1.rank, pool2.rank)
    pool1.rank += pool2.rank

def parse(pool):
    # TODO save special_parameters
    # print(pool.args)
    for item in pool.value:
        #
        item.managers.append(merge_rank)
        print(pool.ge)
    ranks = reduce(pool.value, get_value=lambda pool : pool.source_value)
    # print(ranks, pool.value[:])
    for item in pool.value:
        item.rank = ranks[item.source_value]
        item.managers.append(merge_rank)