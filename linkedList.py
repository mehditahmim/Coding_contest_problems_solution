class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head == None:
            print("No elements found!")
        else:
            headPointer = self.head
            while(headPointer is not None):
                print(headPointer.data)
                headPointer = headPointer.next
    def append(self, data):
        if self.head == None:
            self.data = Node(data)
        else:
            headPointer = self.head
            while(headPointer.next):
                headPointer = headPointer.next
            newNode = Node(data)
            headPointer.next = newNode    

    def size(self):
        headPointer = self.head
        item = 0
        while(headPointer):
            item += 1
            headPointer = headPointer.next
        print(item)

    def delete(self, node):
        node.data =  node.next.data
        node.next = node.next.next
        self.printList()
        




if __name__ == "__main__":
    llist = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head = first
    llist.head.next = second
    second.next = third
    llist.append(4)
    #llist.printList()
    #llist.size()
    llist.delete(second)


