# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:

    def __init__(self,val=0):
        self.val = val
        self.next = None

    def get(self, index: int) -> int:
        cur = self.next
        pos = 0
        while cur:
            if pos == index:
                return (cur.val)
            cur = cur.next
            pos += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedList(val)
        new_node.next = self.next
        self.next = new_node
    
    def addAtTail(self, val: int) -> None:
        new_node = MyLinkedList(val)
        if not self.next:
            self.next = new_node
            return
        current = self.next
        while current.next:
            current = current.next
        current.next = new_node
        current = current.next
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = MyLinkedList(val)
        if index == 0:
            new_node.next = self.next
            self.next = new_node
            return

        pos = 0
        cur = self.next
        while cur and pos < index - 1:
            cur = cur.next
            pos += 1

        if cur is None:
            return  
        new_node.next = cur.next
        cur.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        if self.next is None:
            return
       
        if index == 0:
            self.next = self.next.next
            return
        
        temp = self.next
        for i in range(index-1):
            if temp is None or temp.next is None:
                return
            temp = temp.next

        if temp.next is None:
            return

        if temp.next:
            temp.next = temp.next.next
   

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList(-1)
# param_1 = obj.get(0)
# obj.addAtself.next(5)
# obj.addAtTail(6)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)