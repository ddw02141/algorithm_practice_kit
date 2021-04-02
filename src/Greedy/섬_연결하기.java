// https://programmers.co.kr/learn/courses/30/lessons/42861
package Greedy;

import java.util.Comparator;
import java.util.PriorityQueue;

public class 섬_연결하기 {

  static class Road {

    int x, y, cost;

    Road(int x, int y, int cost) {
      this.x = x;
      this.y = y;
      this.cost = cost;
    }
  }

  static int unionFind(int node) {
    if (node == parent[node]) {
      return node;
    } else {
      return parent[node] = unionFind(parent[node]);
    }
  }

  static int[] parent;
  static PriorityQueue<Road> pq;
  static boolean[][] map;
  static boolean[] visited;
  static int N;

  public static int solution(int n, int[][] costs) {
    int answer = 0;
    N = n;
    pq = new PriorityQueue<>(Comparator.comparingInt(r -> r.cost));
    map = new boolean[n][n];
    visited = new boolean[n];
    parent = new int[n];
    for (int i = 0; i < n; i++) {
      parent[i] = i;
    }
    for (int[] c : costs) {
      pq.add(new Road(c[0], c[1], c[2]));
    }
    while (true) {
      Road r = pq.poll();
      int ux = unionFind(r.x);
      int uy = unionFind(r.y);
      if (unionFind(r.x) == unionFind(r.y)) {
        continue;
      }
      answer += r.cost;
      parent[unionFind(r.y)] = unionFind(r.x);
      map[r.x][r.y] = true;
      map[r.y][r.x] = true;
      dfs(r.x);
      dfs(r.y);
      if (isAllConnected()) {
        break;
      }
    }

    return answer;
  }

  static void dfs(int node) {
    if (visited[node]) {
      return;
    }
    visited[node] = true;
    for (int i = 0; i < N; i++) {
      if (map[node][i] && !visited[i]) {
        dfs(i);
      }
    }
  }

  static boolean isAllConnected() {
    for (int i = 0; i < N - 1; i++) {
      if (unionFind(i) != unionFind(i + 1)) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    System.out.println(solution(4,
        new int[][]{{0, 1, 1}, {0, 2, 2}, {1, 2, 5}, {1, 3, 1}, {2, 3, 8}})); // Expect 4
    System.out.println(solution(5,
        new int[][]{{0, 1, 5}, {1, 2, 3}, {2, 3, 3}, {3, 1, 2}, {3, 0, 4}, {2, 4, 6},
            {4, 0, 7}})); // Expect 15
    System.out.println(solution(5,
        new int[][]{{0, 1, 1}, {0, 4, 5}, {2, 4, 1}, {2, 3, 1}, {3, 4, 1}})); // Expect 8
  }

}
