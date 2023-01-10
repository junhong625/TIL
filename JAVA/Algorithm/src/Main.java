import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

//import 해줘야함
public class Main {
    public static int[] bfs(int i, int j, int R, int C, int[][] visited, String[][] grid) {
        ArrayList<int[]> q = new ArrayList<>();
        int[][] delta = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        int idx = -1;
        int sheep = 0, wolf = 0;
        visited[i][j] = 1;
        q.add(new int[] {i, j});

        while (q.size() > idx) {
            idx++;
            int x = q.get(idx)[0];
            int y = q.get(idx)[1];
            System.out.println(x + " " + y);
            if (Objects.equals(grid[x][y], 'o')){
                sheep++;
            } else if (Objects.equals(grid[x][y], 'v')) {
                wolf++;
            }
            for (int[] d : delta){
                int dx = d[0], dy = d[1];
                dx += x;
                dy += y;
                if (0 <= dx & dx < R & 0 <= dy & dy < C & Objects.equals(visited[dx][dy], 1) & Objects.equals(grid[dx][dy], '#')) {
                    visited[dx][dy] = 1;
                    q.add(new int[] {dx, dy});
                }
            }
        }
        if (sheep < wolf) {
            return new int[] {sheep, 0};
        }
        else {
            return new int[] {0, wolf};
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken()), C = Integer.parseInt(st.nextToken());
        String[][] backYard = new String[R][C];
        int[][] visited = new int[R][C];
        int sheep = 0, wolf = 0;
        for (int i=0; i < R; i++) {
            String line = br.readLine();
            for (int j=0; j < line.length(); j++) {
                backYard[i][j] = String.valueOf(line.charAt(j));
            }
        }
        for (int i=0; i < R; i++) {
            for (int j=0; j < C; j++) {
                int[] result = bfs(i,j,R,C, visited, backYard);
                    sheep += result[0];
                    wolf += result[1];
            }
        }
        System.out.printf("%d %d", sheep, wolf);
//        bw.write();
//        bw.flush();
//        bw.close();
    }
}