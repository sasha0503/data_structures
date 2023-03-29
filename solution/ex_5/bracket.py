from solution.ex_3.stack import Stack


def is_balanced(word):
    """Check if all brackets are closed in the right order.
    """
    stack = Stack()
    for char in word:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if not stack.stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            stack.pop()
    return not stack.stack


if __name__ == '__main__':
    print('----------------------------------------')
    print("Type a combination of () {} [] and I will check if they are balanced.")
    print('All other characters will be ignored.')
    print('----------------------------------------')
    print("Type 'q' to finish.")
    while True:
        test_word = input(">> ")
        if test_word == 'q':
            break
        print("Balanced" if is_balanced(test_word) else "Not balanced")
