from collections import deque

fronta = deque()

fronta.append("A")
fronta.append("B")
fronta.append("C")

print("aktuálně:", fronta)
prvek = fronta.popleft()

print("obsloužen", prvek)
print("fronta aktuálně:", fronta)