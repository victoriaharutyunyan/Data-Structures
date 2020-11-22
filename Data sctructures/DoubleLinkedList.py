class Node:
    # Class to create nodes for linked list
    def __init__(self, DataVal=None):
        self.DataVal = DataVal
        self.NextVal = None
        self.PrevVal = None

class DLinkedList:
    def __init__(self):
        self.HeadVal = None

    def listprint(self, node):
        # Prints the linked list
        while node is not None:
            print(node.DataVal),
            last = node
            node = node.NextVal

    def addFirst(self, NewData):
        # Adds new element to the beginning of the list
        NewNode = Node(NewData)
        NewNode.NextVal = self.HeadVal
        if self.HeadVal is not None:
            self.HeadVal.PrevVal = NewNode
        self.HeadVal = NewNode

    def addLast(self, NewData):
        # Adds new element to the end if the list
        NewNode = Node(NewData)
        NewNode.NextVal = None
        if self.HeadVal is None:
            NewNode.PrevVal = None
            self.HeadVal = NewNode
            return
        last = self.HeadVal
        while (last.NextVal is not None):
            last = last.NextVal
        last.NextVal = NewNode
        NewNode.PrevVal = last
        return

    def InsertAfter(self, PrevNode, NewData):
        #   Inserts new element after the given element
        if PrevNode is None:
            return
        NewNode = Node(NewData)
        NewNode.NextVal = PrevNode.NextVal
        PrevNode.NextVal = NewNode
        NewNode.PrevVal = PrevNode
        if NewNode.NextVal is not None:
            NewNode.NextVal.PrevVal = NewNode

    def InsertBefore(self, NextNode, NewData):
        #   Inserts new element before the given element
        if NextNode is None:
            return
        NewNode = Node(NewData)
        NewNode.PrevVal = NextNode.PrevVal
        NextNode.PrevVal = NewNode
        NewNode.NextVal = NextNode
        if NewNode.NextVal is not None:
            NewNode.PrevVal.NextVal = NewNode

    def RemoveNode(self, RemoveKey):
        # Removes an elements from linked list using the provided remove key
        HeadVal = self.HeadVal

        if HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                self.HeadVal = HeadVal.NextVal
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.NextVal
        if HeadVal == None:
            return
        prev.NextVal = HeadVal.NextVal

        HeadVal = None

    def RemoveFirst(self):
        #   Removes the first element of the list
        self.RemoveNode(self.First())

    def RemoveLast(self):
        #   Removes the last element of the list
        self.RemoveNode(self.Last())

    def First(self):
        #   Returns the first element of the list
        return self.HeadVal.DataVal

    def Last(self):
        #   Returns the last element of the list
        last = self.HeadVal
        while last is not None:
            if last.NextVal == None:
                return (last.DataVal)
            last = last.NextVal

def main():
    dll_test = DLinkedList()
    dll_test.addFirst("A")
    dll_test.addLast("B")
    dll_test.addFirst("C")
    dll_test.addLast("D")
    dll_test.addFirst("E")
    dll_test.addFirst("F")
    dll_test.addLast("G")
    dll_test.addLast("H")

    dll_test.listprint(dll_test.HeadVal)

    dll_test.RemoveFirst()
    dll_test.InsertAfter(dll_test.HeadVal.NextVal, "G")
    dll_test.RemoveLast()
    dll_test.RemoveNode("G")

    dll_test.listprint(dll_test.HeadVal)
    print(dll_test.First())
    print(dll_test.Last())
main()