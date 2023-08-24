from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(cur, pre):
        if not cur:
            return pre
        next = cur.next
        cur.next = pre
        return reverse(next, cur)
    return reverse(head, None)

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
    reversed = reverseList(head)
    print("after")
    printLinkedList(reversed)

if __name__ == "__main__":
    main()
