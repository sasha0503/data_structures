import os
import random
import time


class QueueModel:
    def __init__(self):
        os.system('clear')
        n = input("Enter the number of lines: ")
        n = int(n)
        self.lines = []
        for i in range(n):
            self.lines.append([])

    def _delete_old_customers(self):
        os.system('clear')
        for line in self.lines:
            for customer in line:
                if time.time() > customer[0]:
                    line.remove(customer)

    def _add_customer(self, line_idx: str):
        if len(line_idx) > 1:
            for i in line_idx:
                self._add_customer(i)
        if not line_idx.isdigit():
            self._delete_old_customers()
            return
        line_idx = int(line_idx) - 1
        if line_idx + 1 > len(self.lines) or line_idx < 0:
            self._delete_old_customers()
            return
        last_time = self.lines[line_idx][-1][-2] if self.lines[line_idx] else time.time()
        last_name = self.lines[line_idx][-1][-1] if self.lines[line_idx] else '0'
        self.lines[line_idx].append([last_time + random.randint(1, 3), int(last_name) + 1])
        self._delete_old_customers()

    def _print_lines(self):
        n_cols = len(self.lines)
        n_rows = max(5, max([len(line) for line in self.lines]))
        for i in range(n_rows):
            for j in range(n_cols):
                if i < len(self.lines[j]):
                    print(f"| %.2d " % (self.lines[j][i][-1]), end='')
                else:
                    print("|    ", end='')
            print("|")
        print('\n')

    def run(self):
        os.system('clear')
        while True:
            self._print_lines()
            word = input(">> ")
            if word == 'q':
                break
            os.system('clear')
            self._add_customer(word)


if __name__ == '__main__':
    queue_model = QueueModel()
    queue_model.run()
