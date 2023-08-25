def foo(element, arr = []):
    arr.append(element)
    return arr

print(foo(1))
print(foo(2))
print(foo(3, []))
