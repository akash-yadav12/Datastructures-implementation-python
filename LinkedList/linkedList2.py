class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    #push
    def insertAtBeg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAfterGivenNode(self, prev,data):
        if prev is None:
            print('there is no previous, it should  be in linked list')
            return
        node = Node(data)
        node.next = prev.next
        prev.next = node
    #append
    def insertAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
            
    def printLinkedList(self):
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) +'--->'
            itr = itr.next
        print(lstr)
    def reverseList(self):
        prev = None
        cur = self.head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBeg(3)
    ll.insertAtBeg(4)
    ll.insertAtBeg(5)
    ll.insertAtEnd(100)
    ll.printLinkedList()
    ll.reverseList()
    ll.printLinkedList()


