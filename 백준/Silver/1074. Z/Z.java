import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int leng = (int) Math.pow(2, n);
        
        recur(leng, r, c);
        
        System.out.println(answer);
    }
    
    public static void recur(int leng, int r, int c) {
        if(leng == 1) return;
        if(r < leng / 2 && c < leng / 2) {
            recur(leng / 2, r, c);
        } else if(r < leng / 2 && c >= leng / 2) {
            answer += leng * leng / 4;
            recur(leng / 2, r, c - leng / 2);
        } else if(r >= leng / 2 && c < leng / 2) {
            answer += (leng * leng / 4) * 2;
            recur(leng / 2, r - leng / 2, c);
        } else {
            answer += (leng * leng / 4) * 3;
            recur(leng / 2, r - leng / 2, c - leng / 2);
        }
    }
}