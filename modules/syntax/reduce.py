from modules.syntax.syntax import *
from collections import Counter
def delete(i, container):
    del container[i]

def reduce(
        items,
        get_value=lambda x : x,
        del_item=lambda i, container : delete(i, container)
):
    multiplicities = dict()
    delete = []

    for i, item in enumerate(items):
        if get_value(item) in multiplicities.keys():
            delete.append(i)
            continue
        multiplicities[get_value(item)] = Counter(getattr(item, 'source_value') for item in items)[get_value(item)]

    print(delete)

    for i in delete[::-1]: del_item(i, items)
    print(multiplicities)
    return multiplicities