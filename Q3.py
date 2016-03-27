from scipy.misc import comb
from math import e

r = float(input("Input the interest rate: "))
z = float(input("Input the profit: "))
w = float(input("Input the operating cost: "))
Pm = float(input("Input the Pm: "))
Pw = float(input("Input Pw: "))
R = float(input("Input the profit rate: "))

def C(r,z,w):
    C = (25000*e**(13.5*r))/(r*(e**(13.5*r)-1))+(25000*e**(26*r))/(r*(e**(26*r)-1))+z+w
    return C

def A(Pm,Pw):
    sumM = 0
    sumW = 0
    for i in range(0,15,1):
        M=comb(14, i)*Pm**(14-i)*((1-Pm)**i)*25000*i
        sumM += M
    for j in range(0,27,1):
        W=comb(26, i)*Pw**(26-i)*((1-Pw)**i)*25000*i
        sumW += W
    A = sumM + sumW
    return A

if C(r,z,w)*R > A(Pm,Pw) > C(r,z,w):
    print("Should!")
else:
    print("Should not!")