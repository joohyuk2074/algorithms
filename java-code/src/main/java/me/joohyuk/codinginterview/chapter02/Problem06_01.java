package me.joohyuk.codinginterview.chapter02;

public class Problem06_01 {
    // 뒤집어서 비교

    boolean isPalindrome(LinkedListNode head) {
        LinkedListNode reversed = reverseAndClone(head);
        return isEqual(head, reversed);
    }

    LinkedListNode reverseAndClone(LinkedListNode node) {
        LinkedListNode head = null;
        while (node != null) {
            LinkedListNode n = new LinkedListNode(node.data);       // 복사
            n.next = head;
            head = n;
            node = node.next;
        }
        return head;
    }

    boolean isEqual(LinkedListNode one, LinkedListNode two) {
        while (one != null && two != null) {
            if (one.data != two.data) {
                return false;
            }
        }
        return one == null && two == null;
    }
}
