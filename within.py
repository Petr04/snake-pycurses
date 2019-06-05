def within(coord, max_coord):
	for i, val in enumerate(coord):
		if not( 0 <= val < max_coord[i] ):
			return False

	return True
