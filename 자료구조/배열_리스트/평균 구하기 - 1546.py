N = input() # 테스트할 수의 개수
score = list(map(int, input().split())) # 점수 입력(공백 기준으로 받음)
maxscr = max(score) # 최대 점수

avgscore = sum(score) / maxscr * 100 / len(score) # 평균 점수

print(avgscore)