
def exception(vars_1, vars_2):
    for i in vars_1:
        if i in vars_2:
            vars_1.remove(i)

def division(items_1, items_2):
    exception([item.non_const_part for item in items_1])