import sys
input = sys.stdin.readline

T = int(input())

def before(str):
    stack = [] 
        
    for i in str:
        stack.append(i) # 일단 문자를 스택에 넣음
        
        # 스택의 마지막 4개 문자가 (xx)인지 확인
        if len(stack) >= 4 and stack[-1] == ")" and stack[-2] == "x" and stack[-3] == "x" and stack[-4] == "(" :
            # 괄호 풀어줌
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            
            stack.append("x")
            stack.append("x")
            
    # 리스트를 문자열로 바꿔 리턴
    return "".join(stack)

for _ in range(T):
    A = input().rstrip()
    B = input().rstrip()
    
    if before(A) == before(B):
        print("Yes")
    else:
        print("No")

