def fibonacci(n):
    fib = [0, 1]  # Inicjalizacja listy z dwoma pierwszymi elementami ciągu Fibonacciego

    if n < 2:
        return fib[n]  # Jeśli n <= 1, zwracamy n-ty element bez obliczania dalszych wartości

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Obliczanie kolejnych elementów ciągu

    return fib[n]  # Zwracamy n-ty element ciągu Fibonacciego


# Przykładowe użycie
n = int(input("Podaj numer elementu ciągu Fibonacciego: "))
result = fibonacci(n)
print("Wynik:", result)
