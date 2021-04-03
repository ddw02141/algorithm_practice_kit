// https://programmers.co.kr/learn/courses/30/lessons/49191
package Graph;

import java.util.ArrayList;
import java.util.List;

public class 순위 {

  static List<List<Integer>> wins = new ArrayList<>();
  static List<List<Integer>> loses = new ArrayList<>();
  static boolean[] visited;
  static int winCount, loseCount;

  public static int solution(int n, int[][] results) {
    int answer = 0;
    for (int i = 0; i <= n; i++) {
      wins.add(new ArrayList<>());
      loses.add(new ArrayList<>());
    }
    for (int[] result : results) {
      wins.get(result[0]).add(result[1]);
      loses.get(result[1]).add(result[0]);
    }
    for (int i = 1; i <= n; i++) {
      winCount = loseCount = 0;
      visited = new boolean[n + 1];
      winDfs(i);
      visited = new boolean[n + 1];
      loseDfs(i);
      if (winCount + loseCount == n - 1) {
        answer++;
      }
    }
    return answer;
  }

  static void winDfs(int node) {
    for (int weakNode : wins.get(node)) {
      if (visited[weakNode]) {
        continue;
      }
      visited[weakNode] = true;
      winCount++;
      winDfs(weakNode);
    }
  }

  static void loseDfs(int node) {
    for (int strongNode : loses.get(node)) {
      if (visited[strongNode]) {
        continue;
      }
      visited[strongNode] = true;
      loseCount++;
      loseDfs(strongNode);
    }
  }

  public static void main(String[] args) {
    System.out
        .println(solution(5, new int[][]{{4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}})); // Expect 2
  }
}
