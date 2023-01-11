# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# example solution
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# my solution Time O(N) Space O(N)
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         n = 0
#         ptr = head
#         while ptr.next != None:
#             ptr = ptr.next
#             n+=1
            
#         n /= 2
#         ptr = head
#         while n > 0:
#             ptr = ptr.next
#             n -= 1
            
#         return ptr

class TestCase(object):
    def __init__(self, x, y):
        s = ListNode(x[0])
        p = s
        for i in x[1:]:
            p.next = ListNode(i)
            p = p.next
        self.x = p
            
        s = ListNode(x[0])
        p = s
        for i in y[1:]:
            p.next = ListNode(i)
            p = p.next
        self.y = p
              
testCases = [
    TestCase([1,2,3,4,5],[3,4,5]),
    TestCase([1,2,3,4,5,6],[4,5,6]),
    TestCase([1],[1])
]

if __name__ == "__main__":
    
    s = Solution()
    
    ac = True
    for tc in testCases:
        if s.middleNode(tc.x) != tc.y:
            ac = False
            print(f'wrong! {tc.x}, {tc.y}, a = {s.middleNode(tc.x)}')

    if ac:
        print('All correct!')