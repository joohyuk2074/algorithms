package me.joohyuk.codinginterview.chapter02;

public class Problem07 {
    LinkedListNode findIntersection(LinkedListNode list1, LinkedListNode list2) {
        if (list1 == null || list2 == null) {
            return null;
        }

        // 마지막 노드와 길이를 구한다.
        Result result1 = getTailAndSize(list1);
        Result result2 = getTailAndSize(list2);

        // 마지막 노드가 다르면 교집합이 없다는 뜻이다.
        if (result1.tail != result2.tail) {
            return null;
        }

        // 각 연결릿트의 시작점에 포인터를 세팅한다.
        LinkedListNode shorter = result1.size < result2.size ? list1 : list2;
        LinkedListNode longer = result1.size < result2.size ? list2 : list1;

        // 길이가 긴 연결리스트의 포인터를 길이의 차이만큼 앞으로 움직인다.
        longer = getKthNode(longer, Math.abs(result1.size - result2.size));

        // 두 포인터가 만날 때까지 함께 앞으로 움직인다.
        while (shorter != longer) {
            shorter = shorter.next;
            longer = longer.next;
        }

        return longer;
    }

    private LinkedListNode getKthNode(LinkedListNode head, int k) {
        LinkedListNode current = head;
        while (k > 0 && current != null) {
            current = current.next;
            k--;
        }
        return current;
    }

    private Result getTailAndSize(LinkedListNode list) {
        if (list == null) {
            return null;
        }

        int size = 1;
        LinkedListNode current = list;
        while (current.next != null) {
            size++;
            current = current.next;
        }
        return new Result(current, size);
    }

    class Result {
        public LinkedListNode tail;
        public int size;

        public Result(LinkedListNode tail, int size) {
            this.tail = tail;
            this.size = size;
        }
    }
}
