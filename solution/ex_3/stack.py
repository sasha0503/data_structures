class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()


def input_stacks(stack_even: Stack, stack_odd: Stack):
    print("Type 'q' to finish.")
    print('Only integers are allowed.')
    while True:
        val = input(">> ")
        if val == 'q':
            break
        try:
            val = int(val)
        except ValueError:
            print("Invalid input.")
            continue
        if val % 2 == 0:
            stack_even.push(val)
        else:
            stack_odd.push(val)
        print("Парні:", stack_even.stack)
        print("Непарні:", stack_odd.stack)


if __name__ == '__main__':
    stack_even_test = Stack()
    stack_odd_test = Stack()
    input_stacks(stack_even_test, stack_odd_test)
    print("##################")
    print("Парні:", stack_even_test.stack)
    print("Непарні:", stack_odd_test.stack)
