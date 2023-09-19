def solution(price, money, count):
    answer = 0
    total = 0 
    for i in range (1, count+1):
        total += price*i
    answer = total - money 
    if answer <= 0 :
        answer = 0 
    return answer