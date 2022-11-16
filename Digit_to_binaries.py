from math import *
def Bin(Y):
    "for binaries"
    X=0
    if Y>111111111111:
        X=X+2**12
        Y=Y-10**12
    if Y>11111111111:
        X=X+2**11
        Y=Y-10**11
    if Y>1111111111:
        X=X+2**10
        Y=Y-10**10  
    if Y>111111111:
        X=X+2**9
        Y=Y-10**9
    if Y>11111111:
        X=X+2**8
        Y=Y-10**8
    if Y>1111111:
        X=X+2**7
        Y=Y-10**7
    if Y>111111:
        X=X+2**6
        Y=Y-10**6
    if Y>11111:
        X=X+2**5
        Y=Y-10**5
    if Y>1111:
        X=X+2**4
        Y=Y-10**4
    if Y>111:
        X=X+2**3
        Y=Y-10**3
    if Y>11:
        X=X+2**2
        Y=Y-10**2
    if Y>1:
        X=X+2**1
        Y=Y-10**1
    if Y>0:
        X=X+2**0
        Y=Y-10**0
    return "X est égal à", X

from math import *
def Dig(X):
    "Dig for digits"
    Y=0
    t=0 
    "t pour nombre de tour"
    while X>0:
        if X%2==1:
            X=(X-1)/2
            Y=Y+1*10**t
            t=t+1
        else:
            X=X/2
            t=t+1
    return ('Y est égal à', Y)