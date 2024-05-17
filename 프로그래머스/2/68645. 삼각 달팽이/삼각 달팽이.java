class Solution {
    public int[] solution(int n) {
        int[][] snail = new int[n][n];
        
        int x = -1;
        int y = 0;
        int num = 1;
        
        for(int i=0; i<n; i++) {
            for(int j=i; j<n; j++) {
                if(i % 3 == 0) {
                    x++;
                } else if(i % 3 == 1) {
                    y++;
                } else {
                    x--;
                    y--;
                }
                snail[x][y] = num++;
            }
        }
        
        int idx = 0;
        int[] answer = new int[num-1];
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(snail[i][j] == 0)
                    break;
                answer[idx++] = snail[i][j];
            }
        }
        
        return answer;
    }
}