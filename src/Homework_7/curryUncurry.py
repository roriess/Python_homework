def curry(func, n):
    if isinstance(n, int) and n >= 0 and func.__code__.co_argcount >= n:
        def curried(*args):
            if len(args) >= n:
                if n == 0:
                    return func()
                return func(*args[:n])
            return lambda *args2: curried(*(args + args2)) # если было передано недостаточно аргументов
        return curried
    else:
        raise ValueError("Incorrect n was transmitted")


def uncurry(func, n):
    if isinstance(n, int) and n >= 0:
        def uncurried(*args):
            if len(args) == n:
                if n == 0:
                    return func()
                res = func
                for arg in args:
                    res = res(arg)
                return res
            else:
                raise ValueError("Incorrect n was transmitted")
        return uncurried
    else:
        raise ValueError("Incorrect n was transmitted")