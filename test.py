import curses

def main(stdscr):
	stdscr.clear()

	y_max, x_max = stdscr.getmaxyx()

	stdscr.addch(y_max-1, x_max-1, '@') # Why I can't add char to this coord?

	stdscr.getch()

if __name__ == '__main__':
	curses.wrapper(main)
