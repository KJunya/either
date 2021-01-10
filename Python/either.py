
class Either():
	class __Value():
		def __init__(self, value=None):
			self.__value = value

		# @returns the result of the given function
		# Check if value of self should be applied to the function
		def __do(self, func):
			return func(self.__value) if not self.__value is None else func()

		# @returns the result of function f or g
		# @param f : function to perform when left
		# @param g : function to perform when right
		def either(self, f, g):
			return self.__do(f if isinstance(self, Either.Left) else g)

		# @returns the value v or the result of function g
		# @param v : value
		# @param g : function to perform when right
		def fold(self, l, g):
			return l if isinstance(self, Either.Left) else self.__do(g)

		# @returns the value on left or, if right, the result of function g
		# @param g: function to perform when right
		def flat(self, g):
			return self.__value if isinstance(self, Either.Left) else self.__do(g)

	class Right(__Value):
		def __init__(self, value):
			super().__init__(value)

	class Left(__Value):
		def __init__(self, value):
			super().__init__(value)
