// https://programmers.co.kr/learn/courses/30/lessons/43164
package DFS_BFS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class 여행_경로 {

  // 공항은 최대 10,000개
  // 티켓은 최대 ?개
  // 효율성 검사가 없는 문제라 생각없이 풀면 되는 듯?
  // 같은 경로의 티켓이 존재할수도 있을까?

  static class Route {

    String airPort;
    int num;
    Map<String, Integer> used;

    Route(String a, int n, Map<String, Integer> u) {
      this.airPort = a;
      this.num = n;
      this.used = u;
    }

    @Override
    public String toString() {
      return "Route{" +
          "airPort='" + airPort + '\'' +
          ", num=" + num +
          ", used=" + used +
          '}';
    }
  }

  static Map<String, List<String>> m;
  static Map<String, Integer> used, currentUsed;
  static Queue<Route> q;
  static int t;
  static Route answerRoute = null;

  public static String[] solution(String[][] tickets) {
    t = tickets.length;
    m = new HashMap<>();
    used = new HashMap<>();
    q = new LinkedList<>();
    for (String[] ticket : tickets) {
      if (!m.containsKey(ticket[0])) {
        m.put(ticket[0], new ArrayList<>());
      }
      m.get(ticket[0]).add(ticket[1]);
      used.put((ticket[0] + ticket[1]), 0);
    }

    for (String key : m.keySet()) {
      List<String> value = m.get(key);
      Collections.sort(value);
      m.put(key, value);
    }

    q.add(new Route("ICN", 1, used));

    while (!q.isEmpty()) {
      Route route = q.poll();
//      System.out.println(route.toString());
      if (route.num == t + 1) {
        answerRoute = route;
        break;
      }
      if (!m.containsKey(route.airPort)) {
        continue;
      }
      for (String arrival : m.get(route.airPort)) {
        currentUsed = new HashMap<>(route.used);
        String ticket = route.airPort + arrival;
        if (currentUsed.get(ticket) != 0) {
          continue;
        }
        currentUsed.put(ticket, route.num);
        q.add(new Route(arrival, route.num + 1, currentUsed));
      }
    }
    String[] answer = new String[t + 1];
    answer[0] = "ICN";
    for (String ticket : answerRoute.used.keySet()) {
      Integer num = answerRoute.used.get(ticket);
      answer[num] = ticket.substring(3);
    }

    return answer;
  }

  public static void main(String[] args) {
    System.out.println(Arrays.toString(solution(
        new String[][]{{"ICN", "AAA"}, {"AAA", "BBB"}, {"BBB", "CCC"}, {"CCC", "ICN"},
            {"ICN", "DDD"},
            {"DDD", "ICN"}, {"ICN", "DDD"},
            {"DDD",
                "ICN"}}))); // Expect ["ICN", "AAA", "BBB", "CCC", "ICN", "DDD", "ICN", "DDD", "ICN"]
    System.out.println(Arrays.toString(solution(
        new String[][]{{"ICN", "DDD"}, {"DDD", "BBB"}, {"BBB", "CCC"}, {"CCC", "ICN"},
            {"ICN", "AAA"},
            {"AAA", "ICN"}, {"ICN", "AAA"},
            {"AAA",
                "ICN"}}))); // Expect ["ICN", "AAA", "ICN", "AAA", "ICN", "DDD", "BBB", "CCC", "ICN"]
    System.out.println(Arrays.toString(solution(
        new String[][]{{"ICN", "JFK"}, {"HND", "IAD"},
            {"JFK", "HND"}}))); // Expect ["ICN", "JFK", "HND", "IAD"]
    System.out.println(Arrays.toString(solution(
        new String[][]{{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"},
            {"ATL", "SFO"}}))); // Expect ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
  }
}
