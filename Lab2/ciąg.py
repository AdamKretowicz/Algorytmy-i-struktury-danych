def oblicz_wyraz(n):
    if n == 0 or n == 1:
        return 1

    wyrazy = [1, 1]  # Inicjalizacja listy wyrazów

    for i in range(2, n + 1):
        wyrazy.append(1)  # Dodawanie wartości 1 do listy

    return wyrazy[n]


# Przykładowe użycie:
n = 11
wynik = oblicz_wyraz(n)
print(f"Wyraz S({n}) = {wynik}")

#Wynik dla dowolnego n będzie zawsze równy 1