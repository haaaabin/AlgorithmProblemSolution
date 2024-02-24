def solution(rsp):
    temp = {'2':'0','0':'5','5':'2'}
    answer =''
    for i in rsp:
        answer+= temp.get(i)
    return answer