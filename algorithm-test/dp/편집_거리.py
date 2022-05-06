#문자열 받기
str1 = input()
str2 = input()
    
n = len(str1)
m = len(str2)

#dp 테이블 초기화
dp = [[0] * (m+1) for _ in range(n+1)]

#dp 테이블 초기 설정
for i in range(1,n+1):
  dp[i][0] = i
for j in range(1,m+1):
  dp[0][j] = j


#최소 편집거리 계산
for i in range(1,n+1):
  for j in range(1,m+1):
    # 문자가 같으면, 왼쪽 위에 해당하는 수를 그대로 삽입
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

print(dp[n][m])
