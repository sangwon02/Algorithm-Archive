import sys
input = sys.stdin.readline

while True:
    n = input()
    if not n:  
        break
    
    n = int(n)
    li = [""] * (n+2)
    li[0] = "-"

    for i in range(1, n+1):
        li[i] = li[i-1] + " "*(3**(i-1)) + li[i-1]
    print(li[n])