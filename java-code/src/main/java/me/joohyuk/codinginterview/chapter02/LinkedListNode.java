package me.joohyuk.codinginterview.chapter02;

public class LinkedListNode {

    public LinkedListNode next = null;
    public int data;

    public LinkedListNode(int data) {
        this.data = data;
    }

    public LinkedListNode() {
    }

    void appendToTail(int d) {
        LinkedListNode end = new LinkedListNode(d);
        LinkedListNode n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = end;
    }

    public void setNext(LinkedListNode more) {
        this.next = more;
    }
}
