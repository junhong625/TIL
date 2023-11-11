import java.io.*;
import java.util.*;

//import 해줘야함
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int R1 = Integer.parseInt(st.nextToken());
        int C1 = Integer.parseInt(st.nextToken());
        int R2 = Integer.parseInt(st.nextToken());
        int C2 = Integer.parseInt(st.nextToken());
        ArrayList<Character> alphabet = new ArrayList<>();
        int a = 'a';
        for (int i = 0; i < N; i++) {
            alphabet.add((char) (a + i));
        }
        int dia = 2 * N - 1;
        for (int i = R1; i <= R2; i++) {
            for (int j = C1; j <= C2; j++) {
                int x = i % dia;
                int y = j % dia;
                int dis = Math.abs(N - 1 - x) + Math.abs(N - 1 - y);
                sb.append((dis > N - 1) ? '.' : alphabet.get(dis % 26));
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}