from collections import deque

class Fifo:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def pop(self):
        if self.isEmpty():
            raise IndexError("fronta je prázná!!!")
        return self.items.popleft()

s = Fifo()
s.push("A")
s.push("B")
s.push("C")

print("---------------------")
print("odstraněn:", s.pop())
print("zbývá:", s.items)
print("---------------------")
