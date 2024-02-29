package me.joohyuk.codinginterview.chapter01;

import java.util.Arrays;

public class Problem02 {

    public String sort(String s) {
        char[] content = s.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }

    public boolean permutation1(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        return sort(s).equals(sort(t));
    }

    public boolean permutation2(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] letters = new int[128];    // ascii라고 가정

        char[] sArray = s.toCharArray();
        for (char c : sArray) {
            letters[c]++;
        }

        for (int i = 0; i < t.length(); i++) {
            int c = t.charAt(i);
            letters[c]--;
            if (letters[c] < 0) {
                return false;
            }
        }

        return true;
    }
}
