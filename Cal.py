class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

print(calculator(10, 20).add())
print(calculator(10, 20).sub())
print(calculator(10, 20).mul())
print(calculator(10, 20).div())
