from modules import pow
from modules.syntax.syntax import *
from modules.syntax.reduce import *

a = Pool(
    'a*b',
    [
        Pool(
            'a*b',
            [Variable('a'), Variable('b')],
            Operator('*'),
            None,
            None
        ),
        Pool(
            'a*b',
            [Variable('a'), Variable('b')],
            Operator('*'),
            Operator('-'),
            InitalBasic(rank=1, mul=2)
        )
    ],
    Operator('+'),
    None,
    None
)

compone(a)