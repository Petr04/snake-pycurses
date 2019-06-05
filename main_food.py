import curses
import random
from time import sleep

from near import near
from rand_coord import rand_coord

snake_ch = 'X'
head_ch = 'O'
food_ch = '@'

start_len = 5
timeout = 250

dirs = ( (+1, 0), (-1, 0), (0, -1), (0, +1) ) # Down, up, left, right

def step(stdscr, snake, direction, food):
	new = list(snake[-1])
	for i, val in enumerate(dirs[direction]):
		new[i] += val

	new = tuple(new)

	if new in snake:
		ret = -1

	if food in snake:
		ret = 1
		food = 

	snake.append(new)
	stdscr.addch(*snake[-1], snake_ch)

	stdscr.addch(*snake[0], ' ')
	snake.pop(0)

	return ret

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

	food = []
	while True:
		food = rand_coord(max_coord)

		if food not in snake:
			break

	stdscr.addch(*food, food_ch)

	key_down = 258

	direction = stdscr.getch() - key_down
	stdscr.addch(*snake[-1], snake_ch)

	stdscr.timeout(timeout)

	while True:
		ch = stdscr.getch()

		if ch == -1:
			ret = step(stdscr, snake, direction, food)

			if ret != 0:
				break

		elif ch - key_down in range(4):
			direction = ch - key_down
			ret = step(stdscr, snake, direction, food)

			if ret != 0:
				break

		elif ch == ord('q'):
			break

if __name__ == '__main__':
	curses.wrapper(main)
