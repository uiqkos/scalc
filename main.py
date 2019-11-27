from modules import pow
from modules.syntax.syntax import *
from modules.syntax.reduce import *
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
#


main = \
    Pool('', [
        Pool('(a*a)*(a*a)*(a*a)', [
            Pool('a*a', [
                Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin)
            ], Pool.Type.expression, Operator.operatorType.mul),
            Pool('a*a', [
                Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin)
            ], Pool.Type.expression, Operator.operatorType.mul),
            Pool('a*a', [
                Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin)
            ], Pool.Type.expression, Operator.operatorType.mul),
        ], Pool.Type.expression, Operator.operatorType.mul),

        Pool('a+b', [
            Pool('a', 'a', Pool.Type.non_const, Operator.operatorType.fin), Pool('b', 'b', Pool.Type.non_const, Operator.operatorType.fin)
        ], Pool.Type.expression, Operator.operatorType.plus)
    ], Pool.Type.expression, Operator.operatorType.div
)


main.value[0].value[0].rank = 1
main.value[0].value[1].rank = 1
main.value[0].value[2].rank = 1
main.value[0].rank = 1

pow.parse(main.value[0].value[0])
pow.parse(main.value[0].value[1])
pow.parse(main.value[0].value[2])
reduce(main.value[0].value)
pow.parse(main.value[0])
print(main.value[0].value[0].rank, len(main.value[0].value))

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
#
# class A:
#     a = 4
#     b = 9
#     c = "aaff"
#     def __init__(self, number):
#         self.number = number
#
#     @property
#     def rank(self, other=None):
#         if other is not None:
#             self.number = 6666
#         return 4
# a = A(4)
# print(A.__dict__)
