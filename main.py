from enum import Enum

# class segment:
#     class segType(Enum):
#         undefined = -1
#         const = 0
#         non_const = 1
#

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
    def __init__(self, const_part, non_const_part, operator):
        self.const_part = const_part
        self.non_const_part = non_const_part
        self.operator = Operator(operator)

class pool:
    def __init__(self, non_const_values, operator):
        # self.const_part = const_part
        self.non_const_values = non_const_values
        self.operator = Operator(operator)

a = Item(3, ['a', 'b'], '/')
b = Item(1, ['a', 'a'], '/')
