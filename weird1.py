# Default variable(s) in function is/are initialized once
def foo(element, arr = []):
    arr.append(element)
    return arr

print(foo(1))
print(foo(2))
print(foo(3, []))

def foo2(element, arr = set()):
    arr.add(element)
    return arr

print(foo2(1))
print(foo2(2))
print(foo2(3, set()))
