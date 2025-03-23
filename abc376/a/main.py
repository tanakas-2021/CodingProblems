N,C= map(int, input().split())
T = list(map(int, input().split()))

# 1回目のボタン押下は必ずもらえる
latest_time = T[0]
count = 1

# 2回目からのボタン押下
for i in range(1,N):
    if T[i] - latest_time >= C:
        latest_time = T[i]
        count +=1
    
print(count)