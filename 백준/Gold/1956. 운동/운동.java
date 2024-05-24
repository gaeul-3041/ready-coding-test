import java.io.*;
import java.util.*;

public class Main {
    static int[][] city;
    static int INF = 999999999;
    static int answer = INF;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        city = new int[v+1][v+1];
        
        for(int i = 1; i < v+1; i++) {
            for(int j = 1; j < v+1; j++) {
                if(i != j) city[i][j] = INF;
            }
        }
        
        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            city[a][b] = c;
        }
        
        for(int k = 1; k < v+1; k++) {
            for(int i = 1; i < v+1; i++) {
                for(int j = 1; j < v+1; j++) {
                    if(i == j || i == k || j == k) continue;
                    city[i][j] = Math.min(city[i][j], city[i][k] + city[k][j]);
                }
            }
        }
        
        for(int i = 1; i < v+1; i++) {
            for(int j = 1; j < v+1; j++) {
                if(i == j) continue;
                if(city[i][j] != INF && city[j][i] != INF) {
                    answer = Math.min(answer, city[i][j] + city[j][i]);
                }
            }
        }
        
        if(answer == INF) System.out.println(-1);
        else System.out.println(answer);
    }
}