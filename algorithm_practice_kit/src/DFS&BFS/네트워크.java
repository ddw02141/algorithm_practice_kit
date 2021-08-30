// https://programmers.co.kr/learn/courses/30/lessons/43162
package DFS_BFS;

public class 네트워크 {

  static int N;
  static boolean[][] map;
  static boolean visited[];

  public static int solution(int n, int[][] computers) {
    N = n;
    visited = new boolean[N];
    map = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (computers[i][j] == 1 && i != j) {
          map[i][j] = true;
        }
      }
    }
    int answer = 0;
    for (int i = 0; i < N; i++) {
      if (!visited[i]) {
        answer++;
        dfs(i);
      }
    }
    return answer;
  }

  static void dfs(int idx) {
    if (visited[idx]) {
      return;
    }
    visited[idx] = true;
    for (int i = 0; i < N; i++) {
      if (!visited[i] && map[idx][i]) {
        dfs(i);
      }
    }
  }

  public static void main(String[] args) {
    System.out.println(solution(3, new int[][]{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}})); // Expect 2
    System.out.println(solution(3, new int[][]{{1, 1, 0}, {1, 1, 1}, {0, 1, 1}})); // Expect 1

  }
}
