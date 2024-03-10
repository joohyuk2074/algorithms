package me.joohyuk.codinginterview.chapter02;

public class Problem06_03 {
    // 재귀 접근

    boolean isPalindrome(LinkedListNode head) {
        int length = lengthOfList(head);
        Result p = isPalindrome(head, length);
        return p.result;
    }

    private Result isPalindrome(LinkedListNode head, int length) {
        if (head == null || length <= 0) {
            return new Result(head, true);
        } else if (length == 1) {
            return new Result(head.next, true);
        }

        // 부분 리스트를 재귀적으로 호출한다.
        Result res = isPalindrome(head.next, length - 2);

        // 아래 호출 결과 회문이 아니라는 사실이 밝혀지면, 그 결과값을 반환한다.
        if (!res.result || res.node == null) {
            return res;
        }

        // 두 노드의 값이 같은지 확인한다.
        res.result = (head.data == res.node.data);
        // 그 다음에 비교할 노드를 반환한다.
        res.node = res.node.next;

        return res;
    }

    private int lengthOfList(LinkedListNode n) {
        int size = 0;
        while (n != null) {
            size++;
            n = n.next;
        }
        return size;
    }

    public static class Result {
        public LinkedListNode node;
        public boolean result;

        public Result(LinkedListNode node, boolean result) {
            this.node = node;
            this.result = result;
        }
    }
}
