from enum import Enum

class Operator:
    class operatorType:
        plus = '+'
        minus = '-'
        mul = '*'
        div = '/'
        fin = '_'

    operator_dict = {
        '+' : operatorType.plus,
        '-' : operatorType.minus,
        '*' : operatorType.mul,
        '/' : operatorType.div,
        '_' : operatorType.fin
    }

    def __init__(self, source_op):
        self.type = self.operator_dict[source_op]

class Pool:
    class Type(Enum):
        expression = -1
        const = 1
        non_const = 0

    def __init__(self, source_value, value, type, operator):
        self.source_value = source_value
        self.value = value
        self.type = type
        self.operator = operator

    def get_values(self):
        return [value for value in self.value]

    def count(self, value):
        result = 0
        for item in self.value:
            result += (item.source_value is value)
        return result

# support
#
# def size(self):
#     return len(self)