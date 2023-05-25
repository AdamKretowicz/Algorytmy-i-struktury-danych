def find_max(vector):
    if len(vector) == 1:
        return vector[0]
    elif len(vector) == 2:
        return max(vector[0], vector[1])
    else:
        mid = len(vector) // 2
        left_max = find_max(vector[:mid])
        right_max = find_max(vector[mid:])
        return max(left_max, right_max)

# Przykładowe użycie
vector = [5, 8, 3, 2, 9, 1, 6]
max_element = find_max(vector)
print("Największy element wektora:", max_element)
