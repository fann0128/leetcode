from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
        values = []
        cur = head
        while cur : 
            values.append(cur.val)
            cur = cur.next
        return values == values[::-1]

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
    head = constructLinkedList([1,1,2,1])
    print(isPalindrome(head))

if __name__ == "__main__":
    main()
