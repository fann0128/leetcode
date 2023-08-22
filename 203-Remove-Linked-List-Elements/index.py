from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    cur, prev = head, None
    while cur :
        if cur.val == val:
            if prev is not None:
                prev.next = cur.next
                cur = cur.next
            else :
                cur = cur.next
                head = cur
        else :
            prev = cur
            cur = cur.next
    return head

def printLinkedList(node: Optional[ListNode]) -> None:
    if node :
        print(node.val)

        if node.next:
            printLinkedList(node.next)
    

def main():
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    print("before")
    printLinkedList(head)
    removeElements(head, 3)
    print("after")
    printLinkedList(head)

if __name__ == "__main__":
    main()