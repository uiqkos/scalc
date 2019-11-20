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
        if items[i].value in flags:
            del items[i]
            continue
        else:
            flags.append(items[i].value)
            i += 1
        # print(flags)

def parse(pool):
    # TODO save special_parameters
    # print(pool.args)
    ranks = dict()

    for item in pool.args:
        ranks[item.value] = pool.count(item.value)
    remove_duplicates(pool.args)

    for item in pool.args:
        item.special_parameters['rank'] = ranks[item.value]