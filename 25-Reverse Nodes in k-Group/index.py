from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        if k == 1 :
            return head
        count = 0
        count_pointer = head
        while count_pointer:
            count += 1
            count_pointer = count_pointer.next
        remaining_groups = count // k
        cur = dummy_head.next
        prev = None
        prev_tail = dummy_head
        k_count = k
        while cur:
            if remaining_groups > 0:
                k_count -= 1
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                if k_count == 0:
                    # have enough k element to roate
                    prev_tail.next = prev
                    while prev_tail.next:
                        prev_tail = prev_tail.next
                    remaining_groups -= 1
                    k_count = k
                    prev = None
            else :
                prev_tail.next = cur
                break
        
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
    print("after")
    printLinkedList(reverseKGroup(head, 3))

if __name__ == "__main__":
    main()
