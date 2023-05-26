def is_balanced_symbols(expression):
    stack = []
    opening_symbols = ['(', '[', '{']
    closing_symbols = [')', ']', '}']

    for char in expression:
        if char in opening_symbols:
            stack.append(char)
        elif char in closing_symbols:
            if not stack:
                return False  # Napotkano zamykający symbol, gdy stos jest pusty
            last_opening_symbol = stack.pop()
            if opening_symbols.index(last_opening_symbol) != closing_symbols.index(char):
                return False  # Zamykający symbol nie pasuje do ostatniego otwierającego symbolu

    return len(stack) == 0