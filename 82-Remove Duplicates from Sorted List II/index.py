from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev, cur = dummy, dummy.next

    while cur and cur.next:
        if cur.val == cur.next.val:
            if cur.next.next :
                next_node = cur.next.next
                while next_node and next_node.val == cur.val:
                    next_node = next_node.next
            else :
                next_node = None
            cur = next_node
            prev.next = next_node
        else :
            cur = cur.next
            prev = prev.next
    
    return dummy.next

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
    head = constructLinkedList([1,2,3,3,4,5,5])
    print("before")
    printLinkedList(head)
    print("after")
    printLinkedList(deleteDuplicates(head))

if __name__ == "__main__":
    main()
