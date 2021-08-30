// https://programmers.co.kr/learn/courses/30/lessons/43163
package DFS_BFS;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 단어_변환 {

  static class StringAndScore {

    String s;
    int score;

    StringAndScore(String s, int score) {
      this.s = s;
      this.score = score;
    }
  }

  static Queue<StringAndScore> q = new LinkedList<>();

  public static int solution(String begin, String target, String[] words) {
    if (Arrays.stream(words).noneMatch(e -> e.equals(target))) {
      return 0;
    }
    q.add(new StringAndScore(begin, 0));
    while (!q.isEmpty()) {
      StringAndScore ss = q.poll();
      if (ss.s.equals(target)) {
        return ss.score;
      }
      for (int i = 0; i < words.length; i++) {
        String word = words[i];
        if (calculateDiffCount(ss.s, word) == 1) {
          q.add(new StringAndScore(word, ss.score + 1));
        }
      }
    }

    return 0;
  }

  static int calculateDiffCount(String s1, String s2) {
    int diffCount = 0;
    for (int i = 0; i < s1.length(); i++) {
      if (s1.charAt(i) != s2.charAt(i)) {
        diffCount++;
      }
    }
    return diffCount;
  }

  public static void main(String[] args) {
    System.out
        .println(solution("hit", "cog",
            new String[]{"hot", "dot", "dog", "lot", "log", "cog"})); // Expect 4
    System.out.println(
        solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log"})); // Expect 0
  }
}
