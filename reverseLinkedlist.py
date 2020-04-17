def reverseLinkedList(head):
    current = head
    previous = nextNode = None
    while current! = None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode
    return previous