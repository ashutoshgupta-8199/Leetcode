# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        # Create a min-heap and initialize it with the first node of each list
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        # Create a dummy node to build the merged list
        dummy = ListNode(0)
        current = dummy

        # Merge the lists using the min-heap
        while heap:
            val, index = heapq.heappop(heap)
            current.next = lists[index]
            current = current.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))

        return dummy.next
        