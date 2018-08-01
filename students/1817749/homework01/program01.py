def divisors_factor(num):
    div = 2
    ret = 1
    while div * div <= num:
        cnt = 1
        while num % div == 0:
            cnt += 1
            num //= div
        ret *= cnt
        div += 1
    if num > 1:
        ret *= 2
    return ret


def modi(ls, k):
    ret = []
    for el in ls[:]:
        prop = divisors_factor(el) - 2
        if prop == 0:
            ret += [el]
        if prop != k:
            ls.remove(el)

    return ret
