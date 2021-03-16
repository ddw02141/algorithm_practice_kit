package DP;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class N으로_표현 {
  static List<Set<Integer>> l = new ArrayList();
  public static int solution(int N, int number) {
    int answer = -1;
    for(int i=0;i<9;i++) l.add(new HashSet());

    l.get(1).add(N);

    for(int i=2;i<=8;i++) {
      int i1 = Integer.parseInt(Integer.toBinaryString((int)Math.pow(2, i) - 1));
//      System.out.println("i1 : " + i1);
      l.get(i).add(i1 * N);
      for(int x=1;x<=i;x++) {
        int y = i - x;
        if (x > y) break;
//        System.out.printf("i : %d x : %d y: %d\n", i, x, y);
         for(int xx:l.get(x)) {
             for(int yy:l.get(y)) {
                 l.get(i).add(sum(xx,yy));
                 l.get(i).add(sub(xx,yy));
                 l.get(i).add(subR(xx,yy));
                 l.get(i).add(mul(xx,yy));
                 if(yy!=0) l.get(i).add(div(xx,yy));
                 if(xx!=0) l.get(i).add(divR(xx,yy));
             }
         }
      }
    }
    for(int i=1;i<=8;i++) {
      if(l.get(i).contains(number)) {
        answer = i;
        break;
      }
    }

    return answer;
  }
  public static int sum(int a, int b) { return a + b; }
  public static int sub(int a, int b) { return a - b; }
  public static int subR(int a, int b) { return b - a; }
  public static int mul(int a, int b) { return a * b; }
  public static int div(int a, int b) { return a / b; }
  public static int divR(int a, int b) { return b / a; }

  public static void main(String[] args) {
    System.out.println(solution(5,12)); // Expect 4
    System.out.println(solution(2,11)); // Expect 3
    System.out.println(solution(5,31168)); // Expect -1
  }
}


