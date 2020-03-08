from modules.syntax.syntax import *
from collections import Counter

def compone(pool: Pool):  # for +
    internal_pool1 = pool.internal_values[0]
    internal_pool2 = pool.internal_values[1]

    if internal_pool1.initial_basic.rank == internal_pool2.initial_basic.rank and \
       internal_pool1.get_values() == internal_pool2.get_values():
        del pool.internal_values[0]
        del pool.internal_values[1]
        pool.internal_values.append(Pool(internal_pool1, ))