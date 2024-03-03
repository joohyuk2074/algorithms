package me.joohyuk.codinginterview.chapter02;

public class Problem04 {

    LinkedListNode partitionWithStability(LinkedListNode node, int x) {
        LinkedListNode beforeStart = null;
        LinkedListNode beforeEnd = null;
        LinkedListNode afterStart = null;
        LinkedListNode afterEnd = null;

        // 리스트를 분할한다.
        while (node != null) {
            LinkedListNode next = node.next;
            node.next = null;

            if (node.data < x) {
                // before 리스트의 끝에 원소를 삽입한다.
                if (beforeStart == null) {
                    beforeStart = node;
                    beforeEnd = beforeStart;
                } else {
                    beforeEnd.next = node;
                    beforeEnd = node;
                }
            } else {
                // after 리스트의 끝에 원소를 삽입한다.
                if (afterStart == null) {
                    afterStart = node;
                    afterEnd = afterStart;
                } else {
                    afterEnd.next = node;
                    afterEnd = node;
                }
            }

            node = next;
        }

        if (beforeStart == null) {
            return afterStart;
        }

        beforeEnd.next = afterStart;
        return beforeStart;
    }

    LinkedListNode partitionWithNoStability(LinkedListNode node, int x) {
        LinkedListNode head = node;
        LinkedListNode tail = node;

        while (node != null) {
            LinkedListNode next = node.next;
            if (node.data < x) {
                // head에 노드를 삽입
                node.next = head;
                head = node;
            } else {
                tail.next = node;
                tail = node;
            }
            node = next;
        }

        tail.next = null;

        return head;
    }
}
