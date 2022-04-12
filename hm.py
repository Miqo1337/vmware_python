s = 'Hello'


def changestr(s):
	s += ' World'
	return s;

print(s)
s = changestr(s)
print(s)

l = ['H','e','l','l','o']

def changelst(l):
	l.extend(['W', 'o', 'r',  'l', 'd'])
	return l

print(l)
print(changelst(l))
print(l)
