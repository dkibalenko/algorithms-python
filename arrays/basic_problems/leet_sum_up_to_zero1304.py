def sum_to_zero(n: int):
    l = list(range(1, n))
    l.append(-sum(l))
    
    return l


def sum_to_zero2(n: int):

    result = []

    if n % 2 != 0:
        result = [0]
        
    for i in range(1, (n // 2) + 1):  # loop only a half of the sequence range
        result.append(i)
        result.append(-i)

    return result


def sum_to_zero3(n: int):
    return list(range(1 - n, n, 2))
    # step 2, gives you only range of 'n'

print(sum_to_zero3(4))


def test(n: int) -> list:
    result = []

    if n % 2 == 0:
        result.append(0)

    for i in range(1, n // 2 + 1):
        result.append(i)
        result.append(-i)

    return result