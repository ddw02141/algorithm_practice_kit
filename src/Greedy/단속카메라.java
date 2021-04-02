package Greedy;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class 단속카메라 {

  static class Route {

    int from;
    int to;

    Route(int from, int to) {
      this.from = from;
      this.to = to;
    }
  }

  static List<Route> l;

  public static int solution(int[][] routes) {
    int answer = 0;
    int prevTo = -40000;
    l = new ArrayList<>();
    for (int[] route : routes) {
      l.add(new Route(route[0], route[1]));
    }
    l.sort(Comparator.comparingInt((Route r) -> r.from));
    for (Route r : l) {
      if (r.from <= prevTo) {
        prevTo = Math.min(prevTo, r.to);
        continue;
      }
      answer++;
      prevTo = r.to;
    }
    return answer;
  }

  public static void main(String[] args) {
    System.out
        .println(solution(new int[][]{{-20, 15}, {-14, -5}, {-18, -13}, {-5, -3}})); // Expect 2
    System.out.println(solution(new int[][]{{0, 0}, {0, 0}, {2, 2}})); // Expect 2
    System.out.println(solution(new int[][]{{0, 1}, {0, 1}, {2, 2}})); // Expect 2
  }
}
