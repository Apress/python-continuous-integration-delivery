from functools import reduce
import operator

ops = {
    '+': operator.add,
    '-': operator.add,
    '*': operator.mul,
    '/': operator.truediv,
}

def math_eval(tree):
    if not isinstance(tree, list):
        return tree
    op = ops[tree.pop(0)]
    return reduce(op, map(math_eval, tree))
