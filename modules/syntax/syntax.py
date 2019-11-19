from enum import Enum

class segType(Enum):
    expression = 1
    const = 2
    non_const = 3

class Operator:
    class operatorType:
        plus = '+'
        minus = '-'
        mul = '*'
        div = '/'

    operator_dict = {
        '+' : operatorType.plus,
        '-' : operatorType.minus,
        '*' : operatorType.mul,
        '/' : operatorType.div
    }

    def __init__(self, source_op):
        self.type = self.operator_dict[source_op]

class sourceItem:
    def __init__(self, source_expr):
        self.source_expr = source_expr

class Item:
    def __init__(self, value, type):
        self.value = value
        self.type = type

class Pool:
    def __init__(self, non_const_values, operator):
        # self.const_part = const_part
        self.non_const_values = non_const_values
        self.operator = Operator(operator)

