import curses
import random

from near import near
from rand_coord import rand_coord

import config

dirs = ( (+1, 0), (-1, 0), (0, -1), (0, +1) ) # Down, up, left, right

def main(stdscr):
	max_coord = stdscr.getmaxyx()

	snake = []
	snake.append(rand_coord(max_coord))

	for _ in range(config.start_len-1):
		l = near(snake[-1], max_coord)
		l = [i for i in l if i not in snake]
		snake.append(random.choice(l))

	food = None

	score = 0

	stdscr.clear()
	curses.curs_set(0)

	for coord in snake:
		stdscr.addch(*coord, config.snake_ch)
	stdscr.addch(*snake[-1], config.head_ch)

	key_down = 258

	direction = stdscr.getch() - key_down
	stdscr.addch(*snake[-1], config.snake_ch)

	stdscr.timeout(config.timeout)

	while True:
		ch = stdscr.getch()

		dir_change = ch - key_down in range(4)

		if (ch == -1) or dir_change:
			if dir_change:
				direction = ch - key_down

			new = list(snake[-1])
			for i, val in enumerate(dirs[direction]):
				new[i] += val

			for i, (new_val, max_val) in enumerate(zip(new, max_coord)):
				if new_val not in range(max_val):
					if not config.wrap_borders:
						return -1, score

					if new_val == max_val:
						new[i] = 0
					elif new_val == -1:
						new[i] = max_val-1

			new = tuple(new)

			if new in snake:
				return -1, score

			snake.append(new)
			stdscr.addch(*snake[-1], config.snake_ch)

			if (food in snake) or (food == None):
				score += 1

				while True:
					food = rand_coord(max_coord)

					if food not in snake:
						break

				stdscr.addch(*food, config.food_ch)

			else:
				stdscr.addch(*snake[0], ' ')
				snake.pop(0)

		elif ch == ord('q'):
			return 0, score

if __name__ == '__main__':
	reason, score = curses.wrapper(main)

	print('You {} with score {}'.format({-1: 'lose', 0: 'exited'}[reason], score))
