from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.count = 0 # save number of element

    def get(self, index: int) -> int:
        if index >= self.count :
            return -1
        cur = self.dummy_head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        while cur.next :
            cur = cur.next
        cur.next = ListNode(val)
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.count :
            cur = self.dummy_head
            while index > 0:
                cur = cur.next
                index -= 1
            new_node = ListNode(val)
            new_node.next = cur.next
            cur.next = new_node
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.count :
            cur = self.dummy_head
            while index > 0:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

def main():
    obj = MyLinkedList()
    print(obj.get(1))
    obj.addAtHead(7)
    obj.addAtTail(9)
    obj.addAtIndex(1,8)
    obj.deleteAtIndex(7)
    print(obj.get(1))

if __name__ == "__main__":
    main()