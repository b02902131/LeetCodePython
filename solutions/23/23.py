# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(len(lists)-1, -1, -1):
            if not lists[i]:
                lists.pop(i)
    
        dummyHead = ListNode()
        currNode = dummyHead
        
        while len(lists) > 0:
            minValue, minIdx = float('inf'), -1
            for i in range(len(lists)):
                if lists[i].val < minValue:
                    minValue = lists[i].val
                    minIndice = i
            currNode.next = lists[minIndice]
            currNode = currNode.next
            lists[minIndice] = lists[minIndice].next
            if not lists[minIndice]:
                lists.pop(minIndice)
        return dummyHead.next