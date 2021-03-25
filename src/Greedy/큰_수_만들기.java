// https://programmers.co.kr/learn/courses/30/lessons/42883
// 풀이 참고 : https://gurumee92.tistory.com/162
package Greedy;

import java.util.ArrayList;
import java.util.List;

public class 큰_수_만들기 {

  // 나는 min heap으로 버릴 숫자를 추려낼려고 했는데
  // collected라는 배열에 숫자를 한 개씩 넣으면서 마지막 값이랑 새로운 값 비교
  // collected의 마지막 원소의 값이 작으면 => 제거 => 다시 마지막 값과 새로운 값 비교
  // 새로운 값이 작으면 => 배열에 넣기
  // 이렇게 하면 내림 차순을 만들 수 있네...

  public static String solution(String number, int k) {
    int len = number.length();
    List<Integer> l = new ArrayList<>();
    List<Integer> c = new ArrayList<>();
    for (int i = 0; i < len; i++) {
      int n = number.charAt(i) - '0';
      l.add(n);
    }
    c.add(l.get(0));
    int idx = 1;
    while (k > 0 && idx < len) {
      if (c.get(c.size() - 1) <= l.get(idx)) {
        while (!c.isEmpty() && c.get(c.size() - 1) < l.get(idx) && k > 0) {
          c.remove(c.size() - 1);
          k--;
        }
      }
      c.add(l.get(idx));
      idx++;
    }
    while (idx < len) {
      c.add(l.get(idx));
      idx++;
    }
    StringBuilder answer = new StringBuilder();
    for (Integer ce : c) {
      answer.append(ce);
    }
    return answer.substring(0, answer.length() - k);
  }

  public static void main(String[] args) {
    System.out.println(solution("1924", 2)); // Expect "94"
    System.out.println(solution("1231234", 3)); // Expect 3234
    System.out.println(solution("4177252841", 4)); // Expect 775841
    System.out.println(solution("4177912841", 4)); // Expect 912841
    System.out.println(solution("41987654321", 4)); // Expect 9876543
    System.out.println(solution("55555", 2)); // Expect 555
  }
}
