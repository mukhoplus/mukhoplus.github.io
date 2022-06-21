INF = 10001

N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

dp = [INF] * (M+1)
dp[0] = 0

# 화폐의 종류 별로 Bottom-Up DP 실행
for i in range(N):
    for j in range(money[i], M+1):
        if dp[j - money[i]] != INF: # 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - money[i]] + 1) # 동전의 개수가 하나씩 늘어남

print(dp[M] if dp[M] != INF else -1)
