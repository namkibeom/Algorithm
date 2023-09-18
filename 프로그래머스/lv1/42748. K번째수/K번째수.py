def solution(array, commands):
    answer = []
    for i in commands :
        prior = []
        prior = array[i[0]-1 : i[1]]
        prior.sort()
        answer.append(prior[i[2]-1])
    return answer