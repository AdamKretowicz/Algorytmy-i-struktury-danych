'''def oblicz_dwumianowy(n, m):
    if m > n:
        return 0

    wyniki = [[0] * (m + 1) for _ in range(n + 1)]  # Inicjalizacja tablicy wyników

    for i in range(n + 1):
        for j in range(min(i, m) + 1):
            if j == 0 or j == i:
                wyniki[i][j] = 1
            else:
                wyniki[i][j] = wyniki[i - 1][j - 1] + wyniki[i - 1][j]  # Wzór rekurencyjny

    return wyniki[n][m]


# Przykładowe użycie:
n = 20
m = 11
wynik = oblicz_dwumianowy(n, m)
print(f"Współczynnik dwumianowy C({n}, {m}) = {wynik}")'''

def wspolczynnik_dwumianowy(n, m):
    tab = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, m)+1):
            if j == 0 or i == j:
                tab[i][j] = 1
            else:
                tab[i][j] = tab[i-1][j] + tab[i-1][j-1]

    return tab[n][m]

# Przykładowe użycie:
n = 4
m = 2
wynik = wspolczynnik_dwumianowy(n, m)
print(f"Współczynnik dwumianowy C({n}, {m}) wynosi: {wynik}")

