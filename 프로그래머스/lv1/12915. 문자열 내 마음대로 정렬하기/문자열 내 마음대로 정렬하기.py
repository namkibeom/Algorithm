def solution(strings, n):
    answer=[]
    answer2=[]
    for s in strings :
        answer.append(s[n]+s)
        print(answer)
    answer.sort()
    for j in answer :
        print(j[0])
        answer2.append(j[1:])
    print(answer2)
    return answer2