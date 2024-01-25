import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sarr = [0 for _ in range(n)] # 구간 합 배열
marr = [0 for _ in range(m)] # m으로 나눈 나머지
result = 0

sarr[0] = arr[0] # 구간 합의 첫번째
for i in range(1, n):
  sarr[i] = sarr[i-1] + arr[i] # 구간 합

for i in range(n):
  if sarr[i] % m == 0: # 나눠지면 ++
    result += 1
  marr[sarr[i] % m] += 1 # marrr에 알맞게 저장

for i in range(m):
  if marr[i] >= 2: 
    result += (marr[i] * (marr[i]-1) // 2) # (s[j] - s[i]) % m = 0 일경우 

print(result)