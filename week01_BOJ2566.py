arr = [[0] * 9 for _ in range(9)]
for i in range(9):
    arr[i] = list(map(int, input().split()))
    
max = 0;
x = 0;
y = 0;

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
            x = i+1;
            y = j+1;
            max = arr[i][j];
print(max)
print(x, y)