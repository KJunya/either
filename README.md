# either
Functional programming style either-or library for multiple languages.
Functions exceutes one or the other depending on which side (left or right) it belongs to.

```
x :: Any value
p :: Left or Right
f :: Function for Left
g :: Function for Right

Either(p, f, g) ::
	if p in Left {
		return f(x)
	}
	else if p in Right {
		return g(x)
	}
```

# Implemented language

* Python

## planned
- [ ] Javascript
- [ ] Java (or mabye Kotlin)
- [ ] Swift
- [ ] C (or mabye Rust)
- [ ] Ruby
