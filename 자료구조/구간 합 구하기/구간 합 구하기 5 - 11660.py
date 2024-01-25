import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 크기, 횟수
arr = [0] # 입력받을 배열 생성
sarr = [[0 for _ in range(N+1)] for _ in range(N+1)] # 구간 합을 저장할 배열 생성

for i in range(N):
  t = [0] + list(map(int, input().split())) # 계산이 편하도록 index 1부터 넣음
  arr.append(t)

for i in range(1, N+1):
  for j in range(1, N+1):
    sarr[i][j] = sarr[i-1][j] + sarr[i][j-1] - sarr[i-1][j-1] + arr[i][j] # 2차원 배열 합 공식

for i in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  rst = sarr[x2][y2] - sarr[x1-1][y2] - sarr[x2][y1-1] + sarr[x1-1][y1-1] # 2차원 배열 구간 합 공식
  print(rst)