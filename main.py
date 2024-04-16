# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.


class Stack:
    def __init__(self, max_numbers):
        self.max_numbers = max_numbers
        self.stack = []


    def push(self, item):
        if len(self.stack) < self.max_numbers:
            self.stack.append(item)
            return self.stack
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if len(self.stack) < self.max_numbers:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.stack)

    def is_full(self):
        return len(self.stack) == self.max_numbers

    def clear(self):
        self.stack = []

    def last_elem(self):
        if len(self.stack) < self.max_numbers:
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")


stack = Stack(3)
stack.push("1")
stack.push("2")
print(f"Last element of stack: {stack.last_elem()}")
print(stack.pop())
print(f"Stack size is: {stack.size()}")
stack.push("1")
stack.push("2")
print(f"Is stack full: {stack.is_full()}")
stack.clear()
