import curses
import random
import enum

from near import near
from rand_coord import rand_coord

snake_ch = 'X'
head_ch = 'O' # Add head marking to program
tail_ch = '-'
food_ch = '@'

start_len = 5
timeout = 250

class Direction(enum.Enum):
	LEFT = curses.KEY_LEFT
	RIGHT = curses.KEY_RIGHT
	UP = curses.KEY_UP
	DOWN = curses.KEY_DOWN

def main(stdscr):
	y_max, x_max = stdscr.getmaxyx()

	snake = []
	snake.append(rand_coord( (y_max, x_max) ))

	for _ in range(start_len-1):
		l = near(snake[-1], (y_max, x_max))
		l = [i for i in l if i not in snake]
		snake.append(random.choice(l))

	stdscr.clear()
	curses.curs_set(0)

	for coord in snake:
		stdscr.addch(*coord, snake_ch)
	stdscr.addch(*snake[-1], head_ch)
	stdscr.addch(*snake[0], tail_ch)

	stdscr.timeout(timeout)

	while True:
		ch = stdscr.getch()

		if ch == -1:
			# stdscr.delch
			pass
		elif ch == ord('q'):
			break

if __name__ == '__main__':
	curses.wrapper(main)
