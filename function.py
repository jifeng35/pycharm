def jc(a):
    if a > 1:
        return a * jc(a - 1)
    elif a == 1:
        return 1


print(jc(5))
