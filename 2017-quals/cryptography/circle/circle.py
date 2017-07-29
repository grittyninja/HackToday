#!/usr/bin/python

def encrypt(flag, n):
	check = [0 for i in range(len(flag))]
	point = 1
	result = flag[0]
	check[0] = 1
	i = 0

	while len(result) != len(flag):
		if check[i % len(flag)] == 0:
			if point == n:
				result += flag[i % len(flag)]
				check[i % len(flag)] = 1
				point = 0
		else:
			point -= 1
			
		i += 1
		point += 1
		
	return result

def decrypt():
	#not implemented yet
	pass
