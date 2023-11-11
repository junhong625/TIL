package Baekjoon.Silver;

import java.io.*;
import java.util.*;
//import 해줘야함
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringBuffer sf = new StringBuffer();
        String sentence = br.readLine();
        int idx = 0;
        boolean flag = false;
        String sub = "";
        while (idx < sentence.length()) {
            char c = sentence.charAt(idx);
            if (c == '<') {
                sb.append(sf.append(sub).reverse());
                sf.setLength(0);
                flag = true;
                sub = "";
            } else if (c == '>') {
                flag = false;
                sb.append(c);
                idx += 1;
                continue;
            }
            if (flag) {
                sb.append(c);
            } else {
                if (c == ' ') {
                    sb.append(sf.append(sub).reverse());
                    sf.setLength(0);
                    sb.append(c);
                    sub = "";
                } else {
                    sub += c;
                }
            }
            idx += 1;
        }
        if (!sub.isEmpty()) {
            sb.append(sf.append(sub).reverse());
        }
        System.out.println(sb);
    }
}