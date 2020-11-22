class Node:
    def __init__(self,data,next_value, previous_value):
        self.data = data
        self.next = next_value
        self.prev = previous_value

class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def addFirst(self,obj):
        node = Node(obj,self.front,None)
        self.front = node

    def addLast(self,obj):
        node = Node(obj,None,self.rear)
        self.rear = node

    def removeFront(self):
        if (self.front == None):
            print("The list is empty")
        else:
            tmp = self.front
            self.front = self.front.next
            tmp.next = None


    def removeRear(self):
        if (self.rear == None):
            print("The list is empty")
        temp = self.rear
        self.rear = self.rear.prev
        temp.prev = None

    def first(self):
        if (self.front == None):
            print("The List is empty")
        else:
          print("First Node is:", {self.front.data})

    def last(self):
        if (self.rear == None):
            print("The List is empty")
        else:
         print("Last Node is:", {self.rear.data})

def main():
    list = LinkedList()
    list.addFirst("1")
    list.addFirst("9")
    list.addFirst("5")
    list.addLast("3")
    list.addLast("4")
    list.addLast("7")
    list.removeFront()
    list.removeFront()
    list.removeRear()
    list.removeRear()

    list.first()
    list.last()

main()