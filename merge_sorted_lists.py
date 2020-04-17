class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergetwoLists(l1, l2):

    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    elif l1.val < l2.val:
        l1.next = mergetwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergetwoLists(l1, l2.next)
        return l2

    # Start with the empty list

llist1 = ListNode(1)
llist1.next = ListNode(2)
llist1.next.next = ListNode(4)

llist2 = ListNode(1)
llist2.next = ListNode(3)
llist2.next.next = ListNode(4)


x = mergetwoLists(llist1,llist2)
while x:
    print(x.val)
    x = x.next

