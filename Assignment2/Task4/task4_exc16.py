print("16.a")
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

print("\n 16.b")
def a():
    try:
        f(x, 4)
    finally:
        print("after f")
        print("after f?")
a()

#in 16.b error is not handled, can be done using except