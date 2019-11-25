from modules.syntax.syntax import *
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
    if item1.rank < item2.rank:
        item2.rank -= item1
        item1.rank = 0
    else:
        item1.rank -= item2.rank
        item2.rank = 0


def parse(pool):
    # TODO save special_parameters
    # print(pool.args)
    ranks = dict()

    for item in pool.value:
        ranks[item.source_value] = pool.count(item.source_value)
    remove_duplicates(pool.value)

    for item in pool.value:
        item.rank = ranks[item.source_value]