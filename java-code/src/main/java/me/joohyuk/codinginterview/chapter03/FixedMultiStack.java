package me.joohyuk.codinginterview.chapter03;

import java.util.EmptyStackException;

public class FixedMultiStack {
    // 고정 크기 할당
    private int numberOfStacks = 3;
    private int stackCapacity;
    private int[] values;
    private int[] sizes;

    public FixedMultiStack(int stackSize) {
        stackCapacity = stackSize;
        values = new int[stackSize * numberOfStacks];
        sizes = new int[numberOfStacks];
    }

    // 스택에 값을 추가한다.
    public void push(int stackNum, int value) {
        // 여유 공간이 있는지 검사한다.
        if (isFull(stackNum)) {
            throw new RuntimeException();
        }

        //스택 포인터를 증가시키고 가장 꼭대기 값을 갱신한다.
        sizes[stackNum]++;
        values[indexOfTop(stackNum)] = value;
    }

    // 스택에서 값을 꺼낸다.
    public int pop(int stackNum) {
        if (isEmpty(stackNum)) {
            throw new RuntimeException();
        }

        int topIndex = indexOfTop(stackNum);
        int value = values[topIndex];
        values[topIndex] = 0;
        sizes[stackNum]--;
        return value;
    }

    // 꼭대기 원소를 반환한다.
    public int peek(int stackNum) {
        if (isEmpty(stackNum)) {
            throw new EmptyStackException();
        }

        return values[indexOfTop(stackNum)];
    }

    private boolean isEmpty(int stackNum) {
        return sizes[stackNum] == 0;
    }

    private boolean isFull(int stackNum) {
        return sizes[stackNum] == stackCapacity;
    }

    private int indexOfTop(int stackNum) {
        int offset = stackNum * stackCapacity;
        int size = sizes[stackNum];
        return offset + size - 1;
    }
}
