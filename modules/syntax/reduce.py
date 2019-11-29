from modules.syntax.syntax import *
from collections import Counter
def delete(i, container):
    del container[i]

def reduce(
        pools,
        get_value=lambda x : x,
        del_item=lambda i, container : delete(i, container)
):
    multiplicities = dict()

    for pool in enumerate(pools):
        # if get_value(pool) in multiplicities.keys():
        #     multiplicities[get_value(pool)][1].append(index)
        #     continue
        # multiplicities[get_value(pool)] = tuple([index, []])
        for kpool in pools:
            if kpool == pool:
                pool.to_remove.append(kpool)
    for item in multiplicities.keys():
        for index in multiplicities[item][1][::-1]:
            pools[multiplicities[item][0]].merge(pools[index])
            # print(index, pools[index].source_value)
            delete(index, pools)
            # print(len(pools))


    return multiplicities