import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int answer = 0;
        int n = Integer.parseInt(br.readLine());
        int schedule[][] = new int[n][2];
        
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            schedule[i][0] = Integer.parseInt(st.nextToken());
            schedule[i][1] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(schedule, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                if(o1[1] == o2[1]) return o1[0] - o2[0];
                else return o1[1] - o2[1];
            }
        });
        
        int nxt = -1;
        for(int i = 0; i < n; i++) {
            if(schedule[i][0] >= nxt) {
                nxt = schedule[i][1];
                answer++;
            }
        }
        
        System.out.println(answer);
    }
}