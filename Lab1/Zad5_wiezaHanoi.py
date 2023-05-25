def hanoi(n, glowna, docelowa, pomocnicza):
    if n > 0:
        hanoi(n-1, glowna, pomocnicza, docelowa)
        docelowa.append(glowna.pop())
        hanoi(n-1, pomocnicza, docelowa, glowna)

# przykład użycia
A = [3,2,1]    # glowna wieża A
B = []         # pomocnicza wieża B
C = []         # docelowa wieża C
hanoi(len(A), A, C, B)
print(C)       # wyświetl krążki na docelowej wieży C
