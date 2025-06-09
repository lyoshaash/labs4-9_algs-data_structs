class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def put(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def get(self):
        if not self.head:
            return "error"
        val = self.head.value
        self.head = self.head.next
        self.count -= 1
        if self.head is None:
            self.tail = None
        return val

    def size(self):
        return self.count

q = Queue()
n = int(input())
for _ in range(n):
    cmd = input().strip()
    if cmd.startswith("put"):
        q.put(int(cmd.split()[1]))
    elif cmd == "get":
        print(q.get())
    elif cmd == "size":
        print(q.size())
