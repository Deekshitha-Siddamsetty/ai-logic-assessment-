n=int(input())
intervals=[]

for i in range(n):

    start,end=map(int,input().split())
    intervals.append([start,end])

intervals.sort()
merged=[]

for start,end in intervals:
    if not merged or start>merged[-1][1]:
        intervals.append([start,end])

    else:
        merged=intervals.append(max(merged[-1][1]))

for start,end in merged:
    print(start,end)
