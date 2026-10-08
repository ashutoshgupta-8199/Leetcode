class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prevGroupTail = dummy

        while head:
            groupStart = head
            groupEnd = self.getGroupEnd(head, k)

            if not groupEnd:
                break

            prevGroupTail.next = self.reverseList(groupStart, groupEnd.next)
            prevGroupTail = groupStart
            head = prevGroupTail.next

        newHead = dummy.next
        return newHead

    def getGroupEnd(self, head, k):
        while head and k > 1:
            head = head.next
            k -= 1
        return head

    def reverseList(self, head, stop):
        prev = stop
        while head != stop:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev