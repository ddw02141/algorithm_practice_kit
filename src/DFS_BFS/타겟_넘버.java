// https://programmers.co.kr/learn/courses/30/lessons/43165
package DFS_BFS;

public class 타겟_넘버 {

  static int[] nums;
  static int n, t, answer;
  public static int solution(int[] numbers, int target) {
    t = target;
    n = numbers.length;
    nums = numbers;
    dfs(0, nums[0]);
    dfs(0, -nums[0]);
    return answer;
  }

  public static void dfs(int idx, int sum) {
    if (idx == n-1) {
      if (sum == t) answer++;
      return;
    }
    dfs(idx+1, sum + nums[idx+1]);
    dfs(idx+1, sum - nums[idx+1]);
  }

  public static void main(String[] args) {
    System.out.println(solution(new int[]{1,1,1,1,1}, 3)); // Expect 5
  }
}


