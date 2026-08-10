/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length=0;
        ListNode temp = head;
        while(temp!=null)
        {
            temp = temp.next;
            length++;
        }

        int diff = length - n;
        if(diff==0) //First Element;
        {
            head = head.next;
            return head;
        }
        else
        {
            int move=0;
            ListNode t = head;
            if(length==1)
            {
                return null;
            }
            while(move!=diff-1)
            {
                t = t.next;
                move++;
            }
            ListNode t1 = t.next;
            t.next = t1.next;
            t1.next = null;
            return head;
        }

    }
}
