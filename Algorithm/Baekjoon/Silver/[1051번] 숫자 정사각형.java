import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<String> square = new ArrayList<>();
        int maxV = 0;
        for (int i = 0; i < N; i++) {
            square.add(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int w = maxV;
                char std = square.get(i).charAt(j);
                while (true) {
                    if (i + w >= N || j + w >= M) {
                        break;
                    }
                    if (std == square.get(i).charAt(j + w) & std == square.get(i + w).charAt(j) & std == square.get(i + w).charAt(j + w)) {
                        maxV = Math.max(maxV, w+1);
                    }
                    w += 1;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append((maxV) * (maxV));
        System.out.println(sb);
    }
}