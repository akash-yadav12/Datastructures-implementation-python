class Node:
    def __init__(self,data, prev=None,next = None):
        self.prev = prev
        self.data = data
        self.next = next
class DoublyList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        node = Node(data)
        node.prev = None
        if head:
            self.head.prev = node
            node.next = self.head
        self.head = node
    # def 
if __name__ == "__main__":
    dll = DoublyList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    # dll.print()
        
        