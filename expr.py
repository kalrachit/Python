def expr(st, c):
	ans = []
	currentchar = None
	count = 0
	for cc in st:
		if currentchar == cc:
			count = count +1
		else :
			ans = ans + ([currentchar] * min(c, count))
			currentchar = cc
			count =1

	ans =ans + ([currentchar] * min(c, count))
	ans = ''.join(ans)
	return  ans

def min(a,b):
	if a<b:
		return a
	else :
		return b
print(expr('aaabbaac',1))
print(expr('aaabbaac',2))
print(expr('aaabbaac',3))