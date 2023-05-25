#I wersja
def nwdIte(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(nwdIte(12,18)) #przyklad


def nwdRek(a, b):
    if a == b:
        return a
    elif a > b:
        return nwdRek(a - b, b)
    else:
        return nwdRek(a, b - a)
print(nwdRek(28,24))

#II wersja

def nwdIte2(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(nwdIte2(12,18))

def nwdRek2(a, b):
    if b == 0:
        return a
    else:
        return nwdRek2(b, a % b)
print(nwdRek2(28,24))

