from modules.syntax.syntax import *
from modules.syntax.reduce import *
# #
# # class rank:
# #     def __init__(self, rank):
# def remove_duplicates(values):
#     for i in range(0, len(values)):
#         if values.count(values[i]) > 1:
#             for value in values[i:]:
#                 if value == values[i]:
#                     del value
#
#

def remove_duplicates(items):
    flags = []
    i = 0
    while i < len(items):
        # print(flags)
        if items[i].source_value in flags:
            del items[i]
        else:
            flags.append(items[i].source_value)
            i += 1
        # print(flags)

def lower_rank(item1, item2):
    diff = item1.rank - item2.rank
    ge = lambda x : x if x >= 0 else 0
    item1.rank, item2.rank = ge(diff), ge(-diff)


def parse(pool):
    # TODO save special_parameters
    # print(pool.args)
    ranks = reduce(pool.value, get_value=lambda pool : pool.source_value)
    print(ranks, pool.value[:])
    for item in pool.value:
        item.rank = ranks[item.source_value]