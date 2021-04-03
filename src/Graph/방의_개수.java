// https://programmers.co.kr/learn/courses/30/lessons/49190
package Graph;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

public class 방의_개수 {

  static class Pair {

    int x, y;

    Pair(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public int hashCode() {
      return Objects.hash(x, y);
    }

    @Override
    public boolean equals(Object obj) {
      if (this == obj) {
        return true;
      }
      if (obj == null || getClass() != obj.getClass()) {
        return false;
      }
      return ((Pair) obj).x == x && ((Pair) obj).y == y;
    }

    @Override
    public String toString() {
      return "Pair{" +
          "x=" + x +
          ", y=" + y +
          '}';
    }
  }

  static int[][] move = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
  static Set<Pair> visitedVertex;
  static Map<Pair, Set<Pair>> visitedEdge;

  public static int solution(int[] arrows) {
    int answer = 0;
    visitedVertex = new HashSet<>();
    visitedEdge = new HashMap<>();
    Pair cur = new Pair(0, 0);
    Pair prev;
    visitedVertex.add(new Pair(cur.x, cur.y));
    for (int arrow : arrows) {
      prev = new Pair(cur.x, cur.y);
      cur.x += move[arrow][0];
      cur.y += move[arrow][1];
      if (visitedVertex.contains(new Pair(cur.x, cur.y)) &&
          ((!(visitedEdge.containsKey(new Pair(prev.x, prev.y)))) ||
              (!(visitedEdge.get(new Pair(prev.x, prev.y)).contains(new Pair(cur.x, cur.y)))))) {
        answer++;
      }
      visitedVertex.add(new Pair(cur.x, cur.y));
      if (!(visitedEdge.containsKey(new Pair(prev.x, prev.y)))) {
        visitedEdge.put(new Pair(prev.x, prev.y), new HashSet<>());
      }
      visitedEdge.get(new Pair(prev.x, prev.y)).add(new Pair(cur.x, cur.y));
      if (!(visitedEdge.containsKey(new Pair(cur.x, cur.y)))) {
        visitedEdge.put(new Pair(cur.x, cur.y), new HashSet<>());
      }
      visitedEdge.get(new Pair(cur.x, cur.y)).add(new Pair(prev.x, prev.y));

      prev = new Pair(cur.x, cur.y);
      cur.x += move[arrow][0];
      cur.y += move[arrow][1];
      if (visitedVertex.contains(new Pair(cur.x, cur.y)) &&
          ((!(visitedEdge.containsKey(new Pair(prev.x, prev.y)))) ||
              (!(visitedEdge.get(new Pair(prev.x, prev.y)).contains(new Pair(cur.x, cur.y)))))) {
        answer++;
      }
      visitedVertex.add(new Pair(cur.x, cur.y));
      if (!(visitedEdge.containsKey(new Pair(prev.x, prev.y)))) {
        visitedEdge.put(new Pair(prev.x, prev.y), new HashSet<>());
      }
      visitedEdge.get(new Pair(prev.x, prev.y)).add(new Pair(cur.x, cur.y));
      if (!(visitedEdge.containsKey(new Pair(cur.x, cur.y)))) {
        visitedEdge.put(new Pair(cur.x, cur.y), new HashSet<>());
      }
      visitedEdge.get(new Pair(cur.x, cur.y)).add(new Pair(prev.x, prev.y));

    }
    return answer;
  }

  public static void main(String[] args) {
    System.out.println(
        solution(new int[]{6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0})); // Expect 3
    System.out.println(
        solution(new int[]{6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5})); // Expect 3
    System.out.println(
        solution(new int[]{6, 5, 2, 7, 1, 4, 2, 4, 6})); // Expect 3
    System.out.println(
        solution(new int[]{5, 2, 7, 1, 6, 3})); // Expect 3
    System.out.println(
        solution(new int[]{6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0})); // Expect 3
  }
}
