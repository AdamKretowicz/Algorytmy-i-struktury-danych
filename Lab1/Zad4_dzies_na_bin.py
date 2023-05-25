def dec_to_bin(num):
    if num > 1:
        dec_to_bin(num // 2)
    print(num % 2, end='')

# przykładowe użycie
dec_to_bin(10) # wypisze 1010


