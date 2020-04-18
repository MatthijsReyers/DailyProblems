#!/usr/bin/python3

# THE DAILY PROBLEM
# -------------------------------------------------------------------------------------
# This problem was asked by Airbnb.
# Given a linked list and a positive integer k, rotate the list to the right by k places.
#
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, 
# it should become 3 -> 5 -> 7 -> 7.
#
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, 
# it should become 3 -> 4 -> 5 -> 1 -> 2.

class node:
    def __init__(self, data, previous):
        self.previous = previous
        self.next = None
        self.data = data
    
    def isHead(self) -> bool:
        return (self.previous == None)

    def isTail(self) -> bool:
        return (self.next == None)

    def append(self, data):
        temp = self.next
        self.next = node(data, self)
        self.next.next = temp

def toLinkedList(convertme: list) -> node:
    current = None;
    for item in convertme:
        if current == None:
            current = node(item, None)
            head = current
        else:
            current.append(item)
            current = current.next
    return head

def printList(head: node):
    current = head
    print("[", end="")
    while not current.isTail():
        print(current.data, ",", end="")
        current = current.previous
    print("]")

def rotateList(head: node, amount: int):
    oldhead = head

    newhead = head
    for _ in range(amount):
        newhead = newhead.next

if __name__ == '__main__':

    toReverse = toLinkedList([1,2,3,4,5,6,7,8,9,10])
    printList(toReverse)


    