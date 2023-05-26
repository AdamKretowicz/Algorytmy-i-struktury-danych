def is_balanced(expression):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Napotkano zamykający nawias, gdy stos jest pusty
            last_opening_bracket = stack.pop()
            if opening_brackets.index(last_opening_bracket) != closing_brackets.index(char):
                return False  # Zamykający nawias nie pasuje do ostatniego otwierającego nawiasu

    return len(stack) == 0