# lambda function practice
a = list(range(1,11))

f = lambda x: x**2
print(list(map(f,a)))

g = lambda x: x*2
print(list(map(g,a)))

for y in map(lambda x: f(x)if x %2 == 0 else g(x),a):
    print(y,end = ' ')