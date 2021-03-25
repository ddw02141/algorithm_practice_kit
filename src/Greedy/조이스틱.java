// https://programmers.co.kr/learn/courses/30/lessons/42860
package Greedy;

public class 조이스틱 {

  public static int solution(String name) {
    int n = name.length();
    int change = name.chars().map(c -> Math.min(c - 'A', 'A' - c + 26)).sum();
    int route = n - 1;

    for (int i = 0; i < n; i++) {
      int next = i + 1;
      while (next < n && name.charAt(next) == 'A') {
        next++;
      }
      // next : i에서 가장 가까우면서 A가 아닌 곳의 index
      // ...(i)AAAAA(next)....
      // i와 next 사이의 A를 지나지 않는 경로 => 아래 계산식
      route = Math.min(route, i + n - next + Math.min(i, n - next));
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
    System.out.println(solution("AAABBBBBAA")); // Expect 12
  }
}
