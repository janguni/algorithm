def solution(id_list, report, k):
    num=len(id_list)
    
    dp = [[0 for j in range(num)] for i in range(num)]
    
    for users in report:
        a,b = users.split() # a가 신고자, b가 신고당한 사람
        a_index = id_list.index(a)
        b_index = id_list.index(b)
        if dp[a_index][b_index] == 0:
            dp[a_index][b_index] = 1
        else:
            continue
            
    reported=[0] * num
    for i in range(num):
        for j in range(num):
            if dp[i][j] == 1:
                sum = reported[j] + 1
                reported[j] = sum

    
    for i in range(num):
        if reported[i]<k:
            reported[i]=0
    
    answer=[0] * num
    for i in range(num):
        for j in range(num):
            if dp[i][j]==1:
                if reported[j]>=k:
                    answer[i]+=1
    return answer