def solution(n, money):
    dp = [1] + [0] * n #1은 money에서의 자기자신 횟수+1
    for m in money: #m이라는 money 축 기준으로 횟수 늘어남
        for i in range(m, n+1):
            dp[i] = (dp[i] + dp[i-m]) % 1000000007 #dp[i-m]의 경우 현재 m 횟수랑 이전 m에 따라 더해진 횟수가 반영됨
    return dp[n]
#시간복잡도 = O(n), 공간복잡도 = O(n)
