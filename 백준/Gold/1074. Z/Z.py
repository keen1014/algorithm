def z(N, r, c):
    if N==0:
        return 0
    
    elif r-(2**(N-1)) < 0 and c-(2**(N-1)) < 0:
        return z(N-1, r, c)
    
    elif r-(2**(N-1)) < 0 and c-(2**(N-1)) >= 0:
        return z(N-1, r, c-(2**(N-1)))+(2**(N-1))**2
        
    
    elif r-(2**(N-1)) >= 0 and c-(2**(N-1)) >= 0:
        return z(N-1, r-(2**(N-1)), c-(2**(N-1)))+((2**(N-1))**2)*3

    elif r-(2**(N-1)) >= 0 and c-(2**(N-1)) < 0:
        return z(N-1, r-(2**(N-1)), c)+((2**(N-1))**2)*2

    
import sys
input=sys.stdin.readline
N, r, c= map(int, input().strip().split())
print(z(N, r, c))