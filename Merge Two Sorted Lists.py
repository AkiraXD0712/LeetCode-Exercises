import json
"""
Merge two sorted linked lists and return it as a new list. 

The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def toList(listnode):
            l = []
            while listnode is not None:
                l.append(listnode.val)
                listnode = listnode.next
            return l

        def toListnode(l):
            if len(l) != 0:
                listnode = ListNode(0)
                listnode.val = l[0]
                listnode.next = toListnode(l[1:]) if len(l) != 1 else None
                return listnode
            else:
                return None

        n1 = toList(l1)
        n2 = toList(l2)

        return toListnode(sorted(n1 + n2))


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()