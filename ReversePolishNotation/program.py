def calc(expr):
    if not expr: return 0
    stack = []
    for e in expr.split(" "):
        if e not in ["+", "-", "*", "/"]:
            stack.append(e)
        else:
            a, b = stack.pop(), stack.pop()
            tmp = eval("{}{}{}" . format(b, e, a))
            stack.append(tmp)
    return float(stack.pop())