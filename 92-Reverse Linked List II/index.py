from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, head)
    l_pre = dummy_head
    cur = dummy_head.next

    for i in range(left-1):
        cur, l_pre = cur.next, l_pre.next
    
    pre = None
    for i in range(right-left+1):
        temp = cur.next
        cur.next = pre
        pre, cur = cur, temp
    
    l_pre.next.next = cur
    l_pre.next = pre

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
    # print("before")
    # printLinkedList(head)
    # print("after")
    reverseBetween(head,2,5)
    # printLinkedList()

if __name__ == "__main__":
    main()
