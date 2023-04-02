
import queue

# inbuilt Queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())
print()
# inbuilt Stack
s = queue.LifoQueue()
s.put(1)
s.put(2)
s.put(3)

while not s.empty():
    print(s.get())