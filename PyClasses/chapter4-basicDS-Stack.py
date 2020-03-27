#from pythonds.basic import Stack


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def self_check1():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

# self_check1()


def revstring(mystr):
    s = Stack()
    for letter in mystr:
        s.push(letter)
    reversed = ''
    while not s.isEmpty():
        reversed = reversed + s.pop()
    return reversed


print(revstring('abcdefghijklmnopqrstuvwyz'))


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))


def divideBy2(decNumber):
    remainderstack = Stack()
    while decNumber > 0:
        remainder = decNumber % 2
        remainderstack.push(remainder)
        decNumber = decNumber // 2

    binaryString = ''
    while not remainderstack.isEmpty():
        binaryString = binaryString + str(remainderstack.pop())

    return binaryString


print(divideBy2(23) + "-" + divideBy2(6) + "-" + divideBy2(17))


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'

    remainderStack = Stack()

    while decNumber > 0:
        remainder = decNumber % base
        remainderStack.push(remainder)
        decNumber = decNumber // base

    convertedString = ''

    while not remainderStack.isEmpty():
        convertedString = convertedString + str(digits[remainderStack.pop()])

    return convertedString


print(baseConverter(25, 2))
print(baseConverter(256, 16))
print(baseConverter(25, 8))
