class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet():
    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def _hash(self, element):
        return hash(element) % self._capacity
    def add(self, element):
        index = self._hash(element)
        print(index)
        if (self._hashtable[index] == None):
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1
    #TODO add only unique values to the set
    def contains(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False
    def remove(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        p = None
        while (n != None):
            if (n.data == element):
                if (p == None):
                    self._hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None
    def size(self):
        return self._size

    def intersection(self, s):
        newSet = HashSet(100)
        for e in self._hashtable:
            while (e != None):
                if (s.contains(e.data)):
                    newSet.add(e.data)
                e = e.next
        return newSet

    def union(self, s):
        newSet = HashSet(100)
        for e in self._hashtable:
            while (e != None):
                if (not s.contains(e.data)):
                    newSet.add(e.data)
                e = e.next
        for e in s._hashtable:
            while (e != None):
                newSet.add(e.data)
                e = e.next
        return newSet

    def union_update(self, s):
        for i in s.levelOrderIterator():
            if (self.contains(i) == False):
                self.add(i)

    def intersection_update(self, s):
        for e in self._hashtable:
            p = None
            while (e != None):
                r = None
                if (not s.contains(e.data)):
                    r = e
                    ''''
                    # Option 1
                    r = e
                    e = e.next
                    self.remove(r.data)
                    continue
                    '''
                if (r != None):
                    if (p == None):
                        self._hashtable[self._hash(r.data)] = e.next
                    else:
                        p.next = e.next
                    e = e.next
                    self._size -= 1
                else:
                    p = e
                    e = e.next
    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next
    def __iter__(self):
        for e in self._hashtable:
            if (e != None):
                self._elem = e
                break
        return self
    def __next__(self):
        if self._elem == None:
            raise StopIteration
        tmp = self._elem
        if (self._elem.next != None):
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if (self._hashtable[i] != None):
                    self._elem = self._hashtable[i]
                    break
        return tmp.data


HS = HashSet(100)
HS.add("aa")
HS.add("bb")
HS.add(1)
HS.add(3)
HS1 = HashSet(100)
HS1.add("aa")
HS1.add("bb")
HS1.add(2)
HS1.add(3)
print()
HS3 = HS.intersection(HS1)
print()
HS4 = HS.union(HS1)
print()
# print(HS3.size())
# HS3.print()
HS.intersection_update(HS1)
# HS.print()
for elem in HS:
    print(elem)
