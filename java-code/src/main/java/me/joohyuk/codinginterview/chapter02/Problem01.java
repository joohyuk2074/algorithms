package me.joohyuk.codinginterview.chapter02;

import java.util.HashSet;
import java.util.Set;

public class Problem01 {

    void deleteDupsWithBuffer(LinkedListNode n) {
        Set<Integer> set = new HashSet<>();
        LinkedListNode previous = null;

        while (n != null) {
            if (set.contains(n.data)) {
                previous.next = n.next;
            } else {
                set.add(n.data);
                previous = n;
            }
            n = n.next;
        }
    }

    void deleteDuplsWithNoBuffer(LinkedListNode head) {
        LinkedListNode current = head;

        while (current != null) {
            // 값이 같은 다음 노드들을 모두 제거한다.
            LinkedListNode runner = current;
            while (runner.next != null) {
                if (runner.next.data == current.data) {
                    runner.next = runner.next.next;
                } else {
                    runner = runner.next;
                }
            }

            current = current.next;
        }
    }
}
