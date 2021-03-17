// https://programmers.co.kr/learn/courses/30/lessons/42898
package DP;

public class 등굣길 {

  static int MAX = 1_000_000_007;
  static int PUDDLE = -1;
  static int dp[][];

  public static int solution(int m, int n, int[][] puddles) {
    int answer = 0;
    dp = new int[n][m];
    for (int i = 0; i < puddles.length; i++) {
      int[] puddle = puddles[i];
      dp[puddle[1] - 1][puddle[0] - 1] = PUDDLE;
    }
    for (int i = 0; i < n; i++) {
      if (dp[i][0] == PUDDLE) {
        break;
      }
      dp[i][0] = 1;
    }
    for (int j = 0; j < m; j++) {
      if (dp[0][j] == PUDDLE) {
        break;
      }
      dp[0][j] = 1;
    }
    for (int i = 1; i < n; i++) {
      for (int j = 1; j < m; j++) {
        if (dp[i][j] == PUDDLE) {
          continue;
        }
        if (dp[i - 1][j] == PUDDLE && dp[i][j - 1] == PUDDLE) {
          continue;
        } else if (dp[i - 1][j] == PUDDLE) {
          dp[i][j] = dp[i][j - 1];
        } else if (dp[i][j - 1] == PUDDLE) {
          dp[i][j] = dp[i - 1][j];
        } else {
          dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MAX;
        }
      }
    }

    return dp[n - 1][m - 1];
  }

  public static void main(String[] args) {
    int[][] puddles = {{2, 2}};
    System.out.println(solution(4, 3, puddles)); // Expect 4
  }
}
