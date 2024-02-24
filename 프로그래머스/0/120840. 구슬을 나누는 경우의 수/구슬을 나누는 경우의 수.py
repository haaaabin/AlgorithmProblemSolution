import math

def solution(balls, share):
    n = math.factorial(balls)
    m = math.factorial(share)
    bottom = math.factorial(balls - share) * m
    return n // bottom