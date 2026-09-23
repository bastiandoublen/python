stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack pop:", stack.pop())

from collections import deque
queue = deque(["Ram", "Tarun", "Asif"])
queue.append("Akbar")
print("Queue popleft:", queue.popleft())
print("Queue remaining:", list(queue))
