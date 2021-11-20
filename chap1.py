def identity(x):
    return x

def compose(g,f):
    return lambda x : g(f(x))

# Test compose(g, id) = g and compose(id, f) = f for a single function input
assert compose(lambda x: 2*x, identity)(5) == 10
assert compose(identity, lambda x: 2*x)(5) == 10