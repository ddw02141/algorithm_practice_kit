// https://programmers.co.kr/learn/courses/30/lessons/49189
package Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class 가장_먼_노드 {

  static class Pair {

    int node;
    int level;

    Pair(int node, int level) {
      this.node = node;
      this.level = level;
    }
  }

  static Queue<Pair> q;
  static List<List<Integer>> adj = new ArrayList<>();
  static int[] levels;

  public static int solution(int n, int[][] edge) {
    int answer = 0;
    q = new LinkedList<>();
    levels = new int[n + 1];
    for (int i = 0; i <= n; i++) {
      levels[i] = -1;
    }
    for (int i = 0; i <= n; i++) {
      adj.add(new ArrayList<>());
    }
    for (int[] e : edge) {
      adj.get(e[0]).add(e[1]);
      adj.get(e[1]).add(e[0]);
    }

    q.add(new Pair(1, 0));
    while (!q.isEmpty()) {
      Pair p = q.poll();
      if (levels[p.node] != -1) {
        continue;
      }

      levels[p.node] = p.level;
      for (int adjNode : adj.get(p.node)) {
        if (levels[adjNode] == -1) {
          q.add(new Pair(adjNode, p.level + 1));
        }
      }
    }
    int maxLevel = -1;
    for (int i = 1; i <= n; i++) {
      if (levels[i] > maxLevel) {
        maxLevel = levels[i];
      }
    }
    for (int i = 1; i <= n; i++) {
      if (levels[i] == maxLevel) {
        answer++;
      }
    }
    return answer;
  }

  public static void main(String[] args) {
    System.out.println(solution(6,
        new int[][]{{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}})); // Expect 3
  }
}
