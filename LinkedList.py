#Create a List(node)
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

#Create Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    def print(self):
        if self.head is None:
            print('empty linked list')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '----->'
            itr = itr.next
        print(llstr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    #insert node at begining
    def insert_at_begining(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    #insert a node at specified index
    def insert_at(self,data,index):
        if index<0 or index>self.get_length():
            print('invalid index')
            return
        elif index == 0:
            self.head = Node(data,self.head)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1


    #insert element at the end of the list
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)


    #delete a node by specified index
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    # create a loop for testing check_loop()
    def create_loop(self,head):
        itr = head 
        while itr.next:
            itr = itr.next
        itr.next = head


    #check if loop present
    def check_loop(self,head):
        #Using hashing
        fil = set()
        itr = head
        while itr:
            if itr.next is None:
                return 0
            elif itr in fil:
                return 1
            fil.add(itr)
            itr = itr.next
        #Using Floyd's cycle alog
        # tor = head
        # hare = head
        # while tor and hare and hare.next:
        #     if tor == hare:
        #         return 1
        #     tor = tor.next
        #     hare = hare.next.next
        # return 0

    #reverse a list
    # def reverse_list(self,head):
    #     node = Node()
    #     head = node
    #     itr = head
    #     while itr:
    #         if node is None:
    #             node = head
    #         # else:
    #         #     newNode = Node(head.data)
    #         #     node.next = itr
    def reverseList(self,head):
        prev = None
        cur = head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev
                


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining('akash')
    ll.insert_at_begining('raisaheb')
    ll.insert_at_begining('yadav')
    ll.insert_at('nooo',3)
    print(ll.get_length())
    ll.insert_at_begining('aku')
    ll.insert_at_end('end')
    print(ll.check_loop(ll.head))
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.reverseList(ll.head)
    ll.print()
    # ll.create_loop(ll.head)

    # print('checking for loops',ll.check_loop(ll.head))