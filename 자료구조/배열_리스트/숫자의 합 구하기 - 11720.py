N = input() # 받을 숫자의 개수 받기
num = list(input()) # 숫자 리스트로 받기(파이썬에서는 배열과 리스트를 구분하지 않습니다.)
sum = 0 # N개의 합 생성 및 초기화

for i in num: # 배열 num의 값들을 더합니다.
  sum += int(i)

print(sum) # 출력