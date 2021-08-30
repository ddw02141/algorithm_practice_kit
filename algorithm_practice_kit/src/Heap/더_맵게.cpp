// https://programmers.co.kr/learn/courses/30/lessons/42626
#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
priority_queue< int, vector<int>, greater<int> > pq;

int solution(vector<int> scoville, int K) {
    for(int s:scoville) pq.push(s);
    int answer = 0;
    while(!pq.empty()){
        int min1 = pq.top();
        if (min1 >= K){
            break;
        }
        pq.pop();
        if (pq.empty() && min1 < K) return -1;
        int min2 = pq.top();
        pq.pop();
        if (min2 >= K) {
            answer++;
            break;
        }
        pq.push(min1 + min2*2);
        answer++;
    }
        
    return answer;
}