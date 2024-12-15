# работает только с целыми числами (int) но за константное время
def _isEven(value):
    return not (value & 1)


# работает с любыми числами, но время напрямую зависит от величины
def isEven(value):
    return value % 2 == 0
