package me.joohyuk.codinginterview.chapter02;

public class Problem02 {
    int printKthToLast(LinkedListNode head, int k) {
        if (head == null) {
            return 0;
        }

        int index = printKthToLast(head.next, k) + 1;

        if (index == k) {
            System.out.println(k + "th to last node is " + head.data);
        }
        return index;
    }

    LinkedListNode kthToLast(LinkedListNode head, int k) {
        Index idx = new Index();
        return kthToLast(head, k, idx);
    }

    LinkedListNode kthToLast(LinkedListNode head, int k, Index idx) {
        if (head == null) {
            return null;
        }

        LinkedListNode node = kthToLast(head.next, k, idx);
        idx.value++;
        if (idx.value == k) {
            return head;
        }
        return node;
    }

    public static class Index {
        public int value = 0;
    }

    LinkedListNode nthToLastWithIterate(LinkedListNode head, int k) {
        LinkedListNode p1 = head;
        LinkedListNode p2 = head;

        // p1을 k노드만큼 이동시킨다.
        for (int i = 0; i < k; i++) {
            if (p1 == null) {       // Out of Bounds
                return null;
            }
            p1 = p1.next;
        }

        // p1과 p2를 함께 움직인다. p1이 끝에 도달하면, p2는 length-k번째 원소를 가리키게 된다.
        while (p1 != null) {
            p1 = p1.next;
            p2 = p2.next;
        }

        return p2;
    }
}
