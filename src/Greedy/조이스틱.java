package Greedy;

import java.util.ArrayList;
import java.util.List;

public class 조이스틱 {

  public static int solution(String name) {
    int n = name.length();
    int change = name.chars().map(c -> Math.min(c - 'A', 'A' - c + 26)).sum();
    if (change == 0) {
      return change;
    }
    int route = n - 1;
    List<Integer> l = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      if (name.charAt(i) != 'A') {
        l.add(i);
      }
    }
    if (l.size() == 1) {
      route = Math.min(route, Math.min(l.get(0), n - l.get(0)));
    } else {
      route = Math.min(route, l.get(l.size() - 1));
      route = Math.min(route, n - l.get(0));
      for (int idx = 0; idx < l.size() - 1; idx++) {
        int start = l.get(idx);
        int end = l.get(idx + 1);
        route = Math.min(route, start + (n + start - end));
      }
    }
    return change + route;

  }

  public static void main(String[] args) {
    System.out.println(solution("JEROEN")); // Expect 56
    System.out.println(solution("JAN")); // Expect 23
    System.out.println(solution("AAAAAAAAAA")); // Expect 0
    System.out.println(solution("AAAAAAAAAB")); // Expect 2
    System.out.println(solution("BAAAAAAAAA")); // Expect 1
    System.out.println(solution("AAAAABAAAA")); // Expect 6
    System.out.println(solution("AAAAZZAAAA")); // Expect 7
    System.out.println(solution("ABABABABAB")); // Expect 14
    System.out.println(solution("AABAABAABB")); // Expect 12
  }
}
