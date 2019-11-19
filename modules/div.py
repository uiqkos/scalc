from modules.syntax.syntax import *
def exception(vars_1, vars_2):
    for i in vars_1:
        if i in vars_2:
            vars_1.remove(i)

def parse(pool):
    if pool.operator is not Operator.operatorType.div:
        return False
