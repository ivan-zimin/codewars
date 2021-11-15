# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    sum = 0
    for i in range(1, number):
        if((i % 3 == 0) or (i % 5 == 0)):
            sum += i
    return(sum)

print(solution(10))


# better solution
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)