import math
def solution(numer1, denom1, numer2, denom2):
    upp = numer1*denom2+numer2*denom1
    und = denom1*denom2
    gcdnum = math.gcd(upp,und)
    return [upp/gcdnum,und/gcdnum]