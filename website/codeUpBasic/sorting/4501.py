1    # 백설공주와 난장이

height = []
for _ in range(7):
    height.append(int(input()))

height.sort(reverse=True)
print(height[0])
print(height[1])
