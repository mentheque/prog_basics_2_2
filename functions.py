def graph(f, n = 10, m = 0):
    n,m = min(n,m), max(n , m) + 1
    print(*[f"f({r}) = {f(r)}" for r in range(n, m)])
def eat(*cuisine):
    critical = 1
    for a in cuisine:
        critical *= a
    if critical%2:
        print("i like evens")
    else:
        print("ok")
def repeat(**dict):
    return [word for word, quant in dict.items() for a in range(quant)]


def demonstration():
    graph(lambda x:x*x)
    graph(abs)
    graph(lambda x: x*x, 11)
    graph(lambda x: x*x, 2, 28)
    print(repeat(hello = 2, cat = 3))
    eat(11, 12)
    eat(13)

demonstration()
