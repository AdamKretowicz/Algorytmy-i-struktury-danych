def evaluate_rpn(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Niepoprawne wyrażenie ONP")

            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                raise ValueError("Nieznany operator")

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Niepoprawne wyrażenie ONP")

    return stack[0]