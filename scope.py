# The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):
#
# Local(L): Defined inside function/class
# Enclosed(E): Defined inside enclosing functions(Nested function concept)
# Global(G): Defined at the uppermost level
# Built-in(B): Reserved names in Python builtin modules

pi = 'outer pi variable'

def print_pi():
	pi = 'inner pi variable'
	print(pi)

print_pi()
print(pi)
