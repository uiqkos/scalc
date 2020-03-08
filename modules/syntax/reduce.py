from modules.syntax.syntax import *
from collections import Counter

def compone(pool: Pool):  # for +
    internal_pool1 = pool.internal_values[0]
    internal_pool2 = pool.internal_values[1]

    inib1 = internal_pool1.initial_basic
    inib2 = internal_pool2.initial_basic

    if inib1.rank == inib2.rank and \
       internal_pool1.get_values() == internal_pool2.get_values() and \
       pool.internal_operator == OperatorType.plus:

        pool.internal_values.append(
            Pool.from_pool(
                internal_pool1,
                InitalBasic(
                    rank=inib1.rank,
                    mul=inib1.mul - inib2.mul
                )
            )
        )

        del pool.internal_values[0]
        del pool.internal_values[0]
    else:
        print("No changes")