import curses
import random
from time import sleep

from near import near
from rand_coord import rand_coord
from within import within

snake_ch = 'X'
head_ch = 'O'
food_ch = '@'

start_len = 5
timeout = 250

dirs = ( (+1, 0), (-1, 0), (0, -1), (0, +1) ) # Down, up, left, right

def step(stdscr, snake, direction):
	new = list(snake[-1])
	for i, val in enumerate(dirs[direction]):
		new[i] += val

	new = tuple(new)

	if (new in snake) or not (within(new, stdscr.getmaxyx())):
		return -1

	snake.append(new)
	stdscr.addch(*snake[-1], snake_ch)

	stdscr.addch(*snake[0], ' ')
	snake.pop(0)

	return 0

def main(stdscr):
	max_coord = stdscr.getmaxyx()

	snake = []
	snake.append(rand_coord(max_coord))

	for _ in range(start_len-1):
		l = near(snake[-1], max_coord)
		l = [i for i in l if i not in snake]
		snake.append(random.choice(l))

	stdscr.clear()
	curses.curs_set(0)

	for coord in snake:
		stdscr.addch(*coord, snake_ch)
	stdscr.addch(*snake[-1], head_ch)

	key_down = 258

	direction = stdscr.getch() - key_down
	stdscr.addch(*snake[-1], snake_ch)

	stdscr.timeout(timeout)

	while True:
		ch = stdscr.getch()

		if ch == -1:
			ret = step(stdscr, snake, direction)

			if ret != 0:
				return ret

		elif ch - key_down in range(4):
			direction = ch - key_down
			ret = step(stdscr, snake, direction)

			if ret != 0:
				return ret

		elif ch == ord('q'):
			return 0

if __name__ == '__main__':
	ret = curses.wrapper(main)

	print(ret)
