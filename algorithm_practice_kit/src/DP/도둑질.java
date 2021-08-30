// https://programmers.co.kr/learn/courses/30/lessons/42897
package DP;

public class 도둑질 {

  public static int solution(int[] money) {
    int n = money.length;

    int[] dp = new int[n];
    boolean used = true;

    int[] dpR = new int[n];
    boolean usedR = true;

    dp[0] = money[0];
    dpR[n - 1] = money[n - 1];

    for (int i = 1; i < n; i++) {
      if (used) {
        int num = 0;
        if (i >= 2) {
          num += dp[i - 2];
        }
        num += money[i];
        if (num > dp[i - 1]) {
          dp[i] = num;
          used = true;
        } else {
          dp[i] = dp[i - 1];
          used = false;
        }
      } else {
        dp[i] = dp[i - 1] + money[i];
        used = true;
      }
    }

    for (int i = n - 2; i >= 0; i--) {
      if (usedR) {
        int num = 0;
        if (i + 2 < n) {
          num += dpR[i + 2];
        }
        num += money[i];
        if (num > dpR[i + 1]) {
          dpR[i] = num;
          usedR = true;
        } else {
          dpR[i] = dpR[i + 1];
          usedR = false;
        }
      } else {
        dpR[i] = dpR[i + 1] + money[i];
        usedR = true;
      }
    }

    if (used && usedR) {
      return Math.max(dp[money.length - 2], dpR[1]);
    } else {
      return dp[money.length - 1];
    }

  }


  public static void main(String[] args) {
    System.out.println(solution(new int[]{1, 2, 3, 1})); // Expect 4
    System.out.println(solution(new int[]{1, 5, 2, 3, 8, 4, 6, 7})); // Expect 20
    System.out.println(solution(new int[]{100, 5, 2, 3, 8, 4, 6, 100})); // Expect 116
  }
}
