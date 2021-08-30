// https://programmers.co.kr/learn/courses/30/lessons/43164
package DFS_BFS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
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
    List<Ticket> used;

    Route(String a, int n, List<Ticket> u) {
      this.airPort = a;
      this.num = n;
      this.used = u;
    }
  }

  static class Ticket {

    String departure;
    String arrival;

    int order;

    Ticket(String d, String a, int o) {
      this.departure = d;
      this.arrival = a;
      this.order = o;
    }

    @Override
    public boolean equals(Object o) {
      Ticket other = (Ticket) o;
      return departure.equals(other.departure) && arrival.equals(other.arrival);
    }
  }

  static class TicketComparator implements Comparator<Ticket> {

    @Override
    public int compare(Ticket t1, Ticket t2) {
      if (t1.departure.compareTo(t2.departure) == 0) {
        return t1.arrival.compareTo(t2.arrival);
      } else {
        return t1.departure.compareTo(t2.departure);
      }
    }
  }

  static Map<String, List<String>> m;
  static List<Ticket> used, currentUsed;
  static Queue<Route> q;
  static int t;
  static Route answerRoute = null;

  public static String[] solution(String[][] tickets) {
    t = tickets.length;
    m = new HashMap<>();
    used = new ArrayList<>();
    q = new LinkedList<>();
    for (String[] ticket : tickets) {
      if (!m.containsKey(ticket[0])) {
        m.put(ticket[0], new ArrayList<>());
      }
      m.get(ticket[0]).add(ticket[1]);
      used.add(new Ticket(ticket[0], ticket[1], -1));
    }

    for (String key : m.keySet()) {
      List<String> value = m.get(key);
      Collections.sort(value);
      m.put(key, value);
    }

    used.sort(new TicketComparator());

    q.add(new Route("ICN", 1, used));

    while (!q.isEmpty()) {
      Route route = q.poll();
      if (route.num == t + 1) {
        answerRoute = route;
        break;
      }
      if (!m.containsKey(route.airPort)) {
        continue;
      }
      for (String arrival : m.get(route.airPort)) {
        currentUsed = new ArrayList<>(route.used);
        Ticket nextTicket = new Ticket(route.airPort, arrival, route.num);
        for (int i = 0; i < currentUsed.size(); i++) {
          if (nextTicket.equals(currentUsed.get(i))) {
            if (currentUsed.get(i).order != -1) {
              continue;
            }
            currentUsed.set(i, nextTicket);
            q.add(new Route(arrival, route.num + 1, currentUsed));
            break;
          }
        }
      }
    }
    String[] answer = new String[t + 1];
    answer[0] = "ICN";
    for (Ticket ticket : answerRoute.used) {
      answer[ticket.order] = ticket.arrival;
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
