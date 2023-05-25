def lex_sort(numbers):
    numbers.sort(key=lambda x: str(x))
    return sorted(numbers, key=lambda x: [int(d) for d in str(x)])

numbers = [1, 2, 3, 11, 21, 111, 231]
sorted_numbers = lex_sort(numbers)
print(sorted_numbers)
