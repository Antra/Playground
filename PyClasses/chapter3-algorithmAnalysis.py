import time
from random import randrange


def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    end = time.time()

    return theSum, end-start


def sumOfN3(n):
    start = time.time()
    end = time.time()
    return (n*(n+1))/2, end-start


for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN3(100000000))


def self_check1a(alist):
    # Write two Python functions to find the minimum number in a list.
    # The first function should compare each number to every other number on the list. O(n^2).
    # The second function should be linear O(n).

    answer = alist[0]

    for i in alist:
        for j in alist:
            if i < j and i < answer:
                answer = i

    return answer


def self_check1b(alist):
    # This for loop approach generally performs faster than the sorted version in option C
    minSoFar = alist[0]
    for i in alist:
        if i < minSoFar:
            minSoFar = i
    return minSoFar


def self_check1c(alist):
    temp = alist.sort()
    return alist[0]


for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(self_check1a(alist))
    end = time.time()
    print('Check#1: size %d time: %f' % (listSize, end-start))
    start = time.time()
    print(self_check1b(alist))
    end = time.time()
    print('Check#2: size %d time: %f' % (listSize, end-start))
    start = time.time()
    print(self_check1c(alist))
    end = time.time()
    print('Check#3: size %d time: %f' % (listSize, end-start))
