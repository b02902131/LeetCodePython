/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution
{
    public ListNode MiddleNode(ListNode head)
    {
        ListNode ptr = head;
        int finalIndex = 0;
        while (ptr.next != null)
        {
            finalIndex++;
            ptr = ptr.next;
        }
        int middleIndex = (finalIndex + 1) / 2;
        ptr = head;
        while (middleIndex-- > 0)
        {
            ptr = ptr.next;
        }
        return ptr;
    }
}
