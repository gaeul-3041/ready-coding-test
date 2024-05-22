import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int tree[] = new int[n];
        long left = 0;
        long right = 0;

        for(int i = 0; i < n; i++) {
            tree[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, tree[i]);
        }
        
        while(left <= right) {
            long mid = (left + right) / 2;
            long cut = 0;
            
            for(int i: tree) {
                if(i > mid) cut += i - mid;
            }
            
            if(cut >= m) left = mid + 1;
            else right = mid - 1;
        }
        
        System.out.println(right);
    }
}