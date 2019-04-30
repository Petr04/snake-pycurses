from random import randint

def rand_coord(max_coord):
	ret = []
	for i in max_coord:
		ret.append(randint(0, i-1))

	return tuple(ret)

if __name__ == '__main__':
	print(rand_coord( (10, 10) ))
