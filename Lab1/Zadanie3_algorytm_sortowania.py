def sortowanie(liczby):
    n = len(liczby)
    for i in range(n):
        for j in range(i + 1, n):
            if str(liczby[i]) > str(liczby[j]):
                liczby[i], liczby[j] = liczby[j], liczby[i]
    return liczby


# przykladowe wywolanie funkcji
liczby = [1, 2, 3, 11, 21, 111, 231]
posortowane = sortowanie(liczby)
print(posortowane)