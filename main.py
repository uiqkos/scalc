from modules import pow
from modules.syntax.syntax import *

main = \
    Pool([
        Pool([
            Pool([
                Item('a', Item.itemType.non_const), Item('a', Item.itemType.non_const)
            ], Operator.operatorType.mul),
            Pool([
                Item(2, Item.itemType.const), Item('a', Item.itemType.non_const), Item('b', Item.itemType.non_const)
            ], Operator.operatorType.mul),
            Pool([
                Item('b', Item.itemType.non_const), Item('b', Item.itemType.non_const)
            ], Operator.operatorType.mul)
        ], Operator.operatorType.plus),

        Pool([
            Item('a', Item.itemType.non_const), Item('b', Item.itemType.non_const)
        ], Operator.operatorType.plus)
    ], Operator.operatorType.div
)

pow.parse(main.args[0].args[0])
print(main.args[0].args[1].args[0].special_parameters, main.args[0].args[0].args)
