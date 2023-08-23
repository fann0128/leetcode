from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy_head = ListNode(-1)
    dummy_head.next = head
    prev = dummy_head
    while prev.next :
        if prev.next.val == val:
            prev.next = prev.next.next
        else :
            prev = prev.next
    return dummy_head.next

def constructLinkedList(vals) -> Optional[ListNode]:
    if len(vals) == 0:
        return ListNode()

    head = cur = ListNode(vals[0])
    for v in vals[1::]:
        tmp = ListNode(v)
        cur.next = tmp
        cur = cur.next

    return head

def printLinkedList(node: Optional[ListNode]) -> None:
    if node :
        print(node.val)
        if node.next:
            printLinkedList(node.next)

def main():
    head = constructLinkedList([1,2,3,4,5])
    print("before")
    printLinkedList(head)
    removeElements(head, 3)
    print("after")
    printLinkedList(head)

if __name__ == "__main__":
    main()
