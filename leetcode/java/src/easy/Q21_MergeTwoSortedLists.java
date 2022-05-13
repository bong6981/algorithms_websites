package easy;

public class Q21_MergeTwoSortedLists {
    public static void main(String[] args) {

    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
         if (list2 == null) {
             return list1;
         }

        ListNode ans;
        if(list1.val <= list2.val) {
            ans = new ListNode(list1.val);
            list1 = list1.next;
        } else {
            ans = new ListNode(list2.val);
            list2 = list2.next;
        }

        ListNode now = ans;
        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                now.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                now.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            now = now.next;
        }

        if(list1 != null) {
            while(list1 != null) {
                now.next = new ListNode(list1.val);
                list1 = list1.next;
                now = now.next;
            }
        }

        if(list2 != null) {
            while(list2 != null) {
                now.next = new ListNode(list2.val);
                list2 = list2.next;
                now = now.next;
            }
        }
        return ans;

    }

    static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

}
