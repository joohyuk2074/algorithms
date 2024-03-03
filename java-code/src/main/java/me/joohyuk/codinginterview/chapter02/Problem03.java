package me.joohyuk.codinginterview.chapter02;

public class Problem03 {

    boolean deleteNode(LinkedListNode n) {
        if (n == null || n.next == null) {
            return false;
        }

        LinkedListNode next = n.next;

        n.data = next.data;
        n.next = next.next;

        return true;
    }
}
