from solution.ex_5.bracket import is_balanced


def infix_to_rpn(expression: str) -> list:
    stack = []
    rpn = []
    i = 0
    while i < len(expression):
        token = expression[i]
        i += 1
        if token.isdigit():
            while i < len(expression) and expression[i].isdigit():
                token += expression[i]
                i += 1
            rpn.append(token)
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                rpn.append(stack.pop())
            stack.pop()
        elif token in '/*':
            stack.append(token)
        elif token in '+-':
            while stack and stack[-1] in '/*':
                rpn.append(stack.pop())
            stack.append(token)
    while stack:
        rpn.append(stack.pop())
    return rpn


def calculate_rpn(rpn):
    stack = []
    for token in rpn:
        if token.isdigit():
            stack.append(int(token))
        elif token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(-stack.pop() + stack.pop())
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            stack.append(1 / stack.pop() * stack.pop())
    return stack.pop()


if __name__ == '__main__':
    expression = "(20+(3+2*(5-4)/2)+3)*10"
    if not is_balanced(expression):
        print("Check your parentheses")
        exit(1)
    try:
        rpn = infix_to_rpn(expression)
        res = calculate_rpn(rpn)
    except Exception as e:
        print("Invalid expression")
        exit(1)
    print(expression)
    print(f"rpn: {' '.join(rpn)}")
    print(res)
