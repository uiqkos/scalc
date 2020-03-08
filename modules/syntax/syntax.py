from enum import Enum

class Abstract:
    def __init__(self, value, initial_basic=None):
        self.value = value
        if initial_basic is None:
            self.initial_basic = InitalBasic(rank=1, mul=1)
        else:
            self.initial_basic = initial_basic

    def get_values(self):
        return self.value

    def get_initial(self):
        return self.initial_basic

class Pool:
    def __init__(
            self,
            source_value,
            internal_values,
            internal_operator,
            self_operator,
            initial_basic
    ):
        self.source_value = source_value
        self.internal_values = internal_values
        self.internal_operator = internal_operator
        self.self_operator = self_operator

        if initial_basic is None:
            self.initial_basic = InitalBasic(rank=1, mul=1)
        else:
            self.initial_basic = initial_basic
    # ! Constructors

    @classmethod
    def from_pool(cls, other, initial_basic):
        print(initial_basic.mul)
        return cls(
            other.source_value,
            other.internal_values,
            other.internal_operator,
            other.self_operator,
            InitalBasic(rank=1, mul=1) if initial_basic is None else initial_basic
        )

    def get_values(self):
        return [internal_value.get_values() for internal_value in self.internal_values]
        # for initial_value in self.initial_values:
        #     if isinstance(initial_value, Variable):
        #         return initial_value.name
        #     if isinstance(initial_value, Number):
        #         return initial_value.value
        #     if isinstance(initial_value, Pool):
        #         return initial_value.get_values()
class InitalBasic:
    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            self.__dict__[arg] = value

class Variable(Abstract):
    pass
    # def __init__(self, name):
    #     self.name = name
    #
    # def get_values(self):
    #     return self.name
class Number(Abstract):
    pass
    # def __init__(self, value):
    #     self.value = value
    #
    # def get_values(self):
    #     return self.value


class OperatorType(Enum):
    plus = '+'
    minus = '-'
    div = '/'
    mul = '*'

class Operator:
    def __init__(self, operator):
        self.operator, self.call_func = init(operator)

    def __call__(self, *args, **kwargs):
        return self.call_func(*args, **kwargs)

    def __eq__(self, other):
        if isinstance(other, OperatorType):
            return self.operator == other
        return self.operator == other.operator

def init(operator):
    return {
        '+': (OperatorType.plus,  lambda a, b: a + b),
        '-': (OperatorType.minus, lambda a, b: a - b),
        '*': (OperatorType.mul,   lambda a, b: a * b),
        '/': (OperatorType.div,   lambda a, b: a / b)
    }[operator]

