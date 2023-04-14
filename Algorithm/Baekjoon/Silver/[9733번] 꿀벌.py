import sys 

input = sys.stdin.readline

flag = False

printList = ["Re","Pt","Cc","Ea","Tb","Cm","Ex"]
job_avg = {}
cnt = 0

for _ in range(2):
    if flag:
        break
    jobs = input()
    if jobs.endswith(" "):
        flag = True
    jobs = jobs.split(" ")
    for job in jobs:
        if job not in job_avg.keys():
            job_avg[job] = 1
        else:
            job_avg[job] += 1
        