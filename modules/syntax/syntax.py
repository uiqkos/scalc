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
    class Property:
        def __init__(self, value, merge, equ):
            self.value = value
            self.merge = merge
            self.equ = equ

    class Type(Enum):
        expression = -1
        const = 1
        non_const = 0

    def default_eq(self, other, base_operator):
        if isinstance(other, Pool):
            return self.value == other.value
        return False

    def default_merge(self, other):
        return True

    def __init__(self, source_value, value, type, operator, base_operator):
        self.source_value = source_value
        self.value = value
        self.type = type
        self.operator = operator
        self.base_operator = base_operator
        self.properties = dict()
        self.to_remove = list()
        self.properties['main'] = Pool.Property('@main', self.default_merge, self.default_eq)

    def __hash__(self):
        return hash(self.source_value)

    def __eq__(self, other):
        if isinstance(other, Pool):
            for property in self.properties.values():
                if not property.equ(self, other): return False
            return True
        return False

    def clear(self):
        for pool in self.to_remove:
            del pool

    def values(self):
        return [item.source_value for item in self.value]

    def merge(self, other):
        for prop in self.properties.values():
            prop.merge(self, other, self.base_operator)
        del other
    # def add_property(self, name, value, merge):
    #     self.properties[name] = Pool.Property(value, merge)
# support
#
# def size(self):
#     return len(self)