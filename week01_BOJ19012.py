import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    st = input().rstrip()
    correct = 0;
    for j in st:
        if j == "(":
            correct += 1;
        elif j == ")":
            correct -= 1;
        if correct < 0:
            break;
            
    if correct == 0:
        print("YES")
    else:
        print("NO")