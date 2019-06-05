from within import within

def near(coord, max_coord):
	delta = (-1, 0, 1)
	ret = []

	for i in delta:
		for j in delta:
			if all([d == 0 for d in (i, j)]) or (not 0 in (i, j)):
				continue

			new_coord = []
			for t, val in enumerate(coord):
				new_coord.append(val + (i, j)[t])

			new_coord = tuple(new_coord)

			if within(new_coord, max_coord):
				ret.append(new_coord)

	return ret

if __name__ == '__main__':
	print(near( (0, 0), (10, 10) ))
