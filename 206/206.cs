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
    public ListNode ReverseList(ListNode head)
    {
        if (head == null)
        {
            return null;
        }

        ListNode ptr = head;
        ListNode newHead = new ListNode(head.val, null);
        ListNode temp;
        while (ptr.next != null)
        {
            temp = newHead;
            newHead = new ListNode(ptr.next.val, temp);
            ptr = ptr.next;
        }
        return newHead;
    }
}
