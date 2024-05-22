import java.io.*;
import java.util.*;

public class Main {
    static int[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int n;
    static int cnt;
    
    public static void dfs(int x, int y) {
        map[x][y] = 0;
        cnt++;
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < n && map[nx][ny] == 1)
                dfs(nx, ny);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        int answer = 0;
        
        for(int i = 0; i < n; i++) {
            String str = br.readLine();
            for(int j = 0; j < n; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }
        
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                cnt = 0;
                if(map[i][j] == 1) {
                    dfs(i, j);
                    arr.add(cnt);
                    answer++;
                }
            }
        }
        
        Collections.sort(arr);
        
        System.out.println(answer);
        for(int i : arr) {
            System.out.println(i);
        }
    }
}
