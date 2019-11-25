from modules import pow
from modules.syntax.syntax import *
#
# main = \
#     Pool([
#         Pool([
#             Pool([
#                 Pool('a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', Pool.Type.non_const, Operator.operatorType.fin)
#             ], Pool.Type.expression, Operator.operatorType.mul),
#             Pool([
#                 Pool(2, Pool.Type.const, Operator.operatorType.fin), Pool('a', Pool.Type.non_const, Operator.operatorType.fin), Pool('b', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', Pool.Type.non_const, Operator.operatorType.fin)
#             ], Pool.Type.expression, Operator.operatorType.mul),
#             Pool([
#                 Pool('b', Pool.Type.non_const, Operator.operatorType.fin), Pool('b', Pool.Type.non_const, Operator.operatorType.fin)
#             ], Pool.Type.expression, Operator.operatorType.mul)
#         ], Pool.Type.expression, Operator.operatorType.plus),
#
#         Pool([
#             Pool('a', Pool.Type.non_const, Operator.operatorType.fin), Pool('b', Pool.Type.non_const, Operator.operatorType.fin)
#         ], Pool.Type.expression, Operator.operatorType.plus)
#     ], Pool.Type.expression, Operator.operatorType.div
# )
#
#
# main = \
#     Pool('', [
#         Pool('(a*a)*(a*a)*(a*a)', [
#             Pool('a*a', [
#                 Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin)
#             ], Pool.Type.expression, Operator.operatorType.mul),
#             Pool('a*a', [
#                 Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin)
#             ], Pool.Type.expression, Operator.operatorType.mul),
#             Pool('a*a', [
#                 Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin)
#             ], Pool.Type.expression, Operator.operatorType.mul)
#         ], Pool.Type.expression, Operator.operatorType.mul),
#
#         Pool('a+b', [
#             Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('b', 'b', Pool.Type.non_const, Operator.operatorType.fin)
#         ], Pool.Type.expression, Operator.operatorType.plus)
#     ], Pool.Type.expression, Operator.operatorType.div
# )
#
#
# pow.parse(main.value[0])
# pow.parse(main.value[0].value[0])
# print(main.value[0].value[0].rank, main.value[0].value[0].value[0].rank, len(main.value[0].value))

# def some():
#     pass
#
# class A:
#     pass
#     # def __getattr__(self, item, *args):
#     #     self.funcs[item](args)
#
#     # def __setattr__(self, key, value):
#     #     # if callable(value):
#     #     #     self.funcs[key] = value
#     #     # else:
#     #     #     self.
#     #     self.__dict__[key] = value
#
#
# def print_w(b, c):
#     print(b, c)
#
# func = print_w
#
# a = A()
#
# a.func = func
# # a.func(3, 4)
# a.func(3, 4)

class A:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, A):
            return other.number == self.number
        return False

    def __hash__(self):
        return hash(self.number)

    def __le__(self, other):
        if isinstance(other, A):
            return other.number <= self.number
        return False


a = A(77)
b = A(6)
c = A(7)
set_1 = set([a, b, c])
set_2 = set([b, c])
set_1 - set_2
print(set_1 - set_2)