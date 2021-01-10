from either import Either

f = lambda x : len(x)
g = lambda x : x + 1
isLeft = False

def func():
	return "derp" if isLeft else 10
v = func()
if v == "derp":
	r = f(v)
elif v == 10:
	r = g(v)
print(r)

# becomes

def func():
	return Either.Left("derp") if isLeft else Either.Right(10)

# either f("derp") or g(10)
r = func().either(f, g)
print(r)

# either "yohoho" or g(10)
r = func().fold("yohoho", g)
print(r)

# either "derp" or g(10)
r = func().flat(g)
print(r)
