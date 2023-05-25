def divide_and_conquer_sum(arr):
    # Przypadek bazowy: pusta tablica
    if len(arr) == 0:
        return 0

    # Przypadek bazowy: pojedynczy element
    if len(arr) == 1:
        return arr[0]

    # Podział tablicy na dwie połowy
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Obliczanie sumy dla lewej i prawej połowy rekurencyjnie
    left_sum = divide_and_conquer_sum(left_half)
    right_sum = divide_and_conquer_sum(right_half)

    # Zwracanie sumy dwóch części
    return left_sum + right_sum


# Przykładowe użycie
array = [1, 2, 3, 4, 5]
result = divide_and_conquer_sum(array)
print("Suma elementów w tablicy:", result)
