import java.io.*;
import java.util.*;

public class Main {
    static int[][] network;
    static int[] visited;
    static int answer = 0;
    static int n, k;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        
        network = new int[n+1][n+1];
        visited = new int[n+1];
        
        for(int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            network[a][b] = 1;
            network[b][a] = 1;
        }
        
        dfs(1);
        System.out.println(answer-1);
    }
    
    public static void dfs(int v) {
        visited[v] = 1;
        answer++;
        
        for(int i = 1; i < n+1; i++) {
            if(network[v][i] == 1 && visited[i] == 0)
                dfs(i);
        }
    }
}