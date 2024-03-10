package me.joohyuk.codinginterview.chapter02;

import java.util.Stack;

public class Problem06_02 {
    // 순환 접근

    boolean isPalindrome(LinkedListNode head) {
        LinkedListNode fast = head;
        LinkedListNode slow = head;

        Stack<Integer> stack = new Stack<>();

        /*
            연결리스트의 앞 절반을 스택에 쌓는다. fast runner(2배 빠른)가
            연결리스트 끝에 도달하면, slow runner가 중간에 도달했다는 것을 알 수 있다.
         */
        while (fast != null && fast.next != null) {
            stack.push(slow.data);
            slow = slow.next;
            fast = fast.next.next;
        }

        // 원소의 개수가 홀수 개라면 가운데 원소는 넘긴다.
        if (fast != null) {
            slow = slow.next;
        }

        while (slow != null) {
            int top = stack.pop().intValue();

            if (top != slow.data) {
                return false;
            }

            slow = slow.next;
        }

        return true;
    }
}
