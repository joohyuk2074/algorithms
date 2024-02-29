package me.joohyuk.codinginterview.chapter01;

public class Problem06_01 {
    public static String compressBad(String str) {
        StringBuilder compressedString = new StringBuilder();
        int countConsecutive = 0;
        for (int i = 0; i < str.length(); i++) {
            countConsecutive++;

            // 다음 문자와 현재 문자가 같지 않다면 현재 문자를 결과 문자열에 추가해준다.
            if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressedString.append("").append(str.charAt(i)).append(countConsecutive);
                countConsecutive = 0;
            }
        }
        return compressedString.length() < str.length() ? compressedString.toString() : str;
    }
}
