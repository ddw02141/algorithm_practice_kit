// https://programmers.co.kr/learn/courses/30/lessons/43105
package DP;

public class 정수_삼각형 {

  static int[][] dp;
  public static int solution(int[][] triangle) {
    int height = triangle.length;
    dp = new int[height][height];
    dp[0][0] = triangle[0][0];
    for(int i=1;i<height;i++) {
      for(int j=0;j<=i;j++) {
        dp[i][j] = Math.max(dp[i][j], dp[i-1][j] + triangle[i][j]);
        if(j!=0) dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + triangle[i][j]);
      }
    }
    int answer = 0;
    for(int i=0;i<height;i++) answer = Math.max(answer, dp[height-1][i]);
    return answer;
  }

  public static void main(String[] args) {
    int[][] triangle = 	{{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
    System.out.println(solution(triangle)); // Expect 30
  }
}
