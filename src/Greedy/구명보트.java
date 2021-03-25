// https://programmers.co.kr/learn/courses/30/lessons/42885
package Greedy;

import java.util.Arrays;
import java.util.stream.IntStream;

public class 구명보트 {

  public static int solution(int[] people, int limit) {
    int answer = 0;
    int left = 0;
    int right = people.length - 1;
    Arrays.sort(people);
    int[] p = IntStream.range(0, people.length).map(i -> people[people.length - i - 1]).toArray();

    while (left <= right) {
      if (p[left] + p[right] > limit) {
        left++;
      } else {
        left++;
        right--;
      }
      answer++;
    }
    return answer;
  }

  public static void main(String[] args) {
    System.out.println(solution(new int[]{70, 50, 80, 50}, 100)); // Expect 3
    System.out.println(solution(new int[]{70, 80, 50}, 100)); // Expect 3
    System.out
        .println(solution(new int[]{60, 30, 20, 20, 10, 10, 10, 10, 10, 10, 10}, 100)); // Expect 6
    System.out.println(solution(new int[]{40, 40, 40}, 120)); // Expect 2
    System.out.println(solution(new int[]{160, 150, 140, 60, 50, 40}, 200)); // Expect 3
  }
}
