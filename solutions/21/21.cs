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
    public ListNode MergeTwoLists(ListNode list1, ListNode list2)
    {
        if (list1 == null)
        {
            return list2;
        }
        else if (list2 == null)
        {
            return list1;
        }

        ListNode mergedList = new ListNode();
        if (list1.val < list2.val)
        {
            mergedList.val = list1.val;
            mergedList.next = MergeTwoLists(list1.next, list2);
        }
        else
        {
            mergedList.val = list2.val;
            mergedList.next = MergeTwoLists(list2.next, list1);
        }

        return mergedList;
    }
}
