def func(x):
    if x != 1:
        func(x-1)
    print(x)

func(int(input()))