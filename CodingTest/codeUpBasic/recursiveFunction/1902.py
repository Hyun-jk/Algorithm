def func(x):
    if x != 0:
        print(x) 
        func(x-1)

func(int(input()))