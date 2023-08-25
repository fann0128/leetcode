from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_node = 0
        cur = head
        while cur:
            total_node += 1
            cur = cur.next
        
        node_index_to_del = total_node - n

        dummy_head = ListNode()
        dummy_head.next = head

        cur = dummy_head
        cur_index = -1 # dummy head does not count

        while cur_index < node_index_to_del:
            if cur_index + 1 < node_index_to_del:
                cur = cur.next
                cur_index +=1 
            elif cur_index + 1 == node_index_to_del:
                if cur.next :
                    cur.next = cur.next.next
                else :
                    cur.next = None
                cur_index +=1 
        
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
    after = removeNthFromEnd(head, 2)
    print("after")
    printLinkedList(after)

if __name__ == "__main__":
    main()
