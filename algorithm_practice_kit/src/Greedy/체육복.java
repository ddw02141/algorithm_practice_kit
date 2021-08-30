// https://programmers.co.kr/learn/courses/30/lessons/42862
package Greedy;

import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public class 체육복 {

  public static int solution(int n, int[] lost, int[] reserve) {
    int answer = 0;
    Set<Integer> l = Arrays.stream(lost).boxed().collect(Collectors.toSet());
    Set<Integer> r = Arrays.stream(reserve).boxed().collect(Collectors.toSet());
    for (int stu = 1; stu <= n; stu++) {
      boolean isInL = l.contains(stu);
      boolean isInR = r.contains(stu);
      if (!isInL) {
        answer++;
      } else {
        if (isInR) {
          r.remove(stu);
          answer++;
        } else if (r.contains(stu - 1) && !l.contains(stu - 1)) {
          r.remove(stu - 1);
          answer++;
        } else if (r.contains(stu + 1) && !l.contains(stu + 1)) {
          r.remove(stu + 1);
          answer++;
        }
      }
    }
    return answer;
  }

  public static void main(String[] args) {
    System.out.println(solution(5, new int[]{2, 4}, new int[]{1, 3, 5})); // Expect 5
    System.out.println(solution(5, new int[]{2, 4}, new int[]{3})); // Expect 4
    System.out.println(solution(3, new int[]{3}, new int[]{1})); // Expect 2
    System.out.println(solution(27, new int[]{10, 16, 19, 20, 24, 26, 27},
        new int[]{4, 7, 8, 10, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27})); // Expect 27

  }
}
