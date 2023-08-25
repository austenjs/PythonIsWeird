def foo(N):
    ans = []
    for i in range(N):
        ans.append(lambda x: i)
    return ans

for i, func in enumerate(foo(5)):
    print(func(i))
