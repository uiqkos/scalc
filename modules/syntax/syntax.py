from enum import Enum

class Operator:
    class operatorType:
        plus = '+'
        minus = '-'
        mul = '*'
        div = '/'
        zero = '0'

    operator_dict = {
        '+' : operatorType.plus,
        '-' : operatorType.minus,
        '*' : operatorType.mul,
        '/' : operatorType.div,
        '0' : operatorType.zero
    }

    def __init__(self, source_op):
        self.type = self.operator_dict[source_op]

class Item:
    class itemType(Enum):
        const = 1
        non_const = 0

    special_parameters = dict()

    def __init__(self, value, type):
        self.value = value
        self.type = type

class Pool:
    def __init__(self, args, operator):
        self.args = args
        self.operator = Operator(operator)

    def count(self, value):
        result = 0
        for item in self.args:
            result += (item.value is value)
        return result