import sys
input = sys.stdin.readline # 여러줄 입력 받기 위함

N, M = map(int, input().split()) # 개수와 횟수 입력받기
arr = list(map(int, input().split())) # 배열 입력받기
sumarr = [0] # 구간 합 저장 배열
t = 0 # 구간 합 저장 변수

for i in arr:
  t += i # 구간 합 계산 
  sumarr.append(t) # 배열에 저장

for i in range(M):
  x , y = map(int, input().split()) # 구간 입력받기
  print(sumarr[y] - sumarr[x-1]) # 구간 합 출력