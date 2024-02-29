package me.joohyuk.codinginterview.chapter01;

public class Problem03 {

    // 1. 최종 문자열에 추가 공간이 얼마나 필요한지 계산
    public static void replaceSpaces(char[] str, int trueLength) {
        int spaceCount = 0;
        int index = 0;
        int i = 0;

        for (i = 0; i < trueLength; i++) {
            if (str[i] == ' ') {
                spaceCount++;
            }
        }

        index = trueLength + spaceCount * 2;
        if (trueLength < str.length) {
            str[trueLength] = '\0';
        }

        for (i = trueLength - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[index - 1] = '0';
                str[index - 2] = '2';
                str[index - 3] = '%';
                index -= 3;
            } else {
                str[index - 1] = str[i];
                index--;
            }
        }

        for (char c : str) {
            System.out.print(c);
        }
    }

    // 2. 역방향으로 진행하면서 실제로 문자열을 편집
    public static void main(String[] args) {
        String input = "Mr John Smith";
        replaceSpaces(input.toCharArray(), 13);
    }
}
