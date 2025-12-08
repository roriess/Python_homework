def curry(func, n):
    if int(n) == n and n > 0 and func.__code__.co_argcount == n:
        def curried(*args):
            if len(args) >= func.__code__.co_argcount:
                return func(*args)
            return lambda *args2: curried(*(args + args2)) # если было передано недостаточно аргументов
        return curried
    else:
        raise ValueError("Incorrect n was transmitted")

def uncurry(func, n):
    def uncurried(*args):
        res = func
        for arg in args:
            res = res(arg)
        return res
    return uncurried