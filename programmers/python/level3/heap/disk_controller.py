import heapq
from collections import deque

def find_jobs_in_time(jobs) :
    global time
    global pq

    while True:
        if jobs[0][0] <= time :
            job = jobs.popleft()
            heapq.heappush(pq, (job[1], job[0]))
            if not jobs:
                break
        else:
            break

def solution(jobs):
    global idx
    global time
    global pq

    jobs.sort()

    n = len(jobs)
    pq = []
    time = 0
    acc_time = 0
    jobs = deque(jobs)

    while jobs:
        find_jobs_in_time(jobs)
        if not pq:
            time = jobs[0][0]
            find_jobs_in_time(jobs)

        while pq:
            t, s = heapq.heappop(pq)
            acc_time += (time - s + t)
            time += t
            if jobs and time >= jobs[0][0] :
                break

    return acc_time // n
