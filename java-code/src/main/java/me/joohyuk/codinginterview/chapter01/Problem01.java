package me.joohyuk.codinginterview.chapter01;

import java.util.Arrays;
import java.util.HashSet;

public class Problem01 {

    boolean isUniqueChars1(String str) {
        if (str.length() > 128) {
            return false;
        }

        boolean[] charSet = new boolean[128];
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (charSet[val]) {
                return false;
            }
            charSet[val] = true;
        }
        return true;
    }

    boolean isUniqueChars2(String str) {
        int checker = 0;
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - 'a';
            if ((checker & (1 << val)) > 0) {
                return false;
            }
            checker |= (1 << val);
        }
        return true;
    }

    boolean isUniqueCharsIfUnicode(String str) {
        char[] charArray = str.toCharArray();
        Arrays.sort(charArray);

        for (int i = 0; i < charArray.length - 1; ++i) {
            if (charArray[i] == charArray[i + 1]) {
                return false;
            }
        }

        return true;
    }

    boolean isUniqueChars(String str) {
        HashSet<Character> set = new HashSet<Character>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            if (set.contains(c)) {
                return false;
            }

            set.add(c);
        }

        return true;
    }
}
