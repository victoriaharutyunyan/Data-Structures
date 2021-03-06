class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, obj):
        node = Node(obj,None)
        if self.rear == None:
            self.rear = self.front = node
        self.rear.next = node
        self.rear = node

    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

def main():
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))

main()