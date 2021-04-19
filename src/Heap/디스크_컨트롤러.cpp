// https://programmers.co.kr/learn/courses/30/lessons/42627
#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Job {
    public:
    int maxNowAndRequestTime;
    int now;
    int requestTime;
    int timeRequired;
    Job(int m, int n, int r, int t):maxNowAndRequestTime(m), now(n), requestTime(r), timeRequired(t) {}
};
struct compareJob {
    bool operator()(Job &j1, Job &j2) {
      if (j1.maxNowAndRequestTime == j2.maxNowAndRequestTime)
          return j1.timeRequired > j2.timeRequired;
      else return j1.maxNowAndRequestTime > j2.maxNowAndRequestTime;
  };
};
priority_queue<Job, vector<Job>, compareJob> pq;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int now = 0;
    pq = {};

    for(vector<int> job : jobs) pq.push(Job(job[0], 0, job[0], job[1]));
    while(!pq.empty()) {
        Job j = pq.top();
        pq.pop();
        if (now != j.now) {
            j.now = now;
            // cout << "j.now : " << j.now << endl;
            j.maxNowAndRequestTime = max(j.now, j.requestTime);
            pq.push(j);
            continue;
        }
        // cout << j.maxNowAndRequestTime << " " << j.now <<" " <<j.requestTime << " " << j.timeRequired << endl;
        if (now < j.requestTime) {
            now = j.requestTime;
        }
        answer += (now + j.timeRequired - j.requestTime);
        // cout << "answer += " << now + j.timeRequired - j.requestTime << endl;
        now += j.timeRequired;
        // cout << "now : " << now << endl;
    }
    return answer / jobs.size();
}