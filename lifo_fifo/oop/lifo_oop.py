class Lifo:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self) -> bool:
        return len(self.items)==0

    def pop(self):
        if self.isEmpty():
            raise IndexError("Zásobník je prázdný!!!")
        return self.items.pop()

s = Lifo()
s.push("A")
s.push("B")
s.push("C")

print("---------------------")
print(s.pop())
print("zbývá", s.items)
print("---------------------")