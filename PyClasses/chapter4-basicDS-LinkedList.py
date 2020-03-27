class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def pop(self):
        current = self.head
        previous = None
        moreprev = None
        returnValue = ''
        while current != None:
            moreprev = previous
            previous = current
            current = current.getNext()
        if previous == None:
            returnValue = self.head.getData()
            self.head = None
        else:
            returnValue = previous.getData()
            moreprev.setNext(None)
        return returnValue

    def insert(self, item, pos):
        temp = Node(item)
        count = 0
        current = self.head
        previous = None
        while current != None and pos > count:
            previous = current
            current = current.getNext()
            count += 1
        if pos == count:
            temp.setNext(current)
            previous.setNext(temp)

    def index(self, item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                count += 1
                current = current.getNext()
        return count


mylist = UnorderedList()
print("size at start:", mylist.size())
mylist.append(1)
print("size after 1st append:", mylist.size())
mylist.append(2)
print("size after 2nd append:", mylist.size())
mylist.append(3)
print("size after 3rd append:", mylist.size())
mylist.append(4)
print("size after 4th append:", mylist.size())
print("index of 4?", mylist.index(4))
print("index of 3?", mylist.index(3))
print("index of 2?", mylist.index(2))
print("first pop:", mylist.pop())
print("second pop:", mylist.pop())
print("size after 2 pops:", mylist.size())
print("index of 2?", mylist.index(2))

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("size after all adds:", mylist.size())
print("third pop:", mylist.pop())
print("size after pop:", mylist.size())
print("93 found?", mylist.search(93))
print("index of 93?", mylist.index(93))
print("100 found?", mylist.search(100))

mylist.add(100)
print("100 found?", mylist.search(100))
print("size:", mylist.size())

print("index of 93?", mylist.index(93))
mylist.insert(5, 2)
print("index of 93?", mylist.index(93))
print("index of 5?", mylist.index(5))

mylist.remove(54)
print("size:", mylist.size())
mylist.remove(93)
print("size:", mylist.size())
mylist.remove(31)
print("size:", mylist.size())
print("93 found?", mylist.search(93))


class OrderedList:
    def __init__(self):
        self.head = None

    # isEmpty, size and remove work the same as for unordered lists

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
